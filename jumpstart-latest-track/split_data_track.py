import ast
import os
from datetime import datetime
from insert import insert_flight, insert_ground
import json
import sys

def split_data(file_path):
    struct = {}
    if os.path.exists("./log/messages.log"):
        os.remove("./log/messages.log")
        return
    try:
        with open(file_path) as f:
            content = f.read()
        try: #try parsing to dict
            dataform = str(content).strip("'<>() ").replace('\'', '\"')
            new_dict = json.loads(dataform)


            terminal_data = new_dict.get('ns2:TATrackAndFlightPlan')
            if terminal_data:
                insert_flight(new_dict)
            else:
                pass
            f.close()
            os.remove(file_path)

        except:
            pass
            # print(repr(content))
            # print(sys.exc_info())

    except IOError:
        pass
