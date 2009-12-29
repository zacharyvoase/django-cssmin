# Settings

`django-cssmin` will determine how to compress your CSS files based on the
following settings.

`DEBUG`
:   If this is `True`, `django-cssmin` will not (by default) compress the output
    CSS. This is to help with interactive debugging during design. It can be
    overridden with the options to the command-line interface; see the output of
    `djboss cssmin --help` for more information.

`CSSMIN_INPUT` (required)
:   A list of [glob][] patterns or URLs which `django-cssmin` will expand to get
    a list of CSS stylesheet filenames. For example:
      
  [glob]: http://docs.python.org/library/glob.html
    
        CSSMIN_INPUT = [
            # YUI Reset CSS
            'http://yui.yahooapis.com/2.8.0r4/build/reset/reset.css',
            ## 960 Grid System
            'media/css/960/reset.css',
            'media/css/960/text.css',
            'media/css/960/grid.css',
            # Local CSS Libraries
            'media/css/*.lib.css',
        ]
    
    First, the YUI CSS Reset library is downloaded from Yahoo’s servers. The
    specified CSS files for the 960.gs framework are included in the given
    order. Then, all CSS files in the `media/css/` directory ending in 
    `.lib.css` are included. Globs which do not match anything just resolve to
    empty lists.
    
    All relative paths in globs are first resolved. `django-cssmin` will check 
    for the following settings, in this order:
    
    *   `CSSMIN_ROOT`
    *   `PROJECT_DIR`
    *   `PROJECT_ROOT`
    
    Finally, if none exist, the directory containing the settings module will be
    considered the base path for resolution.

`CSSMIN_OUTPUT` (required)
:   The filename to which the compressed CSS style data will be written.
    Relative output filenames will be resolved as specified above.

`CSSMIN_ROOT` (optional)
:   See the paragraph on relative glob resolution above.

`CSSMIN_PROLOG` (optional)
:   A filename (relative or absolute) which contains a piece of text to include 
    at the beginning of the compressed CSS stylesheet. This will usually be a
    comment containing a copyright statement or license information.
