# Pelican-Tutorials

Pelican-Tutorials is a plugin for pelican to add the ability to specify content
as a Tutorial and have it use a custom template.

# What it Does

The primary purpose of this plugin is to provide a Tutorial content type. This
allows simple and easy to understand template separation. It also allows you to
specify a more specific set of mandatory metadata.

# Installation 

Once the repo is cloned, copy the pelican-tutorial directory to the (or one of
the) path specified in `PLUGIN_PATH`, or add the path of the checkout to the
`PLUGIN_PATHS` variable.


# Configuration

Tutorial-specific requried configuration variables with good defaults are:

```python
TUTORIAL_DIR="tutorial"
TUTORIAL_URL="tutorials/{slug}.html"
TUTORIAL_SAVE_AS = 'tutorials/{slug}.html'
TUTORIAL_EXCLUDES=''
```


To create an tutorial you will create a "normal" article file in this
directory. It will need to have a minimum set of fields in order to meet the
basic criteria, as seen in `contents.py`.


# Template

With these bits in place you can now use the template engine to generate
per-tutorial pages. The default template is `tutorial.html`. Coming soon will be an
`tutorials.html` option to specify a template for generating a list of all tutorials
-- much the same as is done with blog posts.

Included in the plugin is a `templates` directory with a sample `tutorial.html`
template. It is very minimal showing just the basic details of the tutorial. It is
intended to provide a starting point for how to use the module in templates.
