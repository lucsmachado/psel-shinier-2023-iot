import os
import time
import datetime
from dotenv import load_dotenv
from git import Repo

def read_repo():
    load_dotenv()
    repo_path = os.getenv('GIT_REPO_PATH')

    if repo_path == None:
        raise FileNotFoundError('Environment variables .env file not found.\nPlease create one based on the provided .env.example and try again.')

    repo = Repo(repo_path)

    if not repo.bare:
        print(f'Repo at {repo_path} successfully loaded at {datetime.datetime.now()}.')
        origin = repo.remotes.origin
        origin.pull()
        while True:
            time.sleep(10)
            origin.pull()
            print(f'Updated at {datetime.datetime.now()}')
    else:
        print(f'Could not load repo at {repo_path}.')	


if __name__ == "__main__":
    read_repo()
