import sys
import time
import datetime

second = None

while second != 0:
    second = datetime.datetime.now().second
    print(second)
    time.sleep(1)


sys.exit()
