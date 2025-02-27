#!/usr/bin/env python3

"""
Description:
    This script retrieves environment variables in SUSE Linux.

Author:
    [Your Name]

Chapter:
    Forensic Analysis

Usage:
    python3 get_environment_variables.py
"""

import os

def get_environment_variables():
    # Get the environment variables
    env_vars = os.environ
    # Save the environment variables to a file
    output_path = "/tmp/forensics/environment_variables.txt"
    with open(output_path, "w") as f:
        f.write("Environment Variables:\n")
        for key, value in env_vars.items():
            f.write(f"{key}: {value}\n")
    print(f"Environment variables saved to: {output_path}")

if __name__ == "__main__":
    get_environment_variables()

