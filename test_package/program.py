import subprocess
import sys


try:
    result = subprocess.run(
        'services/time_of_day/test_service.py',
        stdout=subprocess.PIPE,
        stderr=subprocess.STDOUT,
        check=True
    )
except subprocess.CalledProcessError as e:
    result = e
sys.exit()
