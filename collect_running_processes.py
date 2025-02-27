"""
Description:
    This script collects the list of running processes in SUSE Linux and saves the output to a file.

Author:
    Jeevan Shetty

Chapter:
    Forensic Analysis

Usage:
    python3 collect_running_processes.py
"""

import os
import subprocess

class ProcessCollector:
    def __init__(self, output_dir):
        self.output_dir = output_dir

    def collect_running_processes(self):
        try:
            # Collect the list of running processes using the 'ps' command
            process_output = subprocess.check_output(["ps", "aux"])
            return process_output.decode('utf-8')
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
    processes_dir = os.path.join(forensics_dir, "processes")
    os.makedirs(processes_dir, exist_ok=True)

    # Initialize collector
    collector = ProcessCollector(processes_dir)

    # Collect running processes
    process_output = collector.collect_running_processes()
    process_file = collector.save_output_to_file(process_output, "running_processes.txt")
    print("List of running processes saved to:", process_file)

