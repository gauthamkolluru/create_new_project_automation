import subprocess


def sprun(args, pp=None):
    if pp:
        return subprocess.run(args, shell=True, cwd=pp)
    return subprocess.run(args, shell=True)
