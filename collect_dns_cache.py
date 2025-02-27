"""
Description:
    This script collects DNS cache details from SUSE Linux using the 'getent hosts' command and saves the output to a file.

Author:
    Jeevan Shetty

Chapter:
    Forensic Analysis

Usage:
    python3 collect_dns_cache.py
"""

import os
import subprocess

class DNSCacheCollector:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def collect_dns_cache(self):
        try:
            # Collect DNS cache details using the 'getent hosts' command
            dns_cache_output = subprocess.check_output(["getent", "hosts"])
            return dns_cache_output.decode('utf-8')
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
    dns_dir = os.path.join(forensics_dir, "dns")
    os.makedirs(dns_dir, exist_ok=True)

    # Initialize collector
    collector = DNSCacheCollector(dns_dir)

    # Collect DNS cache details
    dns_cache_output = collector.collect_dns_cache()
    dns_cache_file = collector.save_output_to_file(dns_cache_output, "dns_cache.txt")
    print("DNS cache details saved to:", dns_cache_file)

