# Regenerates all the .py files from the corresponding .ui files. This is done
# via the pyuic4 program.
#
# The idea here is that all auto-generated files begin with a 'ui_' prefix, and
# all implementation files don't. For example, the daily double choice dialog
# has a .ui file called ui_daily_double_popup.ui and a corresponding auto-
# generated .py file called ui_daily_double_popup.py. The implementation .py
# file is daily_double_popup.py (notice the lack of a 'ui_' prefix).
#
# DON'T EDIT THE AUTO-GENERATED .PY FILES!! Any time someone runs this script
# or regenerates them using pyuic4, your changes will get overwritten!

from glob import glob
import os
from subprocess import call

pyuic4 = '/sw/lib/qt4-mac/lib/python3.4/bin/pyuic4'

# find all .ui files (* means wildcard)
for file in glob(os.path.join('wheelofjeopardy', 'gui', 'pyqt', '*.ui')):
  # output file is the same name, but with a .py extension instead of .ui
  output_file = '%s.py' % (os.path.splitext(file)[0])

  # invoke the pyuic4 command
  call([pyuic4, file, '--output', output_file])
