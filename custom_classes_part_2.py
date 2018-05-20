import validate_time
import sys
import json


class AppService:
    result = ''
    status = 0

    # the AppService needs to do the following when intitialised
    # -initialise dictionaries to store:
    # --output
    # --input
    app_service_input = {}
    app_service_output = {}

    def convert_output_to_json_bytes(self):
        return json.dumps(self.app_service_output).encode(sys.stdout.encoding)

    def get_results(self):
        return self.status,\
               self.convert_output_to_json_bytes()


class TimeOfDayService(AppService):
    def __init__(self, input_time):
        input_time = json.loads(
            input_time
        ).get("data")

        # the program has already validated the time
        # so all we need is the datetime object
        self.validated_time = validate_time.convert_datetime_string(
            input_time,
        )

        self.process_time(self.validated_time)

        self.result_bytes = self.result.encode(sys.stdout.encoding)

    def process_time(self, validated_time):
        pass


class Morning(TimeOfDayService):
    def process_time(self, validated_time):
        if validated_time.hour < 12:
            self.app_service_output["data"] = True
        else:
            self.app_service_output["data"] = False


class Afternoon(TimeOfDayService):
    def process_time(self, validated_time):
        if 12 <= validated_time.hour < 18:
            self.app_service_output["data"] = True
        else:
            self.app_service_output["data"] = False


class Evening(TimeOfDayService):
    def process_time(self, validated_time):
        if 18 <= validated_time.hour < 24:
            self.app_service_output["data"] = True
        else:
            self.app_service_output["data"] = False
