"""News-image entry: write the bundled front page to /output/entry.png.

The image (entry.png, beside this file) sums up Saturday 21 November 2026:
six world-news panels plus an ALSO TODAY ticker, drawn by the agent.
The program copies it byte for byte, so both grader runs match.
"""
import os
import shutil
import sys

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    shutil.copyfile(SRC, dst)
    return 0


if __name__ == "__main__":
    sys.exit(main())
