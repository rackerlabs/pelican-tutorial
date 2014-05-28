from pelican.contents import Page

class Tutorial(Page):
    """
    An Tutorial is meeting, conference, or other occurrence which can be displayed
    and indexed on a static site generation. It is intended to be used with the
    JSON generator and custom templates.
    """
    base_properties = ('title','description','author','level')
    mandatory_properties = ('title','author','level')
    default_template = 'tutorial'
