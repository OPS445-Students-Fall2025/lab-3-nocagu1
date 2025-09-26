#!/usr/bin/env python3

#!/usr/bin/env python3
'''Lab 3 Inv 3 free space checker'''
# Author ID: nagu1

import subprocess

def free_space():
    # Run the Linux command
    cmd = "df -h | grep '/$' | awk '{print $4}'"
    process = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    output, error = process.communicate()

    # Decode to utf-8, strip newline, and return as string
    return output.decode('utf-8').strip()

if __name__ == '__main__':
    print(free_space())
