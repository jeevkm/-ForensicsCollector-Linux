#!/usr/bin/env python3

"""
Description:
    This script lists storage devices in SUSE Linux using the lsblk command.

Author:
    Jeevan Shetty

Chapter:
    Forensic Analysis

Usage:
    python3 discover_storage_devices.py
"""

import subprocess
import os

def discover_storage_devices():
    try:
        # Specify the full path for lsblk
        lsblk_path = "/usr/bin/lsblk"
        
        # Run lsblk command to list storage devices
        lsblk_output = subprocess.check_output([lsblk_path], universal_newlines=True)
        
        # Specify the full path for the output file
        output_dir = "/tmp/forensics/storage_devices"
        output_file = os.path.join(output_dir, "storage_devices.txt")
        
        # Create the output directory if it doesn't exist
        if not os.path.exists(output_dir):
            os.makedirs(output_dir)
        
        # Save the output to the file
        with open(output_file, "w") as f:
            f.write(lsblk_output)
        print(f"Storage devices information saved to: {output_file}")
    except FileNotFoundError:
        print("lsblk command not found. Make sure it is installed.")

if __name__ == "__main__":
    discover_storage_devices()

