"""
Description:
    This script attempts to discover connected users on SUSE Linux by using the 'w' command and saves the output to a file.

Author:
    Jeevan Shetty

Chapter:
    Forensic Analysis

Usage:
    python3 discover_connected_users.py
"""

import os
import subprocess

class ConnectedUsersDiscoverer:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def discover_connected_users(self):
        try:
            # Use 'w' command to find connected users
            w_output = subprocess.check_output(["w"])
            return w_output.decode('utf-8')
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
    users_dir = os.path.join(forensics_dir, "connected_users")
    os.makedirs(users_dir, exist_ok=True)

    # Initialize discoverer
    discoverer = ConnectedUsersDiscoverer(users_dir)

    # Discover connected users
    users_output = discoverer.discover_connected_users()
    users_file = discoverer.save_output_to_file(users_output, "connected_users.txt")
    print("Information about connected users saved to:", users_file)

