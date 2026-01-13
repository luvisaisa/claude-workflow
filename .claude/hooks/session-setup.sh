#!/bin/bash
# session setup hook - runs at session start

# check if we're in a git repo and configure if needed
if git rev-parse --git-dir > /dev/null 2>&1; then
    # load git config from .claude/git-config if it exists
    if [ -f "$CLAUDE_PROJECT_DIR/.claude/git-config" ]; then
        source "$CLAUDE_PROJECT_DIR/.claude/git-config"

        # check if git user is configured for this repo
        current_email=$(git config user.email)
        current_name=$(git config user.name)

        # set git config if not already set correctly
        if [ -n "$GIT_USER_EMAIL" ] && [ "$current_email" != "$GIT_USER_EMAIL" ]; then
            git config user.email "$GIT_USER_EMAIL"
        fi

        if [ -n "$GIT_USER_NAME" ] && [ "$current_name" != "$GIT_USER_NAME" ]; then
            git config user.name "$GIT_USER_NAME"
        fi
    fi
fi

exit 0
