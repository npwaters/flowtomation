import datetime


def convert_datetime_string(input_time):
    try:
        validated_time = datetime.datetime.strptime(
            input_time,
            "%d/%m/%Y %H:%M:%S"
        )
        return validated_time

    except ValueError:
        # exit with status code
        return False
