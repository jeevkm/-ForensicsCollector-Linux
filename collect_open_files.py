"""
Description:
    This script collects information about open files in SUSE Linux using the 'lsof' command and saves the output to a file.

Author:
    Jeevan Shetty

Chapter:
    Forensic Analysis

Usage:
    python3 collect_open_files.py
"""

import os
import subprocess

class OpenFilesCollector:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def collect_open_files(self):
        try:
            # Collect information about open files using the 'lsof' command
            open_files_output = subprocess.check_output(["lsof"])
            return open_files_output.decode('utf-8')
        except subprocess.CalledProcessError as e:
            return str(e)

    def save_output_to_file(self, output, filename):
        output_path = os.path.join(self.output_dir, filename)
        with open(output_path, 'w') as file:
            file.write(output)
        return output_path

if __name__ == "__main__":
    # Directory setup
    forensics_dir = "/tmp/forensics"
    open_files_dir = os.path.join(forensics_dir, "open_files")
    os.makedirs(open_files_dir, exist_ok=True)

    # Initialize collector
    collector = OpenFilesCollector(open_files_dir)

    # Collect information about open files
    open_files_output = collector.collect_open_files()
    open_files_file = collector.save_output_to_file(open_files_output, "open_files_info.txt")
    print("Information about open files saved to:", open_files_file)

