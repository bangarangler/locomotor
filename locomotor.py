import os
from git import Repo
from dotenv import load_dotenv
load_dotenv()

if __name__ == "__main__":

    repo_path = os.getenv('GIT_REPO_PATH')
    git_email = os.getenv('GIT_EMAIL')
    git_user_name = os.getenv('GIT_USER_NAME')
    print(repo_path)
    my_repo = Repo(repo_path)
    print(my_repo)

    def print_repo(my_repo):
        print(f"Repo description: {my_repo.description}")
        print(f"Repo active branch is {my_repo.active_branch}")

    def locomotor(branch):
        """
        This function will...
        1. checkout the branch name provided
        """
        # already_a_branch = False
        # existing_branches = []
        if branch in my_repo.branches:
            print(f"{branch} is already a branch")
            my_repo.git.checkout(branch)
        else:
            print(f"{branch} is not a branch yet")
            my_repo.git.checkout("-b", branch)
        # for sing_branch in my_repo.branches:
            # print(f"branch : {branch}")
            # print(f"sing_branch : {str(sing_branch)}")
            # print(
            #     f"sing_branch is {str(sing_branch)} while branch is {branch}")
        #     existing_branches = []
        #     if str(sing_branch) == branch:
        #         print("setting already_a_branch to True")
        #         already_a_branch = True
        #         # my_repo.git.checkout(branch)
        #         # return
        #     else:
        #         print("setting already_a_branch to False")
        #         already_a_branch = False
        #         # my_repo.git.checkout("-b", branch)
        #         # return
        # if (already_a_branch == True):
        #     print("inside already_a_branch == True")
        #     # my_repo.git.checkout(branch)
        # else:
        #     print("inside else already_a_branch == False")
        #     # my_repo.git.checkout("-b", branch)
        # print("pulling...")
        # # my_repo.remotes.origin.pull()

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
