# Project 0
## Command line git

- status
	- Shows status of the local repository. This status includes:
		- number of local commits that have not been synced with remote (GitHub)
		- list of files in local folder than are NOT being tracked by git
		- list of files in local folder that have changes that need to be committed
	- `git status`

- clone
	- Downloads a git repository
	- `git clone git@github.com:trevorsweigart/example-repo.git`

- add
	- Adds changed files to tracking
	- `git add new_file`

- rm
	- Removes file from system or from tracking
	- `git rm not_needed_file`

- commit
	- A change or group of changes that was done to codebase
		- A way to track changes for version control over time
	- `git commit -m "feature/added new feature"`

- push
	- Pushes changes/commits staged in git to GitHub
	- `git push`


- fetch
	- Updates repository from remote
		- Does not overwrite current local files
		- Can download in indiviual branch
	- `git fetch sample_repo development_brach`

- merge
	- merges git branches on local system
