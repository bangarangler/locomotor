import os
import sys
# from subprocess import call
import subprocess
from git import Repo
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":

    repo_path = os.getenv('GIT_REPO_PATH')
    git_email = os.getenv('GIT_EMAIL')
    git_user_name = os.getenv('GIT_USER_NAME')
    nvm_rc = os.getenv('NVMRC_PATH')
    print(repo_path)
    my_repo = Repo(repo_path)
    print(my_repo)

    def print_repo(my_repo):
        print(f"Repo description: {my_repo.description}")
        print(f"Repo active branch is {my_repo.active_branch}")

    def locomotor(branch):
        """
        This function will...
        1. checkout the branch name provided or create a new branch with that name
        2. check .nvmrc for current node version
        """
        if branch in my_repo.branches:
            print(f"{branch} is already a branch")
            my_repo.git.checkout(branch)
        else:
            print(f"{branch} is not a branch yet")
            my_repo.git.checkout("-b", branch)
        print("pulling...")
        my_repo.remotes.origin.pull()

        with open(nvm_rc) as f:
            read_data = f.read()
            # print(read_data)
        print(read_data)
        # call([f"nvm" f"use {str(read_data)}"])
        nvm_command = f"nvm use {str(read_data)}"
        # switch_nvm = os.system(nvm_command)
        switch_nvm = subprocess.Popen(['/bin/zsh', '-i', '-c', nvm_command])
        switch_nvm.communicate()
        exit_code = switch_nvm.wait()
        print(f"exit_code is {exit_code}")
        if exit_code != 0:
            sys.exit("Done with Process")
        print(f"ran with exit code {switch_nvm}")

    with my_repo.config_writer() as git_config:
        git_config.set_value('user', 'email', git_email)
        git_config.set_value('user', 'name', git_user_name)
    with my_repo.config_reader() as git_config:
        print(git_config.get_value('user', 'email'))
        print(git_config.get_value('user', 'name'))

    if not my_repo.bare:
        print(f"Repo at {repo_path} successfully loaded.")
        print_repo(my_repo)
        locomotor("master")

    else:
        print("Could not load repo")


# locomotor("testPythonBranch")
