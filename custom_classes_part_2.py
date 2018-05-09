import sys
import json


class AppService:
    # the AppService needs to do the following when intitialised
    # -initialise dictionaries to store:
    # --output
    # --input

    app_service_input = {}
    app_service_output = {}
    result = ''
    status = 0

    def convert_output_to_json_bytes(self):
        return json.dumps(self.app_service_output).encode(sys.stdout.encoding)

    def get_results(self):
        # return self.status, self.result_bytes
        # part 2
        return self.status,\
               self.convert_output_to_json_bytes()