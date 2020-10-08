"""
Wrapper around pytest that cleans up subprocesses
"""

import sys

import psutil
import pytest

try:
    code = pytest.main(sys.argv[1:])
finally:
    for child in reversed(psutil.Process().children(recursive=True)):
        try:
            child.kill()
            child.wait()
        except psutil.Error:
            pass

exit(code)
