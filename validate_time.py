import datetime


def convert_datetime_string(input_time):
    try:
        validated_time = datetime.datetime.strptime(
            input_time.rstrip(),
            "%d/%m/%Y %H:%M:%S"
        )
        return validated_time

    except ValueError:
        # exit with status code
        return False


def convert_datetime_string_part2(input_time):
    try:
        validated_time = datetime.datetime.strptime(
            input_time.rstrip(),
            "%d/%m/%Y %H:%M:%S"
        )
        # part 2
        return True

    except ValueError:
        # exit with status code
        return False
