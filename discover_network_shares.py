"""
Description:
    This script attempts to discover network shares in SUSE Linux by examining active network connections listening on port 445 using ss command and saves the output to a file.

Author:
    Jeevan Shetty

Chapter:
    Forensic Analysis

Usage:
    python3 discover_network_shares.py
"""

import os
import subprocess

class NetworkSharesDiscoverer:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def discover_network_shares(self):
        try:
            # Use ss command to find active network connections listening on port 445
            ss_output = subprocess.check_output(["ss", "-tln", "sport = :445"])
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
    shares_dir = os.path.join(forensics_dir, "network_shares")
    os.makedirs(shares_dir, exist_ok=True)

    # Initialize discoverer
    discoverer = NetworkSharesDiscoverer(shares_dir)

    # Discover network shares
    shares_output = discoverer.discover_network_shares()
    shares_file = discoverer.save_output_to_file(shares_output, "network_shares.txt")
    print("Information about network shares saved to:", shares_file)

