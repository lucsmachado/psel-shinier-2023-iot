import os
from dotenv import load_dotenv
from git import Repo

if __name__ == "__main__":
	load_dotenv()
	repo_path = os.getenv('GIT_REPO_PATH')
	repo = Repo(repo_path)
	if not repo.bare:
		print('Repo at {} successfully loaded.'.format(repo_path))
		origin = repo.remotes.origin
		origin.pull()
	else:
		print('Could not load repo at {}.'.format(repo_path))	
