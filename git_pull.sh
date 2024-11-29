#!/bin/bash

# Ensure you're in the correct directory (assuming script and repo are in the same folder)
REPO_DIR="$(pwd)"

# Navigate to the repository
cd "$REPO_DIR"

# Fetch updates from the remote
git fetch origin

# Check if the local branch is behind the remote
UPDATES=$(git status -uno | grep "Your branch is behind")

if [ -n "$UPDATES" ]; then
    echo "$(date): Updates found. Pulling changes." >> "$REPO_DIR/git_update.log"
    git reset --hard origin/main  # Reset to remote branch to overwrite local changes
    git pull >> "$REPO_DIR/git_update.log" 2>&1
else
    echo "$(date): No updates found." >> "$REPO_DIR/git_update.log"
fi
