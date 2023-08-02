import os
import time
import datetime
from dotenv import load_dotenv
from git import Repo

def read_repo(path):
    repo = Repo(path)
    if not repo.bare:
        print(f'Repo at {path} successfully loaded at {datetime.datetime.now()}.')
        origin = repo.remotes.origin
        origin.pull()
        while True:
            time.sleep(3600)
            origin.pull()
            print(f'Updated at {datetime.datetime.now()}')
    else:
        print(f'Could not load repo at {path}.')	


if __name__ == "__main__":
    load_dotenv()
    repo_path = os.getenv('GIT_REPO_PATH')

    if repo_path == None:
        raise FileNotFoundError('Environment variables .env file not found.\nPlease create one based on the provided .env.example and try again.')

    read_repo(repo_path)
