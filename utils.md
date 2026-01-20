# How to publish into github 


# create .gitignore file
echo "" > .gitignore

# Creates a new Git repository in your current folder. After this, Git starts tracking changes in your project
git init

# check status
git status

# create GitHub Repository in UI (just for the first time)

# Stages all files in the current directory for commit
git add .

# Creates a snapshot of your project with a message
git commit -m "publish first ml project"

# Connects your local Git repo to a remote GitHub repository.
git remote add origin https://github.com/kiks4tennis-hash/kaggle-titanic.git

# Renames your current branch to main.
git branch -M main

# Uploads your local main branch to GitHub.
git push -u origin main

