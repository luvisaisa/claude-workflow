#!/usr/bin/env python3
"""
convert icon to platform-specific formats.

converts DEV-WF-ICON.png to:
- icon.icns (macos)
- icon.ico (windows)
- icon-{size}.png (linux, multiple sizes)
"""

from __future__ import annotations

import sys
from pathlib import Path

try:
    from PIL import Image
except ImportError:
    print("error: pillow not installed")
    print("install: pip3 install pillow")
    sys.exit(1)

def create_icns(source_path: Path, output_path: Path) -> bool:
    """
    create macos .icns file from png.

    args:
        source_path: path to source png
        output_path: path to output .icns file

    returns:
        success status
    """
    print(f"creating macos icon: {output_path}")

    # load source image
    img = Image.open(source_path)

    # icns requires specific sizes
    sizes = [16, 32, 64, 128, 256, 512, 1024]

    # create iconset directory
    iconset_path = output_path.parent / f"{output_path.stem}.iconset"
    iconset_path.mkdir(exist_ok=True)

    # create all required sizes
    for size in sizes:
        # standard resolution
        resized = img.resize((size, size), Image.Resampling.LANCZOS)
        resized.save(iconset_path / f"icon_{size}x{size}.png")

        # retina resolution (2x)
        if size <= 512:
            retina_size = size * 2
            resized_2x = img.resize((retina_size, retina_size), Image.Resampling.LANCZOS)
            resized_2x.save(iconset_path / f"icon_{size}x{size}@2x.png")

    # convert iconset to icns using macos tool
    import subprocess
    try:
        result = subprocess.run(
            ["iconutil", "-c", "icns", str(iconset_path), "-o", str(output_path)],
            capture_output=True,
            text=True,
        )

        if result.returncode != 0:
            print(f"warning: iconutil failed: {result.stderr}")
            print("note: icns creation requires macos with iconutil")
            return False

        # cleanup iconset directory
        import shutil
        shutil.rmtree(iconset_path)

        print(f"✓ created {output_path}")
        return True

    except FileNotFoundError:
        print("warning: iconutil not found (macos only)")
        print(f"iconset directory created at: {iconset_path}")
        print("manually convert with: iconutil -c icns " + str(iconset_path))
        return False

def create_ico(source_path: Path, output_path: Path) -> bool:
    """
    create windows .ico file from png.

    args:
        source_path: path to source png
        output_path: path to output .ico file

    returns:
        success status
    """
    print(f"creating windows icon: {output_path}")

    # load source image
    img = Image.open(source_path)

    # ico supports multiple sizes in one file
    sizes = [(16, 16), (32, 32), (48, 48), (64, 64), (128, 128), (256, 256)]

    # create images at each size
    images = []
    for size in sizes:
        resized = img.resize(size, Image.Resampling.LANCZOS)
        images.append(resized)

    # save as ico with all sizes
    img.save(output_path, format='ICO', sizes=sizes)

    print(f"✓ created {output_path}")
    return True

def create_png_icons(source_path: Path, output_dir: Path) -> bool:
    """
    create multiple png sizes for linux.

    args:
        source_path: path to source png
        output_dir: directory for output files

    returns:
        success status
    """
    print(f"creating linux icons: {output_dir}")

    # load source image
    img = Image.open(source_path)

    # common linux icon sizes
    sizes = [16, 22, 24, 32, 48, 64, 128, 256, 512]

    output_dir.mkdir(exist_ok=True)

    for size in sizes:
        resized = img.resize((size, size), Image.Resampling.LANCZOS)
        output_file = output_dir / f"icon-{size}.png"
        resized.save(output_file)

    # also copy original
    import shutil
    shutil.copy(source_path, output_dir / "icon-original.png")

    print(f"✓ created {len(sizes) + 1} icons in {output_dir}")
    return True

def main() -> None:
    """main entry point."""
    # paths - look for icon in assets directory
    source = Path("assets/DEV-WF-ICON.png")

    if not source.exists():
        print(f"error: source icon not found: {source}")
        print("place DEV-WF-ICON.png in assets/ directory")
        sys.exit(1)

    print(f"source icon: {source}")
    print(f"size: {source.stat().st_size / 1024:.1f} kb")

    # verify source is valid
    try:
        img = Image.open(source)
        print(f"dimensions: {img.size[0]}x{img.size[1]}")
        print(f"format: {img.format}")
        print()
    except Exception as e:
        print(f"error: invalid image file: {e}")
        sys.exit(1)

    # create output directory
    icons_dir = Path("assets/icons")
    icons_dir.mkdir(exist_ok=True)

    # convert to each format
    success = True

    # macos .icns
    icns_path = icons_dir / "icon.icns"
    if not create_icns(source, icns_path):
        success = False

    # windows .ico
    ico_path = icons_dir / "icon.ico"
    if not create_ico(source, ico_path):
        success = False

    # linux png icons
    linux_dir = icons_dir / "linux"
    if not create_png_icons(source, linux_dir):
        success = False

    print()
    if success:
        print("✅ all icons created successfully")
        print(f"\noutput directory: {icons_dir}")
        print(f"  - icon.icns (macos)")
        print(f"  - icon.ico (windows)")
        print(f"  - linux/icon-*.png (linux)")
    else:
        print("⚠️  some icons created with warnings")
        print("check output above for details")

if __name__ == "__main__":
    main()
