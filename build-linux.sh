#!/bin/bash
# build script for linux distributable

set -e  # exit on error

echo "========================================"
echo "claude workflow setup - linux build"
echo "========================================"

# check if python3 is available
if ! command -v python3 &> /dev/null; then
    echo "error: python3 not found"
    echo "install python3 using your package manager:"
    echo "  ubuntu/debian: sudo apt install python3 python3-venv python3-pip"
    echo "  fedora: sudo dnf install python3 python3-pip"
    echo "  arch: sudo pacman -S python python-pip"
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
rm -rf build dist claude-workflow-setup

# ensure .claude folder is present
if [ ! -d ".claude" ]; then
    echo "error: .claude folder not found"
    echo "this script must be run from the project root"
    exit 1
fi

# build executable
echo "building linux executable..."
pyinstaller --clean --noconfirm \
    --onefile \
    --windowed \
    --name "claude-workflow-setup" \
    --hidden-import PySide6.QtCore \
    --hidden-import PySide6.QtGui \
    --hidden-import PySide6.QtWidgets \
    claude_setup.py

# verify build
if [ -f "dist/claude-workflow-setup" ]; then
    # make executable
    chmod +x dist/claude-workflow-setup

    echo ""
    echo "========================================"
    echo "build successful!"
    echo "========================================"
    echo ""
    echo "output: dist/claude-workflow-setup"
    echo ""
    echo "to test:"
    echo "  ./dist/claude-workflow-setup"
    echo ""
    echo "to distribute:"
    echo "  1. compress: cd dist && tar -czf claude-workflow-setup-linux.tar.gz claude-workflow-setup"
    echo "  2. share the .tar.gz file"
    echo ""
    echo "note: users may need to install qt libraries:"
    echo "  ubuntu/debian: sudo apt install libxcb-xinerama0"
    echo "  fedora: sudo dnf install xcb-util-wm"
    echo ""
else
    echo ""
    echo "========================================"
    echo "build failed!"
    echo "========================================"
    echo "check the output above for errors"
    exit 1
fi
