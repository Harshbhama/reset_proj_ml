#import mpld3
import datetime
import numpy as np
import matplotlib.pyplot as plt
import base64
from io import BytesIO
import pandas as pd
import numpy as np
import collections
import matplotlib.pyplot as plt
from constraints import area_wise
import math
import sys
import time
import json
import requests
def area_api(filter_1,filter_2,filter_3,filter_4):
    url = "https://back.kriyakonsulting.com/index.php/api/getSpaceDetailsReport"

    myDictObj = { "org_id":filter_4,"workplace":filter_1,"department":filter_2,"sub_department":filter_3}
    print(filter_1,filter_2,filter_3,filter_4)
    serialized= json.dumps(myDictObj, sort_keys=True, indent=3)
#     payload = "{\n\"org_id\":\"7421\",\n\"workplace\":\"All\",\n\"department\":\"All\",\n\"sub_department\":\"All\"\n}"
    headers = {
    'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.InJlc2V0MjAyMEAxNTkwNzczMDQzIg.XZ-05OIGu-I1Xa8B3_cRtRfK0losg3w4Kybqc2Cfa8g",
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "9a9aa8c3-43db-21b4-8512-28f909ad2c41"
    }

    response = requests.request("POST", url, data=serialized, headers=headers)

    # print(response.text)
    df = pd.DataFrame(json.loads(response.text)["data"])
    return df
def upper_fucnt(p):
    p = p
    print(p)
    list_1 = ["#623882","#009B74","#2F5597","#8FAADC","#595959"]
    # list_1 = ["blue","green","orange","yellow","red"]
    k = []
    t = {"y":p[0],"label":"Total Employee","color":list_1[0]}
    q = {"y":p[1],"label":"Safe For Office","color":list_1[1]}
    r = {"y":p[-1],"label":"Post Spatial Constraints","color":list_1[2]}
    s = {"y":p[2],"label":"Post PeakLoad Constraints","color":list_1[3]}
    m = {"y":p[3],"label":"Post Prefrence Constraints","color":list_1[4]}

    l = {"y":0,"label":"   "}
    print([t,q,r,s,m,l])
    return [t,q,r,s,m,l]

def space3(df,filter_4,filter_5):

	filter_2_cluster = df 
	all_green_ = df.shape[0]

	if all_green_==0:
		return 0
	df_2 = area_api("All","All","All",filter_4)
	print(df_2)
	sum_list = []
	for i,k in df_2.iterrows():
		area_1 = k["spatial_details"]
		if k['space_allocated'] == "SQ FT":
			pass
		else:
			area1 = area_1 * 10.764

		total_capacity = k["total_capcity"]
		print(filter_5)
		safe_radius = float(filter_5)
		safe_area         = math.pi*safe_radius**2
		total_accomodation = math.ceil(float(area_1)/float(safe_area))
		if float(total_accomodation) >= float(total_capacity):
			sum_list.append(float(total_capacity))
		else:
			sum_list.append(float(total_accomodation))

	return int(sum(sum_list))

def space4(df,filter_1,filter_2,filter_3,filter_4,filter_5):
    print(filter_1,filter_2,filter_3,filter_4,filter_5)
    filter_2_cluster = df
    all_green_ = df.shape[0]

    if all_green_==0:
        return 0
    df_2 = area_api(filter_1,"All","All",filter_4)
    print(df_2)
    sum_list = []
    for i,k in df_2.iterrows():
        area_1 = k["function_spatial_value"]
        if k['function_spatialunit'] == "SQ FT":
            pass
        else:
            area1 = area_1 * 10.764

        total_capacity = k["function_headcount"]
        safe_radius = float(filter_5)
        safe_area         = math.pi*safe_radius**2

        total_accomodation = math.ceil(float(area_1)/float(safe_area))
        if float(total_accomodation) >= float(total_capacity):
            sum_list.append(float(total_capacity))
        else:
            sum_list.append(float(total_accomodation))
    print(sum_list,sum(sum_list))
    # sys.exit(0)
    return int(sum(sum_list))


def space6(df,filter_1,filter_2,filter_3,filter_4,filter_5):
    print(filter_1,filter_2,filter_3,filter_4,filter_5)
    filter_2_cluster = df
    all_green_ = df.shape[0]

    if all_green_==0:
        return 0
    df_2 = area_api(filter_1,filter_2,filter_3,filter_4)
    print(df_2)
    sum_list = []
    for i,k in df_2.iterrows():
        area_1 = k["space_allocated_sub"]
        if k['space_allocated_sub_sqft'] == "SQ FT":
            pass
        else:
            area1 = area_1 * 10.764

        total_capacity = k["sub_function_capcity"]
        safe_radius = float(filter_5)
        safe_area         = math.pi*safe_radius**2
        print(safe_area)
        # sys.exit(0)
        total_accomodation = math.ceil(float(area_1)/float(safe_area))
        if float(total_accomodation) >= float(total_capacity):
            sum_list.append(float(total_capacity))
        else:
            sum_list.append(float(total_accomodation))
    print(sum_list)
    return int(sum(sum_list))
def space7(df,filter_1,filter_2,filter_3,filter_4,filter_5):
    print(filter_1,filter_2,filter_3,filter_4,filter_5)
    filter_2_cluster = 3
    all_green_ = 3

    if all_green_==0:
        return 0
    df_2 = area_api(filter_1,filter_2,filter_3,filter_4)
    print(df_2)
    sum_list = []
    for i,k in df_2.iterrows():
        area_1 = k["space_allocated_sub"]
        if k['space_allocated_sub_sqft'] == "SQ FT":
            pass
        else:
            area1 = area_1 * 10.764

        total_capacity = k["sub_function_capcity"]
        safe_radius = float(filter_5)
        safe_area         = math.pi*safe_radius**2
        total_accomodation = math.ceil(float(area_1)/float(safe_area))
        if float(total_accomodation) >= float(total_capacity):
            sum_list.append(float(total_capacity))
        else:
            sum_list.append(float(total_accomodation))
    print(sum_list)
    return int(sum(sum_list))
def prefrence2(df):
    all_green_=df#df[df["Cluster"]=="Green"]
    
    all_safe_ = all_green_.shape[0]
    all_green_ = all_green_[all_green_["Prefrence"]=="Office"].shape[0]
    return all_safe_,all_green_
def peak_load2(df):
    ff = ["Peak Load/Deliverable Milestone 1-10","Peak Load/Deliverable Milestone 11-20","Peak Load/Deliverable Milestone 20-EOM"]
    today_ = datetime.datetime.today().day
    get_today_range = int(today_/10) if  int(today_/10)<3 else 2
    useful = ff[get_today_range]
        
        # print(useful,"############" )
    all_green_=df #df[df["Cluster"]=="Green"]
    all_safe_ = all_green_.shape[0]
        # print(all_green_["Cluster"])
    all_green_ = all_green_[all_green_[useful]=="Yes"].shape[0]

    return all_safe_,all_green_
def All_All_All(df,filter_1,filter_2,filter_3,filter_4,filter_5):
    total_employee = df.shape[0]
    safe_for_office = df[df["Cluster"]=="Green"].shape[0]
    peak_load_all_safe,peak_load_values = peak_load2(df)
    f_,preference_values = prefrence2(df)
    space_values = space3(df,filter_4,filter_5)

    return total_employee,safe_for_office,peak_load_values,preference_values,space_values
def All_All_sub(df,filter_sub,filter_5):
    post_filter = df[df["Sub-Function"]==filter_sub]
    total_employee = post_filter.shape[0]
    safe_for_office = post_filter[post_filter["Cluster"]=="Green"].shape[0]
    peak_load_all_safe , peak_load_values = peak_load2(post_filter)
    f_,preference_values = prefrence2(post_filter)
    space_values     = space2(post_filter,filter_5)
    return total_employee,safe_for_office,peak_load_values,preference_values,space_values
def All_fun_all(df,filter_f,filter_5):
    post_filter = df[df["Function"]==filter_f]
    total_employee = post_filter.shape[0]
    safe_for_office = post_filter[post_filter["Cluster"]=="Green"].shape[0]
    peak_load_all_safe , peak_load_values = peak_load2(post_filter)
    f_,preference_values = prefrence2(post_filter)
    space_values     = space2(post_filter,filter_5)
    return total_employee,safe_for_office,peak_load_values,preference_values,space_values
def All_fun_fun(df,filter_1,filter_2,filter_5):
    post_filter_1 = df[df["Function"]==filter_1]
    post_filter_2 = df[df["Sub-Function"]==filter_2]
    total_employee = post_filter_2.shape[0]
    safe_for_office = post_filter_2[post_filter_2["Cluster"]=="Green"].shape[0]
    peak_load_values,peak_load_values = peak_load2(post_filter_2)
    f_,preference_values = prefrence2(post_filter_2)
    print(post_filter_2)
    space_values     = space2(post_filter_2,filter_5)
    return total_employee,safe_for_office,peak_load_values,preference_values,space_values
def Fun_All_All(df,filter_1,filter_2,filter_3,filter_4,filter_5):
    post_filter = df[df["WorkPlace"]==filter_1]
    total_employee = post_filter.shape[0]
    safe_for_office = post_filter[post_filter["Cluster"]=="Green"].shape[0]
    f_,peak_load_values = peak_load2(post_filter)
    f_,preference_values = prefrence2(post_filter)
    space_values     = space4(post_filter,filter_1,filter_2,filter_3,filter_4,filter_5)
    return total_employee,safe_for_office,peak_load_values,preference_values,space_values
def Fun_All_Fun(df,filter_1,filter_2,filter_3,filter_4,filter_5):
    post_filter = df[df["WorkPlace"]==filter_1]
    post_filter_2 = post_filter[post_filter["Sub-Function"]==filter_2]
    total_employee = post_filter_2.shape[0]
    safe_for_office = post_filter_2[post_filter_2["Cluster"]=="Green"].shape[0]
    f_,peak_load_values = peak_load2(post_filter_2)
    f_,preference_values = prefrence2(post_filter_2)
    space_values     = space2(post_filter_2,filter_5)
    return total_employee,safe_for_office,peak_load_values,preference_values,space_values
def Fun_Fun_All(df,filter_1,filter_2,filter_3,filter_4,filter_5):
    post_filter = df[df["WorkPlace"]==filter_1]
    post_filter_2 = post_filter[post_filter["Function"]==filter_2]
    total_employee = post_filter_2.shape[0]
    safe_for_office = post_filter_2[post_filter_2["Cluster"]=="Green"].shape[0]
    f_,peak_load_values = peak_load2(post_filter_2)
    f_,preference_values = prefrence2(post_filter_2)
    space_values     = space6(post_filter_2,filter_1,filter_2,filter_3,filter_4,filter_5)
    return total_employee,safe_for_office,peak_load_values,preference_values,space_values
def Fun_Fun_Fun(df,filter_1,filter_2,filter_3,filter_4,filter_5):
    post_filter = df[df["WorkPlace"]==filter_1]
    post_filter = post_filter[post_filter["Function"]==filter_2]
    total_employee = post_filter.shape[0]
    post_filter = post_filter[post_filter["Sub-Function"]==filter_3]
    safe_for_office = post_filter[post_filter["Cluster"]=="Green"].shape[0]
    f_,peak_load_values = peak_load2(post_filter)
    f_,preference_values = prefrence2(post_filter)
    space_values     = space7(post_filter,filter_1,filter_2,filter_3,filter_4,filter_5)
    return total_employee,safe_for_office,peak_load_values,preference_values,space_values
def entry_point(df,filter_1,filter_2,filter_3,filter_4,filter_5):
    if filter_1=="All" and filter_2 == "All" and filter_3 == "All":
        return upper_fucnt(All_All_All(df,filter_1,filter_2,filter_3,filter_4,filter_5))
    if filter_1=="All" and filter_2 == "All" and filter_3 != "All": #invalid
        return upper_fucnt(All_All_sub(df,filter_1,filter_2,filter_3,filter_4,filter_5))
    if filter_1=="All" and filter_2 != "All" and filter_3 == "All":
        return upper_fucnt(All_fun_all(df,filter_1,filter_2,filter_3,filter_4,filter_5))
    if filter_1=="All" and filter_2 != "All" and filter_3 != "All":
        print("dkdkdkdk")
        return upper_fucnt(All_fun_fun(df,filter_1,filter_2,filter_3,filter_4,filter_5))
    if filter_1!="All" and filter_2 == "All" and filter_3 == "All":
        return upper_fucnt(Fun_All_All(df,filter_1,filter_2,filter_3,filter_4,filter_5))
    if filter_1!="All" and filter_2 == "All" and filter_3 != "All":
        return upper_fucnt(Fun_All_Fun(df,filter_1,filter_2,filter_3,filter_4,filter_5))
    if filter_1!="All" and filter_2 != "All" and filter_3 == "All":
        return upper_fucnt(Fun_Fun_All(df,filter_1,filter_2,filter_3,filter_4,filter_5))
    if filter_1!="All" and filter_2 != "All" and filter_3 != "All":
        return upper_fucnt(Fun_Fun_Fun(df,filter_1,filter_2,filter_3,filter_4,filter_5))







