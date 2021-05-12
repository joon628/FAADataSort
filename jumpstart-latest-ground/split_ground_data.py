import ast
import os
from datetime import datetime
from insert import insert_flight, insert_ground
import json

def split_data(file_path):
    if os.path.exists("./log/messages.log"):
        os.remove("./log/messages.log")
        return
    try:
        with open(file_path) as f:
            content = f.read()
        if content != None:
            print(content)
            new_dict = json.loads(content)
            terminal_data = new_dict.get('ns2:TATrackAndFlightPlan')
        if terminal_data:
            insert_flight(new_dict)
        else:
            other = new_dict.get('ns2:asdexMsg')
            if other:
                surface_data = new_dict['ns2:asdexMsg'].get('xmlns:ns2')
                if surface_data:
                    if new_dict['ns2:asdexMsg']['xmlns:ns2'] == "urn:us:gov:dot:faa:atm:terminal:entities:v4-0:smes:surfacemovementevent":
                        insert_ground(new_dict)
        f.close()
        os.remove(file_path)

    except IOError:
        pass
