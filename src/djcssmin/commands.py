# -*- coding: utf-8 -*-

from cStringIO import StringIO
import glob
import logging
import os
import os.path as p

from django.core.exceptions import ImproperlyConfigured
from djboss.commands import *

from djcssmin import utils


LOG = logging.getLogger('django.djcssmin')


def resolve_patterns(patterns, root):
    """Resolve a list of globs/URLs into absolute filenames."""
    
    input_files, temp_files = [], []
    
    for pattern in patterns:
        # Handle URLs in the CSSMIN_INPUT setting.
        if pattern.startswith("http:"):
            temp_filename = utils.temp_fetch(pattern)
            input_files.append(temp_filename)
            temp_files.append(temp_filename)
        
        else:
            # Ensure glob patterns are absolute.
            glob_files = glob.glob(utils.make_abs(pattern, root))
            # Sort filenames within the results of a single pattern.
            glob_files.sort()
            
            for filename in glob_files:
                # Make sure there are no repetitions.
                if filename not in input_files:
                    input_files.append(filename)
    
    return input_files, temp_files


@command
@argument('-d', '--dev-mode', action='store_true', default=None, dest='development_mode',
          help="Don't minify (just concatenate). Defaults to the value of DEBUG.")
@argument('-p', '--prod-mode', action='store_false', dest='development_mode',
          help="Compress, even when DEBUG is True.")
def cssmin(args):
    """Compress the configured CSS stylesheets."""
    
    if not hasattr(args.settings, 'CSSMIN_INPUT'):
        raise ImproperlyConfigured("Must provide a CSSMIN_INPUT setting")
    elif not hasattr(args.settings, 'CSSMIN_OUTPUT'):
        raise ImproperlyConfigured("Must provide a CSSMIN_OUTPUT setting")
    
    root = utils.get_root(args.settings)
    
    # Set up development mode. If nothing is specified, this will default to the
    # value of `settings.DEBUG`. The `-d` and `-p` options override this value.
    if args.development_mode is None:
        development_mode = args.settings.DEBUG
    else:
        development_mode = args.development_mode
    
    # `temp_files` have to be deleted after processing, whether minification was
    # successful or not.
    input_files, temp_files = resolve_patterns(args.settings.CSSMIN_INPUT, root)
    
    try:
        # Get an absolute output filename.
        output_file = utils.make_abs(args.settings.CSSMIN_OUTPUT, root)
        
        if output_file in input_files:
            # This can happen if you output a '.css' file to the same directory
            # you're globbing from. Remove it from the input files.
            input_files.remove(output_file)
        
        input_io = StringIO()
        try:
            # Populate the input StringIO.
            for filename in input_files:
                if filename in temp_files:
                    LOG.info("Reading %s" % p.basename(filename))
                else:
                    LOG.info("Reading %s" % p.relpath(filename))
                
                # The additional whitespace/comments will be filtered out by the
                # compressor later on, unless we are in development mode, in
                # which case we want the whitespace and comments.
                input_io.write("/* FILE: %s */" % filename + os.linesep)
                input_io.write(utils.read_from(filename))
                input_io.write(os.linesep * 2)
            input_io.seek(0)
            
            output_io = open(output_file, 'w')
            try:
                output_io.write(utils.get_prolog(args.settings, root))
                
                if development_mode:
                    LOG.info("Writing to %s" % p.relpath(output_file))
                    output_io.write(input_io.getvalue())
                else:
                    # Minify and write the output.
                    LOG.info("Minifying and writing to %s" % p.relpath(output_file))
                    output_io.write(utils.compress(input_io.read()))
            finally:
                output_io.close() # Clean up.
        finally:
            input_io.close() # Clean up.
    
    finally:
        # Clean up.
        for temp_filename in temp_files:
            LOG.info("Cleaning temporary file %s" % p.basename(temp_filename))
            os.remove(temp_filename)
