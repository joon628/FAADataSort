

division = {}
def histogram(data):
    if data['ns2:TATrackAndFlightPlan']['xmlns:ns2'] == "urn:us:gov:dot:faa:atm:terminal:entities:v4-0:tais:terminalautomationinformation":
        temp = data['ns2:TATrackAndFlightPlan']['record']
        for i in temp:
            if i['track']['acAddress'] not in division:
                division[i['track']['acAddress']] = {"time":i['track']['mrtTime'],"long":i['track']['lon'],"lat":i['track']['lat'],"alt":i['track']['reportedAltitude']}
            else:
                division.append({"time":i['track']['mrtTime'],"long":i['track']['lon'],"lat":i['track']['lon'],"alt":i['track']['reportedAltitude']})

histogram(data)
print(division)
