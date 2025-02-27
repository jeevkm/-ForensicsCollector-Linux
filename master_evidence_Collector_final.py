#!/usr/bin/env python3

"""
Description:
    This script executes multiple forensic analysis scripts in a SUSE Linux system and captures their outputs.

Author:
    [Author's Name]

Chapter:
    [Chapter Name]

Usage:
    python3 master_evidence_Collector_final.py
"""

import subprocess

def execute_script(script_name, *args):
    try:
        cmd = ["python3", script_name, *args]
        output = subprocess.check_output(cmd)
        print(f"{script_name} output saved to: {output.decode().strip()}")
        return True
    except subprocess.CalledProcessError as e:
        print(f"Error executing {script_name}: {e}")
        return False

def main():
    scripts_to_execute = [
        "collect_ram_content.py",
        "collect_network_info.py",
        "collect_dns_cache.py",
        "collect_running_processes.py",
        "collect_network_connections.py",
        "collect_network_programs.py",
        "collect_open_files.py",
        "discover_network_shares.py",
        "discover_open_ports.py",
        "discover_connected_users.py",
        "discover_active_network_shares.py",
        "monitor_syslog_activity.py",
        "discover_storage_devices.py",
        "get_system_details.py",
        "get_environment_variables.py"
    ]

    success_count = 0
    failure_count = 0

    for script in scripts_to_execute:
        script_name = script.split(".")[0]
        if script_name == "collect_ram_content":
            arg = "ramcontent"
        else:
            arg = ""
        if execute_script(script, arg):
            success_count += 1
        else:
            failure_count += 1

    print(f"\nExecution completed. {success_count} out of {len(scripts_to_execute)} scripts executed successfully.")
    if failure_count > 0:
        print(f"{failure_count} scripts failed to execute.")

if __name__ == "__main__":
    main()

