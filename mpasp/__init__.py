"""dPASP Magic for IPython"""

__version__ = "0.0.1"

from .magic import PaspMagic

def load_ipython_extension(ipython): ipython.register_magics(PaspMagic)
