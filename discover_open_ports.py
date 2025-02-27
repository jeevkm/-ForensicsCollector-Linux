"""
Description:
    This script attempts to discover open ports on SUSE Linux by examining active network connections using the ss command and saves the output to a file.

Author:
    Jeevan Shetty

Chapter:
    Forensic Analysis

Usage:
    python3 discover_open_ports.py
"""

import os
import subprocess

class OpenPortsDiscoverer:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def discover_open_ports(self):
        try:
            # Use ss command to find active network connections and extract open ports
            ss_output = subprocess.check_output(["ss", "-tln"])
            return ss_output.decode('utf-8')
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
    ports_dir = os.path.join(forensics_dir, "open_ports")
    os.makedirs(ports_dir, exist_ok=True)

    # Initialize discoverer
    discoverer = OpenPortsDiscoverer(ports_dir)

    # Discover open ports
    ports_output = discoverer.discover_open_ports()
    ports_file = discoverer.save_output_to_file(ports_output, "open_ports.txt")
    print("Information about open ports saved to:", ports_file)

