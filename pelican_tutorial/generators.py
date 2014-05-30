# -*- coding: utf-8 -*-
from __future__ import unicode_literals, print_function

import time
import logging
from itertools import chain
from pelican.contents import is_valid_content
from pelican.utils import process_translations
from pelican import signals
from pelican.generators import CachingGenerator
from .contents import Tutorial
from .signals import *

logger = logging.getLogger(__name__)



# In order for the bits below to work we need to define various signals. I'm
# not sure about the details because docs on blinker and how it is used here
# are hazy at best. It appears you simply define them here and use them in the
# code below. YMMV.


class TutorialsGenerator(CachingGenerator):
    """
    Generate Tutorials

    """

    def __init__(self, *args, **kwargs):
        self.tutorials = []
        self.hidden_tutorials = []
        self.hidden_translations = []
        super(TutorialsGenerator, self).__init__(*args, **kwargs)
        tutorial_generator_init.send(self)
        self.content_name="Tutorials"

    def generate_report(self):
        """
        This will report to stdout the number of tutorials and hidden tutorials processed.
        """
        print( "Tutorials: {0} published and {1} hidden in {2:0.2f} seconds".format( len(self.tutorials), len(self.hidden_tutorials), self.elapsed ) )

    def generate_context(self):
        """
        Here is the meat of the class - where the heavy lifting occurs.  It
        generates a list of tutorials and places them in the context object so we
        can access them in templates.

        Some of this is leftover from the stock Article class. Ideally those aspect
        will be removed as it is shown they can be safely done away with.
        However, this works.
        """

        all_tutorials = []
        hidden_tutorials = []
        for f in self.get_files(
                self.settings['TUTORIAL_DIR'],
                exclude=self.settings['TUTORIAL_EXCLUDES']):
            tutorial = self.get_cached_data(f, None)
            if tutorial is None:
                try:
                    tutorial = self.readers.read_file(
                        base_path=self.path, path=f, content_class=Tutorial,
                        context=self.context,
                        preread_signal=tutorial_generator_preread,
                        preread_sender=self,
                        context_signal=tutorial_generator_context,
                        context_sender=self)
                except Exception as e:
                    logger.warning('Could not process {}\n{}'.format(f, e))
                    continue

                if not is_valid_content(tutorial, f):
                    continue

                self.cache_data(f, tutorial)

            self.add_source_path(tutorial)

            if tutorial.status == "published":
                all_tutorials.append(tutorial)
                for author_data in self.context['site_authors']:
                    if author_data.name == tutorial.author.name:
                        tutorial.author.data = author_data
            elif tutorial.status == "hidden":
                hidden_tutorials.append(tutorial)
            else:
                logger.warning("Unknown status %s for file %s, skipping it." %
                               (repr(tutorial.status),
                                repr(f)))

        self.tutorials, self.translations = process_translations(all_tutorials)
        self.hidden_tutorials, self.hidden_translations = (
            process_translations(hidden_tutorials))

        self._update_context(('tutorials', ))
        self.context['TUTORIALS'] = self.tutorials

        self.save_cache()
        self.readers.save_cache()
        tutorial_generator_finalized.send(self)

    def generate_output(self, writer):
        """
        Here we generate the HTML page form the tutorial(s).
        """
        start = time.time()
        for tutorial in chain(self.translations, self.tutorials, self.hidden_translations, self.hidden_tutorials):
            #for author_data in self.context['site_authors']:
                #if author_data.name == tutorial.author.name:
                    #tutorial.author.data = author_data
            writer.write_file(
                tutorial.save_as, self.get_template(tutorial.template),
                self.context, tutorial=tutorial,
                relative_urls=self.settings['RELATIVE_URLS'],
                override_output=hasattr(tutorial, 'override_save_as'))
        self.elapsed = time.time() - start
        self.generate_report()

