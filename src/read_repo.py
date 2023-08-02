import os
import sys
import time
import datetime
from dotenv import load_dotenv
from git import Repo
from gui import user_allows_restart

def get_latest_commit(repo):
    repo.remotes.origin.pull()
    return repo.head.commit

def check_for_updates(repo):
    curr_commit = repo.head.commit
    latest_commit = get_latest_commit(repo)
    print(f'> Updated at {datetime.datetime.now()}')
    if curr_commit == latest_commit:
        return True
    else:
        return False

def read_repo():
    load_dotenv()
    repo_path = os.getenv('GIT_REPO_PATH')

    if repo_path == None:
        raise FileNotFoundError('Environment variables .env file not found.\nPlease create one based on the provided .env.example and try again.')

    repo = Repo(repo_path)
    curr_commit = repo.head.commit

    if not repo.bare:
        print(f'> Repo at {repo_path} successfully loaded at {datetime.datetime.now()}.')

        get_latest_commit(repo)
        on_latest_commit = True
        while on_latest_commit:
            print('> STATUS: Up to date!')
            time.sleep(10)
            on_latest_commit = check_for_updates(repo)

        if user_allows_restart():
            print('> STATUS: Restarting...')
            os.execv(sys.executable, ['python3'] + sys.argv)
        else:
            print('> STATUS: Out of date. Restart to run latest version.')
    else:
        print(f'> Could not load repo at {repo_path}.')	


if __name__ == "__main__":
    read_repo()
