# -*- python -*-
import os
import sys
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
print sys.path
from web import app as application  # noQA
