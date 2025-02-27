"""
Description:
    This script collects active network connections in SUSE Linux using the 'ss' command and saves the output to a file.

Author:
    Jeevan Shetty

Chapter:
    Forensic Analysis

Usage:
    python3 collect_network_connections.py
"""

import os
import subprocess

class NetworkConnectionsCollector:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def collect_network_connections(self):
        try:
            # Collect active network connections using the 'ss' command
            connections_output = subprocess.check_output(["ss", "-tuln"])
            return connections_output.decode('utf-8')
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
    collector = NetworkConnectionsCollector(network_dir)

    # Collect active network connections
    connections_output = collector.collect_network_connections()
    connections_file = collector.save_output_to_file(connections_output, "active_network_connections.txt")
    print("Active network connections saved to:", connections_file)

