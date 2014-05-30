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
from pelican import signals as core_signals
from pprint import pprint
import os

from pelican.generators import Generator
from pelican import readers
from pelican import settings

from pelican.utils import pelican_open

from blinker import signal
tutorial_generator_init = signal('tutorial_generator_init')
tutorial_generator_finalized = signal('tutorial_generator_finalized')
tutorial_generator_preread = signal('tutorial_generator_preread')
tutorial_generator_context = signal('tutorial_generator_context')

from .generators import TutorialsGenerator

def get_generators(generators):
	return TutorialsGenerator

def register():
	core_signals.get_generators.connect(get_generators)
	try:
		from authordb import load_data_from_authordb
		tutorial_generator_context.connect(load_data_from_authordb)
	except Exception as exc:
		print("Unable to import and connect authordb")

