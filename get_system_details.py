#!/usr/bin/env python3

"""
Description:
    This script retrieves date, time, and uptime details in SUSE Linux.

Author:
    Jeevan Shetty

Chapter:
    Forensic Analysis

Usage:
    python3 get_system_details.py
"""

import datetime
import os
import psutil

def get_system_details():
    try:
        # Create the directory if it doesn't exist
        output_dir = "/tmp/forensics/system_details/"
        os.makedirs(output_dir, exist_ok=True)

        # Get current date and time
        current_datetime = datetime.datetime.now()
        date_time_str = current_datetime.strftime("%a %b %d %H:%M:%S %Z %Y")

        # Get uptime
        uptime = datetime.timedelta(seconds=psutil.boot_time())

        # Save the output to a file
        output_path = os.path.join(output_dir, "system_details.txt")
        with open(output_path, "w") as f:
            f.write("Date and Time: {}\n".format(date_time_str))
            f.write("Uptime: {}\n".format(str(uptime)))
        print(f"System details saved to: {output_path}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    get_system_details()

