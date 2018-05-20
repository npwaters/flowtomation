import os
import sys
import time

file_modified_times = {}
app_file = "test.json"

file_modified_times[app_file] = {}

while True:
    result = ''
    app_file_info = os.stat(app_file)
    app_file_current_modified_time = app_file_info.st_mtime
    try:
        app_file_last_modified_time = file_modified_times.get(app_file)["file_last_modified"]
    except KeyError:
        file_modified_times.get(app_file)["file_last_modified"] = app_file_current_modified_time
        result = "no modified information found - first run"
        continue

    if app_file_last_modified_time < app_file_current_modified_time:
        result = "file modified since last run!"
        file_modified_times.get(app_file)["file_last_modified"] = app_file_current_modified_time
    else:
        result = "no changes detected since last run!"

    # app_file_current_modified_time = time.strftime(
    #     "%a, %d %b %Y %H:%M:%S +1000",
    #     time.localtime(app_file_info.st_mtime)
    # )


sys.exit()
