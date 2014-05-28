#!/usr/bin/env python

from __future__ import print_function
try:
	import json
except ImportError:
	try:
		import simplejson as json
	except ImportError:
		json = None

import six
import hashlib
from pelican import signals
from pprint import pprint
import os

from pelican.generators import Generator
from pelican import readers
from pelican import settings

from pelican.utils import pelican_open

from blinker import signal
tutorial_generator_init = signal('tutorial_generator_init')
tutorial_generator_finalized = signal('tutorial_generator_finalized')

from .generators import TutorialsGenerator

class TutorialReader(readers.BaseReader):
	enabled = bool(json)
	file_extensions = ["tutorial"]
	def read(self, source_path):
		with pelican_open(source_path) as text:
			print( text )
			data = {}
			pre_data = json.loads(text)
		for k,v in pre_data.items():
			data[k.lower()] = v
		return ("",data)


def add_reader(readers):
	readers.reader_classes['tutorial'] = TutorialReader


def initTutorials(generator):
	tutorials_dict = {}
	try:
		tutorials = generator.context['tutorials']
	except KeyError:
		generator.context['tutorials'] = tutorials = {}

def get_generators(generators):
	return TutorialsGenerator

def register():
	signals.readers_init.connect(add_reader)
	signals.get_generators.connect(get_generators)

