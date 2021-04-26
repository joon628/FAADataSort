import pymysql

def connect(host, user, password):
    conn = pymysql.connect(host=host, user=user, password=password, db='mysql', charset='utf8')
    curs = conn.cursor()
    return conn, curs

def insert_flight(data):
    conn, curs = connect("127.0.0.1", "root", '')
    temp = data['ns2:TATrackAndFlightPlan']['record']
    for i in temp:
        if type(i) != type("string"):
            if i.get('track'):
                if i['track'].get('mrtTime'):
                    time = i['track']['mrtTime']
                else:
                    time = None

                if i['track'].get('acAddress'):
                    acAddress = i['track']['acAddress']
                else:
                    acAddress = None

                if i['track'].get('lon'):
                    lon = i['track']['lon']
                else:
                    lon = 0

                if i['track'].get('lat'):
                    lat = i['track']['lat']
                else:
                    lat = 0

                if i['track'].get('reportedAltitude'):
                    reportedAltitude = i['track']['reportedAltitude']
                else:
                    reportedAltitude = 1000000001

                sql = f"INSERT INTO ground_data.generic (time,acAddress,lon,lat,alt) values {time,acAddress,lon,lat,reportedAltitude}"
                curs.execute(sql)
                conn.commit()

def insert_ground(data):
    conn, curs = connect("127.0.0.1", "root", '')
    temp = data['ns2:asdexMsg']['mlatReport']
    full = temp['full']

    if type(temp) != type("string"):
        if temp.get('report'):
            if temp['report'].get('basicReport'):
                basic_report = temp['report']['basicReport']
                if basic_report.get('time'):
                    time = basic_report['time']
                else:
                    time = None
                if basic_report.get('position'):
                    if basic_report['position'].get('lon'):
                        lon = basic_report['position']['lon']
                    else:
                        lon = 0
                    if basic_report['position'].get('lat'):
                        lon = basic_report['position']['lat']
                    else:
                        lon = 0
                if basic_report.get('track'):
                    track = basic_report['track']
                else:
                    track = 0
            if full == 'true':
                acAddress = temp['report']['acAddress']
            else:
                acAddress = None
            sql = f"INSERT INTO ground_data.ground (time,acAddress,track,lon,lat) values {time,acAddress,track,lon,lat}"
            curs.execute(sql)
            conn.commit()
