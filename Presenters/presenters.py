import sys
from pathlib import Path
from collections import namedtuple

PARENT_PATH = Path(__file__).parent.parent
sys.path.insert(0, str(PARENT_PATH))



class HomePage(object):

    def __init__(self, view):
        super().__init__()
        self.View = view


class SecurityPrices(object):

    def __init__(self, view):
        self.View = view

