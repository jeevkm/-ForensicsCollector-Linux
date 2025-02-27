"""
Description:
    This script collects RAM content from a SUSE system for forensic evidence collection without directly reading from /dev/mem.

Author:
    Jeevan Shetty

Chapter:
    Forensic Analysis

Usage:
    python3 collect_ram_content.py <output_file>
"""

import subprocess
import sys

class RamContentCollector:
    def __init__(self, output_file):
        self.output_file = output_file

    def collect_ram_content(self):
        try:
            # Collect RAM content using dd tool with input from /proc/kcore
            subprocess.run(["dd", "if=/proc/kcore", "of=" + self.output_file, "bs=1M", "count=1024"])
            return "RAM content collected and saved to " + self.output_file
        except subprocess.CalledProcessError as e:
            return "Error occurred during RAM collection: " + str(e)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 collect_ram_content.py <output_file>")
        sys.exit(1)

    output_file = sys.argv[1]
    ram_collector = RamContentCollector(output_file)

    print(ram_collector.collect_ram_content())

