#!/bin/bash
# session setup hook - runs at session start

# check if we're in a git repo and configure if needed
if git rev-parse --git-dir > /dev/null 2>&1; then
    # check if git user is configured for this repo
    current_email=$(git config user.email)
    current_name=$(git config user.name)

    # set git config if not already set correctly
    if [ "$current_email" != "isa.lucia.sch@gmail.com" ] || [ "$current_name" != "luckyisaisa" ]; then
        git config user.email "isa.lucia.sch@gmail.com"
        git config user.name "luckyisaisa"
    fi
fi

exit 0
