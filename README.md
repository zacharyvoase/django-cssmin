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
    
    Either of these commands should install all the required dependencies.

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
    
    More information on the available settings can be found
    [here](http://github.com/zacharyvoase/django-cssmin/blob/master/doc/settings.md).


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


## (Un)license

This is free and unencumbered software released into the public domain.

Anyone is free to copy, modify, publish, use, compile, sell, or distribute this
software, either in source code form or as a compiled binary, for any purpose,
commercial or non-commercial, and by any means.

In jurisdictions that recognize copyright laws, the author or authors of this
software dedicate any and all copyright interest in the software to the public
domain. We make this dedication for the benefit of the public at large and to
the detriment of our heirs and successors. We intend this dedication to be an
overt act of relinquishment in perpetuity of all present and future rights to
this software under copyright law.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS
FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS BE
LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF
CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

For more information, please refer to <http://unlicense.org/>
