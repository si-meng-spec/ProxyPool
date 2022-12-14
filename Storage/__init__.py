import os
import sys

sys.path.append(os.path.dirname(__file__))

from IPStorage import IPProxyStorage
from utils import singleton

__all__ = ["IPProxyStorage", "singleton"]
