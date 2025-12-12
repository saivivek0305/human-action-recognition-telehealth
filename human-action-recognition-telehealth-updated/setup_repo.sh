#!/bin/bash
# USAGE: ./setup_repo.sh <GITHUB_USERNAME> <REPO_NAME>
set -e
if [ "$#" -ne 2 ]; then
  echo "Usage: $0 <github-username> <repo-name>"
  exit 1
fi
GH_USER=$1
REPO=$2

git init
git add .
git commit -m "chore: project scaffold"
git branch -M main

# Create remote repo using gh CLI (must be authenticated)
gh repo create ${GH_USER}/${REPO} --public --source=. --remote=origin --push
