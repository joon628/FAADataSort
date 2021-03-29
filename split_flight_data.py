import ast
import os
from datetime import datetime

def split_data(file_path, output_file):
    try:
        with open(file_path) as f:
            content = f.read()
            content = content.replace('true', 'True')
            content = content.replace('false', 'False')
            content = content.replace('null', 'None')
        if content[2:4] == "ds":
            new_dict = ast.literal_eval(content)
            data_service = new_dict.get('ds:tfmDataService')
            if data_service:
                fltd_output = new_dict['ds:tfmDataService'].get('fltdOutput')
                if fltd_output:
                    acids = new_dict['ds:tfmDataService']['fltdOutput'].get('fdm:fltdMessage')
                    if acids:
                        for acid in acids:
                            track_data = acid.get("fdm:trackInformation")
                            if track_data:
                                exist = acid["fdm:trackInformation"].get("nxcm:ncsmRouteData")
                                if exist:
                                    traversal = acid["fdm:trackInformation"]['nxcm:ncsmRouteData'].get('nxcm:flightTraversalData2')
                                    if traversal:
                                        now = datetime.now()
                                        with open(f'{output_file}_{now}.txt', 'w') as data:
                                        #with open(os.path.join('sorted_data',f'{output_file}_{now}.txt'),'w') as data:
                                            data.write(str(acid))
        os.remove(file_path)

    except IOError:
        pass
