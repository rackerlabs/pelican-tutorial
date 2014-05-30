from blinker import signal

tutorial_generator_init = signal('tutorial_generator_init')
tutorial_generator_finalized = signal('tutorial_generator_finalized')
tutorial_generator_preread = signal('tutorial_generator_preread')
tutorial_generator_context = signal('tutorial_generator_context')

