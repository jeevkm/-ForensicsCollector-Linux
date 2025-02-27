#!/usr/bin/env python3

"""
Description:
    This script identifies active network shares on SUSE Linux by parsing the output of the 'mount' command.
    It saves the list of active network shares to a file.

Author:
    Jeevan Shetty

Chapter:
    Forensic Analysis

Usage:
    python3 discover_active_network_shares.py
"""

import os
import subprocess

def discover_active_network_shares():
    output_file = '/tmp/forensics/network_shares/active_network_shares.txt'

    # Run the 'mount' command and capture its output
    output = subprocess.run(["mount", "-v"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

    # Decode the byte string output
    output_text = output.stdout.decode('utf-8')

    # Parse the output to find active network shares
    network_shares = [line.split()[0] for line in output_text.splitlines() if line.startswith('//')]

    # Save the list of active network shares to the output file
    os.makedirs(os.path.dirname(output_file), exist_ok=True)
    with open(output_file, 'w') as f:
        for share in network_shares:
            f.write(share + '\n')

    return network_shares

if __name__ == "__main__":
    active_network_shares = discover_active_network_shares()
    if active_network_shares:
        print("Active network shares identified and saved to:", output_file)
    else:
        print("No active network shares found.")

