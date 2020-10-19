import pandas as pd
import numpy as np
import sys
import datetime
# from location import get_lat_lon, get_lat_lon_travel, zone
from pre_processing import pre_processing_criticality, pre_processing_vulnerability
from classification import Clustering_Vulnarebility, Clustering_Criticality
from flask import Response, jsonify
from file_plot import plot1
from collections import Counter
import random
import traceback
from map_database import mapping_database
import json
import requests
import json
from time import gmtime, strftime
from analysis import entry_point
from save_to_db import save_to_db


def mapping(string_1, string_2, string_3, string_4, string_5=5):
    df = mapping_database(string_1, string_2, string_3, string_4)
    df.to_csv("skskks.csv")
    df_k = df[["emp_id",
               "Prefrence",
               "emp_dep",
               "emp_sub_department",
               "Workplace_id",
               "Space",
               "Domain_Capacity",
               "Peak Load/Deliverable Milestone 1-10",
               "Peak Load/Deliverable Milestone 11-20",
               "Peak Load/Deliverable Milestone 20-EOM",
               "Workplacex",
               "Total_Space",
               "Total_Capcity",
               "Domain_Area",
               "type"]]
    df_k.loc[df_k.type == "org_admin", ['Workplace_id',
                                        'Workplacex']] = 'Org. Admin', 'Org. Admin'
    df.to_csv("more.csv")
    df1 = df[["emp_dep",
              "emp_sub_department",
              "Current Role",
              "emp_id",
              "org_id",
              "gender",
              "age",
              "pincode",
              "city",
              "state",
              "area_locality",
              "symptoms",
              "medical_history_detail",
              "travel_history",
              "travel_history_detail",
              "recently_interacted_with_positive",
              "covid_positive_vicintiy_home_meters",
              "covid_positive_vicintiy_work_meters",
              "Deliverable Milestone"]]
    df2 = df[['Is_Department_Core_Of_Buisness',
              'Employee Screening availaible',
              "Is_Critical_To_Core_Business",
              "Required for Saturatory/Regulatory",
              "Nature Of Interaction",
              "Requires Working in Close Proximity",
              "Requires Multiple Intraction with People",
              "Long Duration Of Interaction Required",
              "Expirience"]]
    return df, df1, df2, df_k


def start_pre_processing(df1, df2, df):
    data = pd.concat([df1, df2], axis=1)
    # [["Green Zone","Orange Zone","No Classification Zone","Red Zone","Containment Zone"][random.randint(0,4)] for i in range(data.shape[0]) ]#zones(data["Loction_Detail"].tolist())#[["Green Zone","Orange Zone","No Classification Zone","Red Zone","Containment Zone"][random.randint(0,4)] for i in range(data.shape[0]) ]#area_covid_zone
    data["zone"] = zone2(df['location'].tolist())

    # zones(data["Travel_Loction_Detail"].tolist())#[["Green Zone","Orange
    # Zone","No Classification Zone","Red Zone","Containment
    # Zone"][random.randint(0,4)]for i in range(data.shape[0])]#zone(data)
    data["travel_destination_zone"] = [["Green Zone"][0] for i in range(data.shape[0])]
    data.to_csv("heloo.csv")
    data.fillna(0, inplace=True)
    values = pre_processing_criticality(data)
    values_2 = pre_processing_vulnerability(data)
    values = pd.DataFrame(values)
    values.fillna(0, inplace=True)
    values_2 = pd.DataFrame(values_2)
    values_2.fillna(0, inplace=True)
    values_2 = values_2.apply(pd.to_numeric)
    values = values.apply(pd.to_numeric)
    return data, values, values_2


def post_processing(data, ploted):
    fraud = []
    for i in data["Cluster"]:
        if i == "crimson":
            fraud.append("Red")
        elif i in ["darkgreen"]:
            fraud.append("Green")
        else:
            fraud.append("Orange")
    data["Cluster"] = fraud
    xxv = []
    for i in ploted:
        if i == "crimson":
            xxv.append("Red")
        if i in ["palegreen", "Orange", "orange"]:
            xxv.append("Orange")
        if i == "darkgreen":
            xxv.append("Green")
        if i == "yellow":
            xxv.append("Orange")
        if i == 'lightpink':
            xxv.append("Orange")
        if i == 'wheat':
            xxv.append("Orange")

    vulnera_count = []
    for i in data["vulnerability_prediction"].tolist():
        if i == 0:
            vulnera_count.append("Green")
        if i == 1:
            vulnera_count.append("Orange")
        if i == 2:
            vulnera_count.append("Red")

    # ###print(vulnera_count)
    vulnera_count = dict(Counter(vulnera_count))
    vulnera_c = []
    for i in vulnera_count.keys():
        if i == "Green":
            t = {"color": i, "count": "Low : " + str(vulnera_count[i])}
        elif i == "Orange":
            t = {"color": i, "count": "Medium : " + str(vulnera_count[i])}
        elif i == "Red":
            t = {"color": i, "count": "High : " + str(vulnera_count[i])}
        else:
            t = {"color": "", "count": ""}
        vulnera_c.append(t)

    criti_count = []
    # print(type(vulnerability_count))
    for i in data["criticality_prediction"].tolist():
        if i == 1:
            criti_count.append("Orange")
        if i == 2:
            criti_count.append("Green")
        if i == 0:
            criti_count.append("Red")
    criti_count = dict(Counter(criti_count))
    criticality_c = []
    for i in criti_count.keys():
        t = {"color": i, "count": criti_count}
        criticality_c.append(t)

    criti_c = []
    # for i in criti_count.keys():
    #     t = {"color":i,"count":criti_count[i]}
    #     criti_c.append(t)
    for i in criti_count.keys():
        if i == "Green":
            t = {"color": i, "count": "High : " + str(criti_count[i])}
        elif i == "Orange":
            t = {"color": i, "count": "Medium : " + str(criti_count[i])}
        elif i == 'Red':
            t = {"color": i, "count": "Low : " + str(criti_count[i])}
        else:
            t = ""
        criti_c.append(t)

    total_count2 = []
    total_count = dict(Counter(xxv))
    total_count = [{"color": "Green",
                    "count": "Low : " + str(total_count.get("Green","0"))},
                   {"color": "Orange",
                    "count": "Medium : " + str(total_count.get("Orange","0"))},
                   {"color": "Red",
                    "count": "High : " + str(total_count.get("Red","0"))}]
    values2 = {
        "total_count": total_count,
        "vulnerability_count": vulnera_c,
        "criticality_count": criti_c}
    return values2


def Cluster_result(
        data,
        df_k,
        clustering_vulnerability,
        clustering_criticality,
        string_1,
        string_2,
        string_3,
        string_4,
        string_5=5):
    data["type"] = df_k["type"]
    data["vulnerability_prediction"] = clustering_vulnerability
    data["criticality_prediction"] = clustering_criticality
    data.loc[data.type == "org_admin", ['criticality_prediction']] = 2
    data.loc[data.type == "fun_admin", ['criticality_prediction']] = 2
    vulnerability_count = Counter(data["vulnerability_prediction"].to_list())
    criticality_count = Counter(data["criticality_prediction"].to_list())
    vulnerability_count = dict_changing(dict(vulnerability_count))
    criticality_count = dict_changing(dict(criticality_count))
    data["vulnerability_level"] = data["vulnerability_prediction"].apply(
        vulnerability_category)
    data["criticality_level"] = data["criticality_prediction"].apply(
        criticality_category)
    data["Workplace_id"] = df_k["Workplace_id"]
    data["emp_id"] = df_k["emp_id"]
    data = data[data["Workplace_id"] ==
                string_1] if string_1 != 'All' else data
    data = data[data["emp_dep"] == string_2] if string_2 != "All" else data
    data = data[data["emp_sub_department"] ==
                string_3] if string_3 != "All" else data
    return data


def zone2(list_values_lat_lon):
    final = []
    #"http://15.206.203.123/api/workdetails-report"
    url = "https://back.kriyakonsulting.com/index.php/api/getDetailsCovidReport"
    headers = {
        'key': "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJtYWlsSWRlbnRpdHkiOiJzYW5kZXBwLmdhdGVAZ21haWwuY29tIn0.Z8uE7l-Yhr77PkNEW75wVoGJ-mcsK_0Xmy7QuX5R2f0",
        'cache-control': "no-cache",
        'postman-token': "42f624f6-5a05-a551-51b8-4305a20e29c5"}
    for si in list_values_lat_lon:
        i = ",".join(si)
        print(i)
        myDictObj = {"latlong": [i]}
        serialized = json.dumps(myDictObj, sort_keys=True, indent=3)
        response = requests.request(
            "POST", url, data=serialized, headers=headers)
        val = json.loads(response.text)
        xv = val["data"]
        if xv:
            val2 = val["data"][0]
            print(val2, type(val2))
            if val2["inContainmentZone"] in ["true", True, 1, "1"]:

                final.append(6)
            else:
                final.append(2)
        else:
            final.append(2)
    return final


def get_function_name(id_s, id_x, id_y):
    try:
        url = "https://back.kriyakonsulting.com/index.php/api/getFunctionSubfuntionNamereport"

        payload = "{\r\n    \"fun_id\": \"268811\",\r\n    \"subfun_id\":\"268813\"\r\n}"
        headers = {
            'content-type': "application/json",
            'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.InJlc2V0MjAyMEAxNTkwNzYxMTQzIg.vhHChN3H8UM--EqP0C_1JmGWdf2ciLa-AXYBO9yZuVg",
            'cache-control': "no-cache",
            'postman-token': "5a642e7b-9e44-56de-96d2-d376650d71c8"}
        response = requests.request("POST", url, data=payload, headers=headers)
        myDictObj = {"workplace_id": id_s, "fun_id": id_x, "subfun_id": id_y}
        serialized = json.dumps(myDictObj, sort_keys=True, indent=3)
        response = requests.request(
            "POST", url, data=serialized, headers=headers)
        mv = json.loads(response.text)["data"]
        return mv["workplace_name"], mv["function_name"], mv["subfunction_name"]
    except Exception as e:
        print(id_s,id_x,id_y)
        # sys.exit(0)
        return id_s, id_x, id_y


def dict_changing(dict1):
    dict_final = {}
    for i in dict1.keys():
        if i == 0:
            dict_final["Green"] = dict1.get(0)
        if i == 1:
            dict_final["Orange"] = dict1.get(1)
        if i == 2:
            dict_final["Red"] = dict1.get(2)

    if dict_final.get("Red") is None:
        dict_final["Red"] = "0"
    if dict_final.get("Green") is None:
        dict_final["Green"] = 0
    if dict_final.get("Orange") is None:
        dict_final["Orange"] = 0

    return dict_final


def vulnerability_category(t):
    if t == 0:
        return "Low Vulnerability"
    if t == 1:
        return "Medium Vulnerability"
    if t == 2:
        return "High Vulnerability"


def criticality_category(t):
    if t == 0:
        return "Low Criticality"
    if t == 1:
        return "Medium Criticality"
    if t == 2:
        return "High Criticality"


def start(string_1, string_2, string_3, string_4, string_5=5):
    try:
        print(type(string_1),"ksddkkdkdkkd")
        string_1 = eval(string_1)
        print(type(string_1),"ksddkkdkdkkd")
        # print(string_1["wp_id"],"fdksnfldsnfldksnflk")
        print(type(string_1),string_1)
        # print(string_1,type(string_1["wp_id"][0]))

        wp_list  = [iik["wp_id"] for iik in string_1]
        wp_list.append(None)
        df_list = []
        df1_list = []
        df2_list = []
        df_k_list = []

        for sv in wp_list:
            try:

                print(sv)
                df_val, df1_val, df2_val, df_k_val = mapping(
                    sv, string_2, string_3, string_4, string_5=5)

                df_list.append(df_val)
                df1_list.append(df1_val)
                df2_list.append(df2_val)
                df_k_list.append(df_k_val)
            except Exception as e:
                pass
        print(df_list)
        df = pd.concat(df_list)
        df1 = pd.concat(df1_list)
        df2 = pd.concat(df2_list)
        df_k = pd.concat(df_k_list)
        string_1 = "All"
        string_2 = "All"
        string_3 = "All"
        string_5 = "5"



        data, values, values_2 = start_pre_processing(df1, df2, df)
        clustering_vulnerability = Clustering_Vulnarebility(values_2)
        clustering_criticality = Clustering_Criticality(values)
        data = Cluster_result(
            data,
            df_k,
            clustering_vulnerability,
            clustering_criticality,
            string_1,
            string_2,
            string_3,
            string_4,
            string_5=5)
        ploted, scatter_plot_response, data = plot1(data)
        values2 = post_processing(data, ploted)
        values2["optionScatter"] = scatter_plot_response
        df_k = pd.merge(df_k, data[["emp_id", "Cluster", "vulnerability_level",
                                    "criticality_level"]], on="emp_id")
        df_k.to_csv("hellohellp.csv")
        df_k.rename(
            columns={
                "emp_dep": "Function",
                "emp_sub_department": "Sub-Function",
                "Workplace_id": "WorkPlace"},
            inplace=True)
        df_k = df_k.applymap(str)
        df_k.to_csv("df.csv")   
        bar_plot = entry_point(
            df_k,
            string_1,
            string_2,
            string_3,
            string_4,
            string_5)
        values2["bar_plot"] = bar_plot
        dfx = df_k
        ff = [
            "Peak Load/Deliverable Milestone 1-10",
            "Peak Load/Deliverable Milestone 11-20",
            "Peak Load/Deliverable Milestone 20-EOM"]
        today_ = datetime.datetime.today().day
        get_today_range = int(today_ / 10) if int(today_ / 10) < 3 else 2
        useful = ff[get_today_range]
        dfx["PeakLoad_Relevance"] = dfx[useful]
        dfx = dfx[["WorkPlace",
                   "Function",
                   "Sub-Function",
                   "emp_id",
                   "Cluster",
                   "Prefrence",
                   "PeakLoad_Relevance",
                   "vulnerability_level",
                   "criticality_level"]]
        dfx = dfx[dfx["WorkPlace"] == string_1] if string_1 != "All" else dfx
        dfx = dfx[dfx["Function"] == string_2] if string_2 != "All" else dfx
        dfx = dfx[dfx["Sub-Function"] ==
                  string_3] if string_3 != "All" else dfx
        func_name = []
        sub_func_name = []
        wp_name = []
        dfx.to_csv("final2.csv")
        save_to_db(dfx, string_4)
        print("done")
        # sys.exit(0)s
        for k, i in dfx.iterrows():
            c, a, b = get_function_name(
                i["WorkPlace"], i["Function"], i["Sub-Function"])
            func_name.append(a)
            sub_func_name.append(b)
            wp_name.append(c)
        dfx["WorkPlace"] = wp_name
        dfx["Function"] = func_name
        dfx["Sub_Function"] = sub_func_name
        dfx.rename(columns={"Workplacex": "WorkPlace"})
        

        qt = dfx[dfx["Sub-Function"] ==
                 string_3].shape[0] if string_3 != "All" else dfx.shape[0]
        if qt > 0:
            dfx['json'] = dfx.apply(lambda x: x.to_dict(), axis=1)
            values2["employee"] = dfx['json'].tolist()
            values2["time"] = strftime("%Y-%m-%d %H:%M:%S", gmtime())

        else:
            values2 = {"total_count": [{"color": "Green", "count": 0}, {"color": "Red", "count": 0}, {"color": "Orange", "count": 0}], "vulnerability_count": [{"color": "Green", "count": 0}, {"color": "Red", "count": 0}, {"color": "Orange", "count": 0}], "criticality_count": [{"color": "Green", "count": 0}, {"color": "Red", "count": 0}, {
                "color": "Orange", "count": 0}]}  # {"total_count" : [{"color":"Green","count":0},{"color":"Red","count":0,{"color":"Orange","count":0}}],"vulnerability_count":[{"color":"Green","count":0},{"color":"Red","count":0,{"color":"Orange","count":0}}],"criticality_count":[{"color":"Green","count":0},{"color":"Red","count":0,{"color":"Orange","count":0}}]}
            values2["bar_plot"] = [
                {
                    "y": 0, "label": "Total Employee", "color": "#623882"}, {
                    "y": 0, "label": "Safe For Office", "color": "#009B74"}, {
                    "y": 0, "label": "Post Spatial Constraints", "color": "#2F5597"}, {
                    "y": 0, "label": "Post PeakLoad Constraints", "color": "#8FAADC"}, {
                        "y": 0, "label": "Post Prefrence Constraints", "color": "#595959"}]  # {"graph1":{"Total Employee":0,"Safe For Office":0,"Post Spatial Constraints":0,"Post PeakLoad Constraints":0,"Post Prefrence Constraints":0}}
            values2["optionScatter"] = [
                {"x": 0, "y": 0, "emp_id": "", "label": "   ", "color": "White"}]
            values2["employee"] = [
                {"Workplace": " ", "emp_id": "", "Function": "", "Sub_Function": ""}]
        print(values2)
        # save_to_db(dfx,string_4)
        return jsonify(values2)
    except Exception as e:
        print("Exception: {}".format(type(e).__name__))
        print("Exception message: {}".format(e))
        return jsonify({"status": "101"})


if __name__ == "__main__":

    start(str({"wp_id":[{"wp_id":"154"}]}),"All","All",6890)
