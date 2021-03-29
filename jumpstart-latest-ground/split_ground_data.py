import ast
import os
from datetime import datetime
from insert import insert
import json

def split_data(file_path):
    if os.path.exists("./log/messages.log"):
        os.remove("./log/messages.log")
        return
    try:
        with open(file_path) as f:
            content = f.read()

        print("hey",content)
        #new_dict = ast.literal_eval(content)
        new_dict = json.loads(content)
        terminal_data = new_dict.get('ns2:TATrackAndFlightPlan')
        if terminal_data:
            insert(new_dict)
        f.close()
        os.remove(file_path)

    except IOError:
        pass
