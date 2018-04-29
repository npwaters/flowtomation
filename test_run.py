import subprocess
import sys


result = subprocess.run(
    [
        "ls",
        "-la",
    ],
    # shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE
)

sys.exit()
