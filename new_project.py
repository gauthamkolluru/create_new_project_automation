import os
import sys

from file_utils import *

"""
pn : project name
PD : Project Directory
pp : project path
crp : create project
rd : return dictionary
"""

PD = "C:\\Users\\sakollur\\Documents"

PY_GIT_IGNORE_LIST = [
    "__pycache__/",
    ".vscode",

    "*.json",
    "**/*.json",

    "*.pickle",
    "**/*.pickle",

    "rough.py",
    "**/rough.py",

    "sample.py",
    "**/sample.py"
]


def cr_gitignore(pp):
    return wf(pp=os.path.join(pp, ".gitignore"), dl=PY_GIT_IGNORE_LIST)


def crp(pp):
    if os.path.exists(pp):
        return False
    if crd(pp).returncode == 0:
        if cr_gitignore(pp):
            if ipagr(pp).returncode == 0:
                if agr(pp, input("Paste Git repo link : ")).returncode == 0:
                    return True
    return False


def main():
    rd = dict()
    for pn in sys.argv[1:]:
        rd.update({
            pn: "created" if crp(os.path.join(PD, pn)) else "Not created"
        })
    return rd


if __name__ == "__main__":
    print(main())
