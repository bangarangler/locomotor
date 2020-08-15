import os
from git import repo


def locomotor(branch):
    """
    This function will...
    1. checkout the branch name provided
    """
    repo.checkout("-b", branch)


locomotor("testPythonBranch")
