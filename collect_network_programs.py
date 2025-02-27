"""
Description:
    This script collects programs and services using the network in SUSE Linux using the 'lsof' command and saves the output to a file.

Author:
    Jeevan Shetty

Chapter:
    Forensic Analysis

Usage:
    python3 collect_network_programs.py
"""

import os
import subprocess

class NetworkProgramsCollector:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def collect_network_programs(self):
        try:
            # Collect programs and services using the network using the 'lsof' command
            network_programs_output = subprocess.check_output(["lsof", "-i"])
            return network_programs_output.decode('utf-8')
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
    network_dir = os.path.join(forensics_dir, "network")
    os.makedirs(network_dir, exist_ok=True)

    # Initialize collector
    collector = NetworkProgramsCollector(network_dir)

    # Collect programs and services using the network
    programs_output = collector.collect_network_programs()
    programs_file = collector.save_output_to_file(programs_output, "network_programs.txt")
    print("Programs and services using the network saved to:", programs_file)

