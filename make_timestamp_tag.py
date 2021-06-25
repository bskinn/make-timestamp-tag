import argparse as ap
import subprocess as sp
import sys
import time

DEFAULT_STAMP_FORMAT = "%Y.%m.%d.%H%M"


def get_params():
    """Retrieve command-line parameters."""


def main():
    # Just implement. Will need return value later.
    # Will also want configurable tag format
    # Will probably want to proofread tag format, too.
    stamp = time.strftime("%Y.%m.%d.%H%M", time.localtime())

    sp.run(f"git tag {stamp}")


if __name__ == "__main__":
    sys.exit(main())
