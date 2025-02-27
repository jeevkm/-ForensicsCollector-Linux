"""
Description:
    This script collects network information including routing table, ARP cache, and kernel statistics
    using various Linux tools.

Author:
    Jeevan Shetty

Chapter:
    Forensic Analysis

Usage:
    python3 collect_network_info.py

"""

import os
import subprocess

class NetworkInfoCollector:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def collect_routing_table(self):
        try:
            # Collect routing table using ip route show command
            routing_table_output = subprocess.check_output(["ip", "route", "show"])
            return routing_table_output.decode('utf-8')
        except subprocess.CalledProcessError:
            return "Error: Failed to retrieve routing table."

    def collect_arp_cache(self):
        try:
            # Read ARP cache from /proc/net/arp
            with open("/proc/net/arp", "r") as arp_file:
                arp_cache_output = arp_file.read()
            return arp_cache_output
        except FileNotFoundError:
            return "Error: Failed to retrieve ARP cache."

    def collect_kernel_statistics(self):
        try:
            # Collect kernel statistics using ss command
            kernel_stats_output = subprocess.check_output(["ss", "-s"])
            return kernel_stats_output.decode('utf-8')
        except subprocess.CalledProcessError:
            return "Error: Failed to retrieve kernel statistics."

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
    collector = NetworkInfoCollector(network_dir)

    # Collect routing table
    routing_table_output = collector.collect_routing_table()
    routing_table_file = collector.save_output_to_file(routing_table_output, "routing_table.txt")
    print("Routing table information saved to:", routing_table_file)

    # Collect ARP cache
    arp_cache_output = collector.collect_arp_cache()
    arp_cache_file = collector.save_output_to_file(arp_cache_output, "arp_cache.txt")
    print("ARP cache information saved to:", arp_cache_file)

    # Collect kernel statistics
    kernel_stats_output = collector.collect_kernel_statistics()
    kernel_stats_file = collector.save_output_to_file(kernel_stats_output, "kernel_statistics.txt")
    print("Kernel statistics saved to:", kernel_stats_file)

