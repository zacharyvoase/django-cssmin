<!--*-markdown-*-->

# `django-cssmin`

`django-cssmin` is a reusable application for [Django][] which makes it easy to
automatically [compress][] your CSS stylesheets.

  [django]: http://www.djangoproject.com/
  [compress]: http://developer.yahoo.com/yui/compressor/


## Why compress?

*   Reduce the overhead of multiple HTTP requests for multiple CSS files. By
    concatenating them into one file, the browser will only need to make one
    HTTP request, reducing server load and bandwidth.

*   Reduce the size of CSS files by stripping unnecessary bytes (whitespace, et
    cetera), saving network bandwidth and reducing page load times.

## Installation and Setup

*   Install the `django-cssmin` library:
    
        :::bash
        $ pip install django-cssmin # OR
        $ easy_install django-cssmin
    
    Either of these commands should install all the required dependencies. The
    YUI CSS compressor is installed via the [yuicompressor][] PyPI package; one
    way or another, `django-cssmin` expects a `yuicompressor` command to be
    available. If the PyPI package doesn’t install correctly for you, see
    [installing the YUI compressor](#installing-the-yui-compressor).

[yuicompressor]: http://pypi.python.org/pypi/yuicompressor

*   Add `'djcssmin'` to your `INSTALLED_APPS` setting.

*   Add the necessary settings to your `settings.py` file:

        :::python
        ## somewhere in settings.py
        CSSMIN_ROOT = '/path/to/my/project/'
        
        CSSMIN_INPUT = [
            #  YUI Reset CSS
            'http://yui.yahooapis.com/2.8.0r4/build/reset/reset.css',
            # 960 Grid System
            'media/css/960/reset.css',
            'media/css/960/text.css',
            'media/css/960/grid.css',
            # Local CSS Libraries
            'media/css/*.lib.css',
        ]

        CSSMIN_OUTPUT = 'media/css/style.min.css'
    
    More information on the available settings can be found [here](/settings).


## `DEBUG` mode

If `DEBUG` is set to `True` in your Django project when you run `django-cssmin`,
the CSS input files will only be concatenated to the output file, not
compressed. This allows you to debug your stylesheets with meaningful line
numbers during design, and then use the fully-minified version in production.
You can force specific behaviour with options to the `djboss cssmin` command;
see the output of `djboss cssmin --help` for more information.


## Usage

`django-cssmin` uses [`django-boss`][djboss], a library/tool for writing and
running Django management commands. This will be installed automatically by
setuptools when you install `django-cssmin`.

  [djboss]: http://github.com/zacharyvoase/django-boss

Usage is relatively simple:

    :::bash
    $ djboss --log-level DEBUG cssmin --prod-mode
    Saving http://yui.yahooapis.com/.../reset.css to a temporary file
    Saved http://yui.yahooapis.com/.../reset.css to tmp8QRfOa
    Reading tmp8QRfOa
    Reading media/css/960/reset.css
    Reading media/css/960/text.css
    Reading media/css/960/grid.css
    Minifying and writing to media/css/style.min.css
    Cleaning temporary file tmp8QRfOa

The compressed CSS stylesheet will be output to the filename given by the
`CSSMIN_OUTPUT` setting, in this case `media/css/style.min.css`.


## Installing the YUI Compressor

*   Download the yuicompressor JAR file from
    [here](http://yuilibrary.com/downloads/#yuicompressor).

*   Extract the `yuicompressor-x.y.z.jar` file to a path in your `JAVA_HOME`
    environment variable.

*   Make `yuicompressor` an alias for `java -jar yuicompressor-x.y.z.jar`,
    using a proxy `yuicompressor` script on your path:

        #!/bin/bash
        # For example, in /usr/bin/yuicompressor:
        java -jar yuicompressor-x.y.z.jar $*
    
    Ensure this file has the executable bit set (via
    `sudo chmod a+x /usr/bin/yuicompressor` or otherwise).

*   Test the installation by running `yuicompressor --help`; you should see this
    output:
    
        :::text
        Usage: java -jar yuicompressor-x.y.z.jar [options] [input file]
        
        Global Options
          -h, --help                Displays this information
          --type <js|css>           Specifies the type of the input file
          --charset <charset>       Read the input file using <charset>
          --line-break <column>     Insert a line break after the specified column number
          -v, --verbose             Display informational messages and warnings
          -o <file>                 Place the output into <file>. Defaults to stdout.
        
        JavaScript Options
          --nomunge                 Minify only, do not obfuscate
          --preserve-semi           Preserve all semicolons
          --disable-optimizations   Disable all micro optimizations
        
        If no input file is specified, it defaults to stdin. In this case, the 'type'
        option is required. Otherwise, the 'type' option is required only if the input
        file extension is neither 'js' nor 'css'.


## License

`django-cssmin` is licensed under the following MIT/X11-style license:

> Copyright (c) 2009 Zachary Voase
> 
> Permission is hereby granted, free of charge, to any person
> obtaining a copy of this software and associated documentation
> files (the "Software"), to deal in the Software without
> restriction, including without limitation the rights to use,
> copy, modify, merge, publish, distribute, sublicense, and/or sell
> copies of the Software, and to permit persons to whom the
> Software is furnished to do so, subject to the following
> conditions:
> 
> The above copyright notice and this permission notice shall be
> included in all copies or substantial portions of the Software.
> 
> THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
> EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES
> OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND
> NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT
> HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY,
> WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
> FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR
> OTHER DEALINGS IN THE SOFTWARE.
