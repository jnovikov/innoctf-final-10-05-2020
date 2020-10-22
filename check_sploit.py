#!/usr/bin/env python3

import subprocess
import re
import sys

regexp = re.compile(r'[A-Z0-9]{31}=')

out = subprocess.check_output(["python3", "sploits/overheard/edit_post.py", "127.0.0.1"])

matches = regexp.findall(out.decode())

if len(matches) > 0:
    print("Exploit is working!!!", flush=True)
    sys.exit(1)
else:
    print("OK")
    sys.exit(0)
