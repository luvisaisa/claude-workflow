#!/bin/bash
# auto-format python files after write/edit operations

# read stdin to get tool input
input=$(cat)

# extract file path from tool input
file_path=$(echo "$input" | python3 -c "
import json
import sys
try:
    data = json.load(sys.stdin)
    path = data.get('tool_input', {}).get('file_path', '')
    print(path)
except:
    pass
")

# only format python files
if [[ "$file_path" == *.py ]]; then
    if [ -f "$file_path" ]; then
        ruff format "$file_path" 2>/dev/null
        exit 0
    fi
fi

exit 0
