from subprocess_utils import *

__author__ = "Gautham Kolluru"

"""
pp : project path
ipagr : initiate project as a git repository
agr : add git remote
"""


def crd(pp):
    """
    crd : Create Directory
    """
    return sprun(['mkdir', pp])


def chd(pp):
    """
    chd : Change Directory
    """
    return sprun(['cd', pp])


def rf(pp) -> list:
    """
    rf : read file
    """
    with open(pp) as fp:
        lines = fp.readlines()
    return lines


def wf(pp: str, d="", dl=[]) -> rf:
    """
    wf : write file
    """
    with open(pp, "w") as fp:
        if d and isinstance(d, str):
            fp.write(d)
        if dl and isinstance(dl, list):
            fp.writelines([l+"\n" for l in dl])
    return rf(pp)


def ipagr(pp):
    return sprun(["git", "init"], pp=pp)


def agr(pp, link):
    return sprun(["git", "remote", "add", "origin", link], pp=pp)
