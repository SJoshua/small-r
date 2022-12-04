"""utils"""
import logging
import sys

from rich.traceback import install
from rich.logging import RichHandler

# only enable rich on terminal
if sys.stdin and sys.stdin.isatty():
    logging.basicConfig(handlers=[RichHandler()], datefmt="[%X]", format="%(message)s", level=logging.DEBUG)
    install(show_locals=True)

logger = logging.getLogger()
