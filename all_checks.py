#!/usr/bin/env python3
import os.path

def check_reboot():

    """Returns True if the computar has a pending reboot."""
    return os.path.exists("/run/reboot-required")

def main():
    pass

main()
