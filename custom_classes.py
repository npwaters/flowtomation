import validate_time
import sys


class TimeOfDayService:
    def __init__(self, input_time):
        # set result to False
        self.result = ""
        self.status = 0
        # self.input_time = input_time
        self.validated_time = validate_time.convert_datetime_string(
            input_time,
        )

        if not self.validated_time:
            # provide an error message to stderr,
            # return code will be 1, and
            # a CalledProcessError exception will be raised
            self.status = "Invalid time given!"
        else:
            self.process_time(self.validated_time)

        self.result_bytes = self.result.encode(sys.stdout.encoding)

    def process_time(self, validated_time):
        pass

    def get_results(self):
        return self.status, self.result_bytes


class Morning(TimeOfDayService):
    def process_time(self, validated_time):
        if validated_time.hour < 12:
            self.result = "True"


class Afternoon(TimeOfDayService):
    def process_time(self, validated_time):
        if 12 <= validated_time.hour < 18:
            self.result = "True"


class Evening(TimeOfDayService):
    def process_time(self, validated_time):
        if 18 <= validated_time.hour < 24:
            self.result = "True"
