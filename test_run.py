import subprocess
import sys
import shlex


result = subprocess.run(
    # [
    #     "ls",
    #     "-la",
    #     "/mnt/c/Users/natha/Downloads"
    # ],
    shlex.split("ls -la /mnt/c/Users/natha/Downloads"),
    # shell=True,
    stdout=subprocess.PIPE,
    stderr=subprocess.PIPE,
    # TODO: implement python 3.6 encoding option
    # python 3.6
    # encoding="utf-8"
)


directory_listing = result.stdout.decode("utf-8").split("\n")

sys.exit()
