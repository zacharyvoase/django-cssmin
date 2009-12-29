# -*- coding: utf-8 -*-

import logging
import os
import subprocess
import tempfile
import urllib2
import urlparse


LOG = logging.getLogger('django.djcssmin')


## workaround for Python pre-2.6.
if not hasattr(os.path, 'relpath'):
    def relpath(path, start=os.path.curdir):
        """Return a relative version of a path"""
        
        if not path:
            raise ValueError("no path specified")
        
        start_list = os.path.abspath(start).split(os.path.sep)
        path_list = os.path.abspath(path).split(os.path.sep)
        
        # Work out how much of the filepath is shared by start and path.
        i = len(os.path.commonprefix([start_list, path_list]))
        
        rel_list = [os.path.pardir] * (len(start_list)-i) + path_list[i:]
        if not rel_list:
            return os.path.curdir
        return os.path.join(*rel_list)
    os.path.relpath = relpath



def compress(input_string):
    """Use the YUI CSS compressor on a CSS string, returning a string."""
    
    pipe = subprocess.Popen(['yuicompressor', '--type', 'css'],
                            stdin=subprocess.PIPE, stdout=subprocess.PIPE)
    return pipe.communicate(input_string)[0]


def get_root(settings):
    """Get the directory from which to resolve the `CSSMIN_INPUT` globs."""
    
    if hasattr(settings, 'CSSMIN_ROOT'):
        return settings.CSSMIN_ROOT
    elif hasattr(settings, 'PROJECT_DIR'):
        return settings.PROJECT_DIR
    elif hasattr(settings, 'PROJECT_ROOT'):
        return settings.PROJECT_ROOT
    return os.path.dirname(os.path.abspath(settings.__file__))


def get_prolog(settings, root):
    """Get the prolog data from the `CSSMIN_PROLOG` setting."""
    
    if hasattr(settings, 'CSSMIN_PROLOG'):
        filename = make_abs(settings.CSSMIN_PROLOG, root)
        if not os.path.exists(filename):
            LOG.warn("Specified CSSMIN_PROLOG does not exist, continuing anyway")
        else:
            return read_from(filename)
    return ''


def make_abs(path, root):
    """Ensure a path is absolute."""
    
    return path if os.path.isabs(path) else os.path.abspath(os.path.join(root, path))


def temp_fetch(url):
    """Fetch a URL and save it in a temporary file, returning the filename."""
    
    conn = urllib2.urlopen(url)
    try:
        fp = tempfile.NamedTemporaryFile(delete=False)
        LOG.info("Saving %s to a temporary file" % truncate_url(url))
        try:
            fp.write(conn.read())
        finally:
            fp.close()
    finally:
        conn.close()
    
    LOG.info("Saved %s to %s" % (truncate_url(url), os.path.basename(fp.name)))
    return fp.name


def truncate_url(url):
    """Return a short version of a URL."""
    
    split = list(urlparse.urlsplit(url))
    
    path = split[2]
    if path == '/' or path.count('/') <= 2:
        pass
    elif path.endswith('/'):
        split[2] = '/.../' + '/'.join(path.rsplit('/', 2)[-2:])
    else:
        split[2] = '/.../' + path.rsplit('/', 1)[-1]
    
    return urlparse.urlunsplit(split)


def read_from(filename):
    fp = open(filename)
    try:
        return fp.read()
    finally:
        fp.close()
