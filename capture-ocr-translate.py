#! /usr/bin/env -S nix run nixpkgs#uv -- run --script
# /// script
# requires-python = ">=3.13"
# dependencies = []
# ///

import os
import subprocess
import sys

def capture_screenshot():
    desktop_session = os.environ.get('DESKTOP_SESSION')
    
    if desktop_session == 'sway':
        result = subprocess.run(['grim', '-g', subprocess.check_output(['slurp']).strip()], stdout=open('/tmp/tmp.just_random_name.png', 'wb'))
    elif desktop_session in ['plasmawayland', 'plasma']:
        result = subprocess.run(['spectacle', '--region', '--nonotify', '--background', '--output', '/tmp/tmp.just_random_name.png'])
    else:
        print("Failed to know desktop type")
        sys.exit(1)

    # Check if the screenshot was successfully created
    if not os.path.exists('/tmp/tmp.just_random_name.png'):
        print("Error: Screenshot was not created.")
        sys.exit(1)

def perform_ocr():
    # Check if the screenshot file exists before performing OCR
    if not os.path.exists('/tmp/tmp.just_random_name.png'):
        print("Error: Input file for OCR does not exist.")
        sys.exit(1)
    subprocess.run(['tesseract', '/tmp/tmp.just_random_name.png', '/tmp/tmp.just_random_name', '--oem', '1', '-l', 'eng'])

def open_in_goldendict():
    with open('/tmp/tmp.just_random_name.txt', 'r') as file:
        content = file.read()
    subprocess.run(['goldendict', content])

def cleanup():
    os.remove('/tmp/tmp.just_random_name.png')
    os.remove('/tmp/tmp.just_random_name.txt')

if __name__ == "__main__":
    capture_screenshot()
    perform_ocr()
    open_in_goldendict()
    cleanup()