#!/bin/bash
# build script for macos distributable

set -e  # exit on error

echo "========================================"
echo "claude workflow setup - macos build"
echo "========================================"

# check if python3 is available
if ! command -v python3 &> /dev/null; then
    echo "error: python3 not found"
    echo "install python from https://www.python.org/downloads/"
    exit 1
fi

# create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo "creating virtual environment..."
    python3 -m venv venv
fi

# activate virtual environment
echo "activating virtual environment..."
source venv/bin/activate

# install dependencies
echo "installing dependencies..."
pip install --upgrade pip
pip install -r requirements.txt
pip install pyinstaller

# clean previous builds
echo "cleaning previous builds..."
rm -rf build dist "Claude Workflow Setup.app"

# ensure .claude folder is present
if [ ! -d ".claude" ]; then
    echo "error: .claude folder not found"
    echo "this script must be run from the project root"
    exit 1
fi

# build executable
echo "building macos app bundle..."
pyinstaller --clean --noconfirm claude-setup.spec

# verify build
if [ -d "dist/Claude Workflow Setup.app" ]; then
    echo ""
    echo "========================================"
    echo "build successful!"
    echo "========================================"
    echo ""
    echo "output: dist/Claude Workflow Setup.app"
    echo ""
    echo "to test:"
    echo "  open 'dist/Claude Workflow Setup.app'"
    echo ""
    echo "to distribute:"
    echo "  1. compress: cd dist && zip -r 'claude-workflow-setup-macos.zip' 'Claude Workflow Setup.app'"
    echo "  2. share the .zip file"
    echo ""
    echo "note: users may need to allow the app in system preferences > security & privacy"
    echo "      (right-click app > open to bypass gatekeeper)"
    echo ""
else
    echo ""
    echo "========================================"
    echo "build failed!"
    echo "========================================"
    echo "check the output above for errors"
    exit 1
fi
