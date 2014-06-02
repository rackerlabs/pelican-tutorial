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


# Tutorial Metadata

## Mandatory Properties

Mandatory properties are entries in the metadata/front-matter which are
required for the tutorial to be processed. The idea here is to ensure
tutorial-specific data is present. 

1. Level
	This field identifies the level of difficulty or required knowledge this
	tutorial was written for.

2. Author
	The person or persons who write this tutorial.

3. Title
	The title of the article.

## Recommended Properties

In order to obtain a better experience, certain properties are available. It is
recommended these be present in order to take full advantage of templating and
per-tutorial informatioobtain a better experience, certain properties are
available. It is recommended these be present in order to take full advantage
of templating and per-tutorial information

1. Subtitle
	Usually used for a more descriptive single-line explanation of what the
	tutorial is for.  # Template

2. Repository 
	All tutorials which involve code should have the source code described in
	the tutorial available. This property can represent a source repository
	such as Github, but could also be a direct-to-download link.

3. Description
	This is a summary field use din most templating to provide a *brief*
	description of the tutorial.

With these bits in place you can now use the template engine to generate
per-tutorial pages. The default template is `tutorial.html`. Coming soon will be a
`tutorials.html` option to specify a template for generating a list of all tutorials
-- much the same as is done with blog posts.
