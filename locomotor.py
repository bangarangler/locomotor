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

    # with my_repo.config.writer() as git_config:
    #     git_config.set_value('user', 'email', git_email)
    #     git_config.set_value('user', 'name', git_user_name)
    # with my_repo.config_reader() as git_config:
    #     print(git_config.get_value('user', 'email'))
    #     print(git_config.get_value('user', 'name'))

    if not my_repo.bare:
        print(f"Repo at {repo_path} successfully loaded.")
        print_repo(my_repo)

    else:
        print("Could not load repo")


# def locomotor(branch):
#     """
#     This function will...
#     1. checkout the branch name provided
#     """
#
#
# locomotor("testPythonBranch")
