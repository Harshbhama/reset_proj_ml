import pandas as pd 
import sys
import os
import pgeocode
import tqdm
import requests
from ast import literal_eval
 
def get_lat_lon(data):
	noim = pgeocode.Nominatim('IN')
	lat_lon = []
	for k,j in data.iterrows():
		# printj.pincode)
		xv = noim.query_postal_code(str(int(j.pincode)))
		lat_lon.append([xv.latitude,xv.longitude])


	return lat_lon
def get_lat_lon_travel(data):
	# noim = pgeocode.Nominatim('IN')
	df = pd.read_csv("./data/lat_lon.csv")
	zone  = []

	for i,k in data.iterrows():
		print(k.travel_history == "Yes")
		if k.travel_history == "Yes":
			# sys.exit(0)
			print(k.travel_history_detail)
			travel_area_zone = k.travel_history_detail
			print(travel_area_zone)
			values  = df[df["officename"]==travel_area_zone]
			# print(travel_area_zone,"################")
			values = values.iloc[0].lat_lon
			if len(values):
				zone.append(values)
			else:
				zone.append("[25.2459, 73.61168823529411]")
		else:
			zone.append("XXX")
	return zone

 

def zone(data):
	area_zone = []
	travel_area_zone = []

	for i,k in data.iterrows():
		# print(type(k.lat_lon))
		lat_lon1 = eval(str(k.lat_lon))
		lat_lon1 = str(lat_lon1)

		string = 'https://api.smartmarket.ai/api/v1/covid/assessRisk/?geom_type=point&name='+lat_lon1+'&api_key=45XHWQX-6Q5MRX0-KMGVJ6X-TG5V0B2'
		result1 =  requests.get(string)
		out  = result1.json()[0]
		area_zone.append(out["covidriskzonename"])
		print(k.travel_history,k.lat_lon_travel)
		if k.travel_history == "Yes":
			lat_lon_2 = eval(str(k.lat_lon_travel)) 
			lat_lon_2 = str(lat_lon_2)
			string2 = 'https://api.smartmarket.ai/api/v1/covid/assessRisk/?geom_type=point&name='+lat_lon_2+'&api_key=45XHWQX-6Q5MRX0-KMGVJ6X-TG5V0B2'

			result2 = requests.get(string2)
			out2    = result2.json()[0]
			travel_area_zone.append(out2["covidriskzonename"])
		else:
			travel_area_zone.append("XXX")
	return area_zone,travel_area_zone
