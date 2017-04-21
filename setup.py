#!/usr/bin/env python

# FIXME: HACK: Asegura ejecución de youtubedl
import os
import commands
BASE_PATH = os.path.dirname(__file__)
you_lib = os.path.join(BASE_PATH, "youtube_dl")
you_file = os.path.join(BASE_PATH, "youtube-dl")
print commands.getoutput('chmod -R 755 %s' % you_lib)
print commands.getoutput('chmod 755 %s' % you_file)

from sugar.activity import bundlebuilder
bundlebuilder.start()