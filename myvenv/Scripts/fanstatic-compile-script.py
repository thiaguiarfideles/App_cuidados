#!c:\users\thiag\pycharmprojects\rogti\myvenv\scripts\python.exe
# EASY-INSTALL-ENTRY-SCRIPT: 'fanstatic==1.1','console_scripts','fanstatic-compile'
__requires__ = 'fanstatic==1.1'
import re
import sys
from pkg_resources import load_entry_point

if __name__ == '__main__':
    sys.argv[0] = re.sub(r'(-script\.pyw?|\.exe)?$', '', sys.argv[0])
    sys.exit(
        load_entry_point('fanstatic==1.1', 'console_scripts', 'fanstatic-compile')()
    )
