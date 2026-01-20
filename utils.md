# How to publish into github 


## 1. create .gitignore file
echo "" > .gitignore

## 2. Creates a new Git repository in your current folder. After this, Git starts tracking changes in your project
git init

## 3. check status
git status

## 4. create GitHub Repository in UI. (only first time)

## 5. Stages all files in the current directory for commit
git add .

## 6. Creates a snapshot of your project with a message
git commit -m "publish first ml project"

## 7. Connects your local Git repo to a remote GitHub repository. (only first time)
git remote add origin https://github.com/kiks4tennis-hash/kaggle-titanic.git

## 8. Renames your current branch to main. (only first time)
git branch -M main

## 9. Uploads your local main branch to GitHub.
git push -u origin main