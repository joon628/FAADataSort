import ast
import os
from datetime import datetime
from insert import insert
def split_data(file_path, output_file):
    try:
        with open(file_path) as f:
            content = f.read()
            content = content.replace('true', 'True')
            content = content.replace('false', 'False')
            content = content.replace('null', 'None')
        
        new_dict = ast.literal_eval(content)
        terminal_data = new_dict.get('ns2:TATrackAndFlightPlan')
        if terminal_data:
            insert(new_dict)
        os.remove(file_path)

    except IOError:
        pass
