import sys
import json
import requests

def save_to_db(df_k,org_id):
    df_k = df_k.rename(columns = {"Workplace_id":"WorkPlace","criticality_level":"Criticality","vulnerability_level":"Vulnerability", "emp_dep":"Function",'emp_sub_department':"Sub-Function"})
    df_k = df_k[["Cluster","Criticality","Vulnerability","WorkPlace","Function","Sub-Function","emp_id"]]
    df_k["Function"] = df_k["Function"]
    df_k["json"]= df_k.apply(lambda x: json.loads(x.to_json()), axis=1)
    url = "https://back.kriyakonsulting.com/index.php/api/runsumDatainsert"
    myDictObj = {"org_id":str(org_id),"data":df_k.json.tolist()}
    serialized= json.dumps(myDictObj, sort_keys=True, indent=3)
    headers = {
               'authorization': "Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.InJlc2V0MjAyMEAxNTkwNzczMDQzIg.XZ-05OIGu-I1Xa8B3_cRtRfK0losg3w4Kybqc2Cfa8g",
               'content-type': "application/json",
                'cache-control': "no-cache",
                'postman-token': "af50e7ad-d67c-4b91-e62d-07802ea2c2ac"
                }
    response = requests.request("POST", url, data=serialized, headers=headers)
    # print(response)
    return 1
