"""Maybe I'll understand how to do packages."""

from importlib.metadata import PackageNotFoundError, version

try:
    __version__ = version("super-nice-package-sb-nc")
except PackageNotFoundError:
    __version__ = "uninstalled"
__author__ = "Nicolas Chiaruttini"
__email__ = "nicolas.chiaruttini@epfl.ch"
