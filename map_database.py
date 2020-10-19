#!/usr/bin/env python
# coding: utf-8

# In[3]:
import sys
import random
import json
import requests
import pandas as pd
import re
from ast import literal_eval
import requests
#"http://15.206.203.123/api/workdetails-report"
def mapping_database(id_1,id_2,id_3,id_4):
    def self_conversion(df_s):
        if df_s == "self":
            return 0
        if df_s == "org_admin":
            return 6
        if df_s=="fun_admin":
            return 4
    def api_functionality(id_1,id_2,id_3,id_4):
    	#"https://back.kriyakonsulting.com/index.php/api/workdetails-report"
        url = "https://back.kriyakonsulting.com/index.php/api/workdetails-report"
        myDictObj = { "org_id":id_4}
        ##convert object to json
        serialized= json.dumps(myDictObj, sort_keys=True, indent=3)
        print(serialized)
        # ll = ll ="{{\n\t\"org_id\":\"{}\"\n}}".format(id)
        payload = "{\n\t\"org_id\":\"5785\"\n}"

        headers = {
            'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InJlc2V0QHJlc2V0LmNvbTE1OTI2Mzg1ODAifQ.Ll1XE8QZsPuzRCOn4vE1gd6Da8HmpY6VIbGGYfT1U10",
            'content-type': "application/json",
            'cache-control': "no-cache",
            'postman-token': "9ec69946-ec75-4bce-51d9-2a515f5f630b"
            }

        response = requests.request("POST", url, data=serialized, headers=headers)
        k = json.loads(response.text)
        #print(pd.DataFrame(k))
        df  = pd.DataFrame(k["data"])
        function_Details = function_Details = {"spatial_details":"Space","total_capcity":"Total Capacity","workplace_name":"Workplace"}
        df = df.rename(columns=function_Details)
        df["Function"]=df["dep_details"].apply(lambda x: json.loads(x)[0]["subfunction"] if len(json.loads(x)) else "")
	#df["Function"]=df["dep_details"].apply(lambda x: json.loads(x)[0]["subfunction"])
        df["Space"] = df["Space"].replace(to_replace ='[A-Za-z ]', value = '', regex = True) 
        
        return df
    def Data_Report(id_1,id_2,id_3,id_4):

        myDictObj = { "org_id":id_4, "workplace":id_1, "department":"All", "sub_department":"All" }
        ##convert object to json
        serialized= json.dumps(myDictObj, sort_keys=True, indent=3)
        
        url = "https://back.kriyakonsulting.com/index.php/api/getEmployeeDatareport"

        # payload  = "{\n\"org_id\":\"5785\",\n\"workplace\":\"59\",\n\"department\":\"All\",\n\"sub_department\":\"All\"\n}"#"{\n\"org_id\":\"5785\",\n\"workplace\":\"59\",\n\"department\":\"268774\",\n\"sub_department\":\"268774\"\n}"
        headers = {
            'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InJlc2V0QHJlc2V0LmNvbTE1OTI2Mzg1ODAifQ.Ll1XE8QZsPuzRCOn4vE1gd6Da8HmpY6VIbGGYfT1U10",
            'content-type': "application/json",
            'cache-control': "no-cache",
            'postman-token': "4f156b1a-66d4-3666-e80c-df9301c83d01"
            }

        response = requests.request("POST", url, data=serialized, headers=headers)
        print(response.text)
        xv= {"work_exp":"Expirience","role":"Current_Role","milestone":"Deliverable Milestone","peak_load_month":"Peak Load/Deliverable Milestone 1-10",
            "emp_activity_11":"Peak Load/Deliverable Milestone 11-20","emp_activity_21":"Peak Load/Deliverable Milestone 20-EOM"}
    #     #print(xv)
        # #print(json.loads(response.text))
        df = pd.DataFrame(json.loads(response.text)["data"])
        df = df.rename(columns = xv)
        return df
    import requests
    def functional_data(id1,id2,id_3,id_4):
        
        url = "https://back.kriyakonsulting.com/index.php/api/functiondetails-report"

        myDictObj = { "org_id":id_4, "workplace":id1, "department":"All", "sub_department":"All" }
        ##convert object to json
        serialized= json.dumps(myDictObj, sort_keys=True, indent=3)
        headers = {
            'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InJlc2V0QHJlc2V0LmNvbTE1OTI2Mzg1ODAifQ.Ll1XE8QZsPuzRCOn4vE1gd6Da8HmpY6VIbGGYfT1U10",
            'content-type': "application/json",
            'cache-control': "no-cache",
            'postman-token': "969f0502-42cd-fd92-a5e0-b0c6f8ab2176"
            }

        response = requests.request("POST", url, data=serialized, headers=headers)
        k = {"department":"Function",
             "is_the_function":"Is_Department_Core_Of_Buisness",
             'delivering_outputs': 'Required for Saturatory/Regulatory',
             'space_allocated':'Space_function',
             'total_capacity' : 'Capacity_Function',
             'sub_function':"Sub-Function",
             'nature_of_interaction':"Nature Of Interaction",
             'close_proximity_required':'Requires Working in Close Proximity',
             'many_interactions_required':'Requires Multiple Intraction with People',
             'sub_function_capcity'  : "Domain Capacity",
             'space_allocated_sub': "Domain_Area"
         }
        df = pd.DataFrame(json.loads(response.text)["data"])
        # #print(df.columns)
        df = df.rename(columns = k)
        df['Is_Critical_To_Core_Business'] = df['extremely_critical'].tolist()
        df['Employee Screening availaible'] = df['screening_points'].tolist()
        df['Long Duration Of Interaction Required'] = df["long_durations_required"].tolist()
        df["Space_function"] = df["Space_function"].replace(to_replace ='[A-Za-z ]', value = '', regex = True) 
    #     #print(df.columns)
        
        return df
    def covid_positive_vicintiy_home_meters(string):
        string =str(string)
        #print(type(string),"s"+string)
        if type(string) is not str:
            return 0 
        string = re.findall(r'\d+(?:\.\d+)?',str(string),flags=re.I)[0] if len(re.findall(r'\d+(?:\.\d+)?',str(string),flags=re.I))>0 else 0
        # #print(string)
        # #print(type(string))
        if str(int(float(string))) in ["10",'10000']:
            return 1
        elif  str(int(float(string))) in ["5","5000"]:
            return 2
        elif str(int(float(string))) in ["2000","2"]:
            return 4
        elif str(int(float(string)))in ["1","1000"]:
            return 5
        elif str(int(float(string))) in ["500","0.5"]:
            return 6
        else:
            return 3
    def travel_city(string):
        string = literal_eval(string)[0]
        return string.get("city",0).lower().title()
    def travel_state(string):
        string = literal_eval(string)[0]
        return string.get("state",0).title()
    def travel_country(string):
        string = literal_eval(string)[0]
        return string.get("country",0).title()
    def emp_data(id_1,id_2,id_3,id_4):
        # id_1 =59
        url = "https://back.kriyakonsulting.com/index.php/api/report"
        myDictObj = { "org_id":id_4, "workplace":id_1, "department":"All", "sub_department":"All" }
        # payload = "{\r\n\"org_id\":\"5785\",\r\n\"workplace\":\"59\",\r\n\"department\":\"All\",\r\n\"sub_department\":\"All\"\r\n\t\r\n}"#"{\r\n\"org_id\":\"5785\",\r\n\"workplace\":\"59\",\r\n\"department\":\"268774\",\r\n\"sub_department\":\"268774\"\r\n\t\r\n}"
        serialized= json.dumps(myDictObj, sort_keys=True, indent=3)
        headers = {
            'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJlbWFpbCI6InJlc2V0QHJlc2V0LmNvbSJ9.qeSklac7b48DMZmgKTeDmzyCAuIAxOXeayF9-Wr-qvQ",
            'cache-control': "no-cache",
            'content-type': "application/json",
            'postman-token': "754f36d7-806d-a834-0929-ce39b93ddaa8"
            }

        response = requests.request("POST", url, data=serialized, headers=headers)
        kp = {
        "emp_id": "emp_id",
        "wp_id": "Workplace_id",
        "fun_id": "emp_dep",
        "subfun_id": "emp_sub_department",
        'aarogya_setu_residence': 'covid_positive_vicintiy_home_meters',
        'aarogya_setu_workplace': 'covid_positive_vicintiy_work_meters',
        'recentlyinteracted': 'recently_interacted_with_positive',
        'travelhistory': 'travel_history',
        'medicalhistory_no': 'medical_history',
        'gender': 'gender',
        'age': 'age',
        'Pincode': 'pincode',
        'City': 'city',
        'State': 'state',
        'Location': 'area_locality',
        'cough':'cough',
        'cold':'cold',
        'fever':'fever',
        'breadthingdiffculty': "breathing_difficulty",
        'bphypertension':"bp_hypertension",
        'diabetes':'diabetes',
        'heartlungdieases':'Heart_Lung_Disease',
        'pregentwomen':'pregnant_women',
        'prefer_towork_from_home':'Prefrence',
        'listtravelcountry':'travel_history_detail',
        'emp_sub_department':'Sub-Function',
        'emp_dep':"Function"
        }
        print(response.text)
        df = pd.DataFrame(json.loads(response.text)["data"])
        print(df.columns)
        # sys.exit(0)
        df.fillna("",inplace=True)
        # #print(df.columns)
        # print(df.columns)
        df = df.rename(columns = kp)
        df["cold"] = df["cold"].apply(lambda x:1 if x.lower()in ["Yes".lower(),'1']  else 0)
        df["cough"] = df["cough"].apply(lambda x: 1 if x.lower() in ["Yes".lower(),'1'] else 0)
        
        df["breathing_difficulty"] = df["breathing_difficulty"].apply(lambda x: 1 if x.lower()in ["Yes".lower(),'1'] else 0)
        df["fever"] = df["fever"].apply(lambda x: 1 if x.lower()in ["Yes".lower(),'1'] else 0)
        df["medical_history"] = df["medical_history"].apply(lambda x: 0 if x.lower()=="yes" else 0)
        # print(df.symptoms.tolist())
        df["symptoms"] =df[["cold","cough","breathing_difficulty","fever"]].sum(axis=1)
        # sys.exit(0)
        ################medical_history############################################
        df["diabetes"] = df['diabetes'].apply(lambda x: 1 if x.lower()in ["Yes".lower(),'1'] else 0)
        df['bp_hypertension'] = df['bp_hypertension'].apply(lambda x: 1 if x.lower()in ["Yes".lower(),'1'] else 0)
        df['Heart_Lung_Disease'] = df['Heart_Lung_Disease'].apply(lambda x: 1 if x.lower()in ["Yes".lower(),'1'] else 0)
        
        # print(df.pregentwomen.tolist())
        df["pregnant_women"] = df['pregnant_women'].apply(lambda x: 1 if x.lower()in ["Yes".lower(),'1'] else 0)
        df["symptoms_no"] = df["symptoms_no"].apply(lambda x: 0 if x.lower() in ["Yes".lower(),'1'] else 0)
        # print(df.pregnant_women.tolist())
        df["medical_history_detail"] = df[["diabetes",'bp_hypertension',"Heart_Lung_Disease","pregnant_women",'symptoms_no']].sum(axis=1)
        ######################Travel_Details####################################################
        # df["travel_history"] = df["travel_history"].apply(lambda x: 2 if x.lower()=="Yes".lower(),else 0)
        # df['travel_history_detail'] = df["listtravelcountry"].apply(travel_country)
        ########################### Other #######################################3
        df['recently_interacted_with_positive'] = df['recently_interacted_with_positive'].apply(lambda x: 3 if x.lower()=="Yes".lower() else 1)
        # sys.exit(0)
        #####################################################################3

        # print(df.covid_positive_vicintiy_work_meters.tolist())
        # print(df.covid_positive_vicintiy_work_meters.tolist())
        df["covid_positive_vicintiy_work_meters"] = df["covid_positive_vicintiy_work_meters"].apply(covid_positive_vicintiy_home_meters)
        df["Prefrence"] = df["Prefrence"].apply(lambda x: 'Office' if x.lower()=="yes" else "Work From Home")
        df["covid_positive_vicintiy_home_meters"] = df["covid_positive_vicintiy_home_meters"].apply(covid_positive_vicintiy_home_meters)
        df.loc[df.type =="org_admin", ['Workplace_id', 'emp_dep']] = 'Org Admin', 'Org Admin'
        df["type"] = df["type"].apply(self_conversion)
        df["location"] = df[["latitude","longitude"]].values.tolist()
        df.to_csv("./data_integrity/fina.csv")
        # sys.exit(0)
        return df
    def get_criticality_data(df,df_functional_data):
        #print(df.columns,df_functional_data.columns)
        is_critical = []
        saturatory_regulatory = []
        nature_of_interaction = []
        Proximity = [] 
        requires_multiple  = []
        long_duration = []
        space = []
        Cap = []
        Da = []
        screen = []
        Tg = []
        
        for i,k in df.iterrows():
            function = k.emp_dep
            #print(df_functional_data.columns)
            # sys.exit(0)
    #         #print(k.emp_sub_department)
            sub_subfunction = k.emp_sub_department
    #         #print(function,sub_subfunction)
            c = df_functional_data[df_functional_data["fun_id"]==function]
            # c = df_functional_data[df_functional_data["Sub-Function"]==sub_subfunction]
            # c = df_functional_data[() & (df_functional_data["Sub-Function"])]
            # #print(c)
            # sys.exit()
            is_critical_value = c["Is_Critical_To_Core_Business"].iloc[0] if c.shape[0]>0 else "Disagree"
            s = c['Required for Saturatory/Regulatory'].iloc[0] if c.shape[0]>0 else "Disagree"
            n = c["Nature Of Interaction"].iloc[0] if c.shape[0]>0 else "Disagree"
            p = c['Requires Working in Close Proximity'].iloc[0] if c.shape[0]>0 else "Disagree"
            r = c['Requires Multiple Intraction with People'].iloc[0] if c.shape[0]>0 else "Disagree"
            l = c['Long Duration Of Interaction Required'].iloc[0] if c.shape[0]>0 else "NA"
            k1 = c["Employee Screening availaible"].iloc[0] if c.shape[0]>0 else "No"
            space1 = c['Space_function'].iloc[0] if c.shape[0]>0 else 200
            Cap1 = c['Capacity_Function'].iloc[0] if c.shape[0]>0 else 200
            dm = c["Domain_Area"].iloc[0] if c.shape[0]>0 else 200
            tg = c["Is_Department_Core_Of_Buisness"].iloc[0] if c.shape[0]>0 else "No"
            
            
            # #print(is_critical_value,s,n,p,r,l,space)
            
            is_critical.append(is_critical_value)
            saturatory_regulatory.append(s)
            nature_of_interaction.append(n)
            Proximity.append(p)
            requires_multiple.append(p)
            long_duration.append(l)
            space.append(space1)
            Cap.append(Cap1)
            Da.append(dm)
            screen.append(k1)
            Tg.append(tg)
            #print(is_critical,saturatory_regulatory,"\n\n\n#######################3\n\n\n")
            # sys.exit(0)
        return Da,Cap1,space,is_critical,saturatory_regulatory,nature_of_interaction,Proximity,requires_multiple,long_duration,k1,Tg
            
            





    df_api_functionality  = api_functionality(id_1,id_2,id_3,id_4)
    # df_api_functionality.fillna("",inplace = True)
    df_api_functionality.to_csv("data_integrity/api_functionalityxx2.csv")
    print(df_api_functionality)
    df_functional_data    = functional_data(id_1,id_2,id_3,id_4)
    df_functional_data.fillna("",inplace=True)
    df_functional_data.to_csv("data_integrity/fntionaldetailxx1.csv")
    # sys.exit(0)
    df_emp_data           = emp_data(id_1,id_2,id_3,id_4)
    df_emp_data.fillna("",inplace=True)
    df_emp_data.to_csv("data_integrity/emp_detail1.csv")


    # sys.exit(0)
    df_data_report        = Data_Report(id_1,id_2,id_3,id_4)
    df_data_report.fillna("",inplace=True)
    df_data_report.to_csv("data_integrity/data_reportxx.csv")

    # df_functional_data["Function"] = df_functional_data["Function"].apply(lambda x: ["Finance","HR"][random.randint(0,1)])
    # df_functional_data['Sub-Function'] = df_functional_data["Sub-Function"].apply(lambda x: ["Account Payble","Account Receivable"][random.randint(0,1)]if x=="Finance" 
    #                                                                           else ["Talent Accquisition","Recruitment"][random.randint(0,1)])
    # df_functional_data['Is_Department_Core_Of_Buisness'] = df_functional_data["Is_Department_Core_Of_Buisness"].apply(lambda x: ["Largely Agree","Strongly Agree","Moderately Agree","Slightly Agree",'Disagree'][random.randint(0,4)])
    # df_functional_data['Is_Critical_To_Core_Business'] = df_functional_data["Is_Critical_To_Core_Business"].apply(lambda x: ["Largely Agree","Strongly Agree","Moderately Agree","Slightly Agree",'Disagree'][random.randint(0,4)])
    # df_functional_data['Required for Saturatory/Regulatory'] = df_functional_data["Required for Saturatory/Regulatory"].apply(lambda x: ["Largely Agree","Strongly Agree","Moderately Agree","Slightly Agree",'Disagree'][random.randint(0,4)])
    # df_functional_data['Space_function'] = df_functional_data["Space_function"].apply(lambda x: random.randint(3000,6000))
    # df_functional_data["Nature Of Interaction"] = df_functional_data["Nature Of Interaction"].apply(lambda x: ['Extended','Sporadic','Limited', 'Minimal', 'NA'][random.randint(0,4)])
    # df_functional_data['Long Duration Of Interaction Required'] = df_functional_data["Long Duration Of Interaction Required"].apply(lambda x: ["Largely Agree","Strongly Agree","Moderately Agree","Slightly Agree",'Disagree'][random.randint(0,4)])
    # df_functional_data["Domain Capacity"] = df_functional_data["Domain Capacity"].apply(lambda x: ["Largely Agree","Strongly Agree","Moderately Agree","Slightly Agree",'Disagree'][random.randint(0,4)])
    # df_functional_data["Requires Working in Close Proximity"] = df_functional_data["Requires Working in Close Proximity"].apply(lambda x: ["Largely Agree","Strongly Agree","Moderately Agree","Slightly Agree",'Disagree'][random.randint(0,4)])
    # df_functional_data["Domain_Area"] = df_functional_data["Domain_Area"].replace(to_replace ='[A-Za-z ]', value = '', regex = True)
    # df_functional_data["Requires Multiple Intraction with People"]= df_functional_data["Requires Multiple Intraction with People"].apply(lambda x: ["Largely Agree","Strongly Agree","Moderately Agree","Slightly Agree",'Disagree'][random.randint(0,4)])
    #print(df_api_functionality.columns,"####################################################################")
    # sys.exit(0)


    DomA,Cap1,space,a,b,c,d,e,f,g,Tg = get_criticality_data(df_emp_data,df_functional_data)
    # #print(Cap1,a,b,c,d,e,f)
    #print(a)
    df_emp_data["Is_Critical_To_Core_Business"]=a
    df_emp_data["Required for Saturatory/Regulatory"]=b
    df_emp_data["Nature Of Interaction"] = c
    df_emp_data["Requires Working in Close Proximity"]=d
    df_emp_data['Requires Multiple Intraction with People']=e
    df_emp_data['Long Duration Of Interaction Required'] = f
    df_emp_data['Space'] = space
    df_emp_data["Domain_Capacity"]  = Cap1
    df_emp_data["Domain_Area"] = DomA
    df_emp_data['Employee Screening availaible'] = g
    df_emp_data["Is_Department_Core_Of_Buisness"] = Tg
    #print(df_emp_data)
    df_emp_data.to_csv("./data_integrity/first.csv")
    dm = []
    pm_10 = []
    pm_11 = []
    pm_21 = []
    exp = []
    curr_role = []
    for i in df_emp_data["emp_id"].tolist():
        x = df_data_report[df_data_report["emp_id"]==i]
        pm_10.append(x["Peak Load/Deliverable Milestone 1-10"].iloc[0] if x.shape[0]>0 else "No")
        pm_11.append(x["Peak Load/Deliverable Milestone 11-20"].iloc[0] if x.shape[0]>0 else "No")
        pm_21.append(x["Peak Load/Deliverable Milestone 20-EOM"].iloc[0] if x.shape[0]>0 else "No")
        dm.append(x["Deliverable Milestone"].iloc[0] if x.shape[0]>0 else "Weekly")
        curr_role.append(x["Current_Role"].iloc[0] if x.shape[0]>0 else "Individual")
        exp.append(x["Expirience"].iloc[0] if x.shape[0]>0 else random.randint(0,10))
    df_emp_data["Peak Load/Deliverable Milestone 1-10"] = pm_10
    df_emp_data["Peak Load/Deliverable Milestone 11-20"] = pm_11
    df_emp_data["Peak Load/Deliverable Milestone 20-EOM"] = pm_21
    df_emp_data["Deliverable Milestone"] = dm
    df_emp_data["Current Role"] = curr_role
    df_emp_data["Expirience"] = exp
    df_emp_data.to_csv("data_integrity/shsh11111.csv")
    # sys.exit(0)

    # In[38]:

    Workplacex= []
    Total_Space = []
    Total_Capcity = []
    # sys.exit(0)
    for i in df_emp_data.Workplace_id:


        c = df_api_functionality[df_api_functionality["wp_id"]==i]
        Workplacex.append(c["Workplace"].iloc[0] if c.shape[0]>0 else "None")
        Total_Space.append(c['Space'].iloc[0] if c.shape[0]>0 else "None")
        Total_Capcity.append(c['Total Capacity'].iloc[0] if c.shape[0]>0 else "None")


    df_emp_data["Workplacex"] = Workplacex
    df_emp_data["Total_Space"] = Total_Space
    df_emp_data["Total_Capcity"] = Total_Capcity
    #print(df_emp_data.shape)
    df_emp_data.to_csv("data_integrity/finalxx1.csv")
    print(df_emp_data)
    return df_emp_data



# mapping_database("All","All","All",7421)
    
