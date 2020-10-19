import mpld3
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
def upper_fucnt(dictionary):
    def straight_(p):
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
        # l = {"y":0,"label":"   "}
        return [t,q,r,s,m]

def find_perfect(df,filter_1,filter_2,filter_3):
    # df.to_csv("to hell.csv")
    if filter_3!="All":
        print("yeah")
        # print(filter_2)
        t1 = df[df["WorkPlace"]==filter_1]
        print(t1)
        # ##sys.ex()
        tx = t1[t1["Function"]==filter_2]
        t3 = tx[tx["Sub-Function"]==filter_3]
        # print(t3["Sub-Function"].tolist())
        # print(t3.shape)
        t4 = t3[t3["Cluster"]=="Green"]
        # # print(t2)
        
        # print(t3.shape[0],t4.shape[0])
        # ##sys.ex(0)
        # print(tx.shape[0],t3.shape[0])
        # ##sys.ex(0)
        return t3.shape[0],t4.shape[0]
    else:
        
        t1 = df[df["WorkPlace"]==filter_1]
        t2 = t1[t1["Cluster"]=="Green"]
        t2 = t2[t2["Function"]==filter_2] if filter_2 !="All" else t2
        # t3 = t2[t2["Sub-Function"]==filter_3]

        print(t2.shape[0],"!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return t1.shape[0],t2.shape[0]


def Entry_Point(df,filter_1,filter_2,filter_3,filter_4):
    print(filter_1,filter_2,filter_3,"#################33")
    print(df.columns)
    # ##sys.ex(0)

    safe_peak_load, peak_load_values = All_choice_peakload(df,filter_1,filter_2,filter_3)
    print(safe_peak_load,peak_load_values)
    safe_prefrence, preference_values = All_choice_preference(df,filter_1,filter_2,filter_3)
    print(safe_prefrence,preference_values)
    # print(safe_peak_load,peak_load_values,safe_prefrence,preference_values,"slsl")
    safe_accomodation   = All_choice_space(df,filter_1,filter_2,filter_3)
    print(safe_accomodation)


    if filter_2!="All" and filter_3!="All":
        print("###############")
        df_x = df[df["Function"]==filter_2]
        # dx_y = df_x[df_x["Sub-Function"]==filter_3]
        df3 = df_x[df_x["Sub-Function"]==filter_3]
        df_z = df_x[df_x["Cluster"]=="Green"]
        df4 = df3[df3["Cluster"]=="Green"]
        safe_peak_load2, peak_load_values2 = All_choice_peakload(df,filter_1,filter_2,"All")
        safe_prefrence2, preference_values2 = All_choice_preference(df,filter_1,filter_2,"All")
        safe_accomodation2   = All_choice_space(df,filter_1,filter_2,"All")
        print(safe_peak_load2,peak_load_values2)
        print(safe_prefrence2,preference_values2)
        print(safe_accomodation2)
        #uncomment for fuck ups
        # return upper_fucnt({"graph1":{"Total Employee":df_x.shape[0],"Safe For Office":df_z.shape[0],
        #         "Post Spatial Constraints":safe_accomodation2,"Post PeakLoad Constraints":peak_load_values2,
        #         "Post Prefrence Constraints":preference_values2},"graph2":{"Total Employee":df3.shape[0],"Safe For Office" : df4.shape[0],
        #         "Post Spatial Constraints":safe_accomodation,"Post PeakLoad Constraints":peak_load_values, 
        #         "Post Prefrence Constraints":preference_values}})
        # if df3.shape[0]>0:
        #     return upper_fucnt({"graph1":{"Total Employee":df_x.shape[0],"Safe For Office":df_z.shape[0],
        #         "Post Spatial Constraints":safe_accomodation2,"Post PeakLoad Constraints":peak_load_values2,
        #         "Post Prefrence Constraints":preference_values2},"graph2":{"Total Employee":df3.shape[0],"Safe For Office" : df4.shape[0],
        #         "Post Spatial Constraints":safe_accomodation,"Post PeakLoad Constraints":peak_load_values, 
        #         "Post Prefrence Constraints":preference_values}})
        
        if df3.shape[0]>0:
            return upper_fucnt({"graph1":{"Total Employee":df3.shape[0],"Safe For Office" : df4.shape[0],
                "Post Spatial Constraints":safe_accomodation,"Post PeakLoad Constraints":peak_load_values, 
                "Post Prefrence Constraints":preference_values}})
        else:
            return upper_fucnt({"graph1":{"Total Employee":"","Safe For Office":"",
                "Post Spatial Constraints":"","Post PeakLoad Constraints":"",
                "Post Prefrence Constraints":""}})         
            # return {}

    df_kp1 = df[df["WorkPlace"]==filter_1] if filter_1 !="All" else df


    
    df_kp2 = df_kp1[df_kp1["Function"]==filter_2] if filter_2 !="All" else df_kp1
    df_kp3 = df_kp2[df_kp2["Sub-Function"]==filter_3] if filter_3 !="All" else df_kp2
    dfkpx = df_kp3[df_kp3["Cluster"]=="Green"]
    # print({"graph1":{"Total Employee":df_kp1.shape[0],"Safe For Office":dfkpx.shape[0],
    #             "Post Spatial Constraints":safe_accomodation,"Post PeakLoad Constraints":peak_load_values,
    #             "Post Prefrence Constraints":preference_values}})
    # #sys.ex(0)
    return  upper_fucnt({"graph1":{"Total Employee":df_kp1.shape[0],"Safe For Office":dfkpx.shape[0],
                "Post Spatial Constraints":safe_accomodation,"Post PeakLoad Constraints":peak_load_values,
                "Post Prefrence Constraints":preference_values}})






 




    #make the sqft wala
    # visualize()   



def All_choice_preference(df,filter_1,filter_2,filter_3):
    # print(df)

    df_c = df[df["WorkPlace"]==filter_1]
    all_green_ = df_c[df_c["Cluster"]=="Green"].shape[0]
    # print(df_c)
    if filter_2 == "All":

        return preference(df_c,"All","All")
    else:
        # print(filter_2)
        # print("xx")
        dft = df_c[df_c["Function"]==filter_2]
        # print(dft)
        # ##sys.ex(0)
        # print(dft)
        return preference(dft,filter_2,filter_3)

def All_choice_peakload(df,filter_1,filter_2,filter_3):

    df_c = df[df["WorkPlace"]==filter_1]
    # print(df_c)
    if filter_2 == "All":

        return peak_load(df_c,"All","All")
    else:
        # print(filter_2)
        # print("xx")
        dft = df_c[df_c["Function"]==filter_2]
        # print(dft)
        # print(dft)
        return peak_load(dft,filter_2,filter_3)
def All_choice_space(df,filter_1,filter_2,filter_3):
    # print(df.shape)
    # ##sys.ex(0)
    df_c = df[df["WorkPlace"]==filter_1]
    # print(df_c)
    # print(df_c)
    if filter_2 == "All":

        return space(df_c,"All","All")
    else:
        # print(filter_2,df_c,"@@@@@@@@@@@@@@@@@@@@")
        # print("xx")
        dft = df_c[df_c["Function"]==filter_2]
        print(dft)
        # ##sys.ex(0)
        # print(dft)
        return space(dft,filter_2,filter_3)


def peak_load(df,filter_1,filter_2):
    # print(df,"sjsjs")
    
    # print(df.Cluster)
    # df = df[df["Function"]]
    if filter_2 != "All":
        # print("yeah")
        ff = ["Peak Load/Deliverable Milestone 1-10","Peak Load/Deliverable Milestone 11-20","Peak Load/Deliverable Milestone 20-EOM"]
        today_ = datetime.datetime.today().day
        get_today_range = int(today_/10) if  int(today_/10)<3 else 2
        useful = ff[get_today_range]
        # print(useful,"SSSSSSSSSSSSSSS")
        filter_2_cluster = df[df["Cluster"]=="Green"]
        # all_safe_ = filter_2_cluster.shape[0] #thik hai
        filter_2_data    = filter_2_cluster[filter_2_cluster["Sub-Function"]==filter_2]
        all_safe_ = filter_2_data.shape[0]
        # print(filter_2_data)
        filter_2_data = filter_2_data[filter_2_data[useful]=="Yes"].shape[0]
        # print(filter_2_cluster[useful].shape[0],filter_2_data)
        all_green_    =  filter_2_data

        return all_safe_,all_green_
    else:
        
        ff = ["Peak Load/Deliverable Milestone 1-10","Peak Load/Deliverable Milestone 11-20","Peak Load/Deliverable Milestone 20-EOM"]
        today_ = datetime.datetime.today().day

        get_today_range = int(today_/10) if  int(today_/10)<3 else 2
        useful = ff[get_today_range]
        
        # print(useful,"############" )
        all_green_=df[df["Cluster"]=="Green"]
        all_safe_ = all_green_.shape[0]
        # print(all_green_["Cluster"])
        all_green_ = all_green_[all_green_[useful]=="Yes"].shape[0]

        return all_safe_,all_green_


def space(df,filter_1,filter_2):
    # print(df)
    # ##sys.ex(0)
    
    # df = df[df["Function"]]
    if filter_2 != "All":
        # ff = ["Peak Load/Deliverable Milestone 1-10","Peak Load/Deliverable Milestone 11-20","Peak Load/Deliverable Milestone 20-EOM"]
        # today_ = datetime.datetime.today().day
        # get_today_range = int(today_/10) if  int(today_/10)<3 else 2
        # useful = ff[get_today_range]
        # print("TEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE",filter_2)
        # print(df[df["Cluster"]]=="Green")
        filter_2_cluster = df[df["Cluster"]=="Green"] 
        print(filter_2_cluster,"#############")
        # ##sys.ex(0)
        if filter_2_cluster.shape[0]==0:
            return 0
        filter_2_data    = filter_2_cluster[filter_2_cluster["Sub-Function"]==filter_2] #subfuction green
        # print(filter_2_data.shape[0],"all_green_")
        print(filter_2_cluster,"kskskskskskk")
        filter_2_cluster.to_csv("bong.csv")
        area_function    = filter_2_cluster["Space"].iloc[0]
        area_subdomain   = filter_2_cluster["Domain_Area"].iloc[0]
        function_capacity = filter_2_cluster["Total_Capcity"].iloc[0]
        subdomain_capacity = filter_2_cluster["Domain_Capacity"].iloc[0]
        safe_radius       = 5
        safe_area         = math.pi*safe_radius**2
        total_accomodation = math.ceil(float(area_function)/safe_area)
        domaim_accomodation = math.ceil(float(area_subdomain)/safe_area)
        # print(domaim_accomodation,"sssk")
        all_green_ = filter_2_data.shape[0]
        final_sitting_capacity =  domaim_accomodation
        
        # all_safe_ = filter_2_data.shape[0]
        return final_sitting_capacity
    else:

        filter_2_cluster=df[df["Cluster"]=="Green"]
        all_green_ = filter_2_cluster.shape[0]
        if all_green_==0:
            return 0
        area_function    = filter_2_cluster["Space"].iloc[0]
        # print(area_function)
        area_subdomain   = filter_2_cluster["Domain_Area"].iloc[0]
        function_capacity = filter_2_cluster["Total_Capcity"].iloc[0]
        # print(function_capacity,"Domain_Capacity")
        subdomain_capacity = filter_2_cluster["Domain_Capacity"].iloc[0]
        safe_radius       = 5
        safe_area         = math.pi*safe_radius**2
        total_accomodation = math.ceil(float(area_function)/float(safe_area))
        domaim_accomodation = math.ceil(float(area_subdomain)/safe_area)
        final_sitting_capacity = total_accomodation 
        return final_sitting_capacity




def preference(df,filter_1,filter_2):
    # print(df)
    
    # df = df[df["Function"]]
    if filter_2 != "All":
        # ff = ["Peak Load/Deliverable Milestone 1-10","Peak Load/Deliverable Milestone 11-20","Peak Load/Deliverable Milestone 20-EOM"]
        # today_ = datetime.datetime.today().day
        # get_today_range = int(today_/10) if  int(today_/10)<3 else 2
        # useful = ff[get_today_range]
        # print("TEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEEE",filter_2)
        filter_2_cluster = df[df["Cluster"]=="Green"]
        filter_2_data    = filter_2_cluster[filter_2_cluster["Sub-Function"]==filter_2]
        all_green_ = filter_2_data[filter_2_data["Prefrence"]=="Office"].shape[0]
        all_safe_ = filter_2_data.shape[0]
        return all_safe_,all_green_
    else:
        # print('uuey')
        # df = df[df["Function"]==filter_1]
        # print(df)
        # ff = ["Peak Load/Deliverable Milestone 1-10","Peak Load/Deliverable Milestone 11-20","Peak Load/Deliverable Milestone 20-EOM"]
        # today_ = datetime.datetime.today().day
        # get_today_range = int(today_/10) if  int(today_/10)<3 else 2
        # useful = ff[get_today_range]
        all_green_=df[df["Cluster"]=="Green"]
        filter_2_data    = all_green_[all_green_["Sub-Function"]==filter_2]
        all_safe_ = all_green_.shape[0]
        # print(all_safe_)
        all_green_ = all_green_[all_green_["Prefrence"]=="Office"].shape[0]

        return all_safe_,all_green_

def peak_load(df,filter_1,filter_2):
    # print(df,"sjsjs")
    
    # print(df.Cluster)
    # df = df[df["Function"]]
    if filter_2 != "All":
        # print("yeah")
        ff = ["Peak Load/Deliverable Milestone 1-10","Peak Load/Deliverable Milestone 11-20","Peak Load/Deliverable Milestone 20-EOM"]
        today_ = datetime.datetime.today().day
        get_today_range = int(today_/10) if  int(today_/10)<3 else 2
        useful = ff[get_today_range]
        # print(useful,"SSSSSSSSSSSSSSS")
        filter_2_cluster = df[df["Cluster"]=="Green"]
        # all_safe_ = filter_2_cluster.shape[0] #thik hai
        filter_2_data    = filter_2_cluster[filter_2_cluster["Sub-Function"]==filter_2]
        all_safe_ = filter_2_data.shape[0]
        # print(filter_2_data)
        filter_2_data = filter_2_data[filter_2_data[useful]=="Yes"].shape[0]
        # print(filter_2_cluster[useful].shape[0],filter_2_data)
        all_green_    =  filter_2_data

        return all_safe_,all_green_
    else:
        
        ff = ["Peak Load/Deliverable Milestone 1-10","Peak Load/Deliverable Milestone 11-20","Peak Load/Deliverable Milestone 20-EOM"]
        today_ = datetime.datetime.today().day

        get_today_range = int(today_/10) if  int(today_/10)<3 else 2
        useful = ff[get_today_range]
        
        # print(useful,"############" )
        all_green_=df[df["Cluster"]=="Green"]
        all_safe_ = all_green_.shape[0]
        # print(all_green_["Cluster"])
        all_green_ = all_green_[all_green_[useful]=="Yes"].shape[0]

        return all_safe_,all_green_
def space2(df,filter_4):
    filter_2_cluster=df#df[df["Cluster"]=="Green"]
    all_green_ = filter_2_cluster.shape[0]
    if all_green_==0:
        return 0
    area_function    = filter_2_cluster["Space"].iloc[0]
    # print(area_function)
    area_subdomain   = filter_2_cluster["Domain_Area"].iloc[0]
    function_capacity = filter_2_cluster["Total_Capcity"].iloc[0]
    # print(function_capacity,"Domain_Capacity")
    subdomain_capacity = filter_2_cluster["Domain_Capacity"].iloc[0]
    safe_radius       = filter_4
    safe_area         = math.pi*safe_radius**2
    total_accomodation = math.ceil(float(area_function)/float(safe_area))
    domaim_accomodation = math.ceil(float(area_subdomain)/safe_area)
    final_sitting_capacity = total_accomodation 
    return final_sitting_capacity
def prefrence2(df):
    # all_green_=df[df["Cluster"]=="Green"]
    filter_2_data    = df #all_green_[all_green_["Sub-Function"]==filter_2]
    all_safe_ = all_green_.shape[0]
    all_green_ = all_green_[all_green_["Prefrence"]=="Office"].shape[0]
    return all_safe_,all_green_
def peak_load2(df):
    ff = ["Peak Load/Deliverable Milestone 1-10","Peak Load/Deliverable Milestone 11-20","Peak Load/Deliverable Milestone 20-EOM"]
    today_ = datetime.datetime.today().day
    get_today_range = int(today_/10) if  int(today_/10)<3 else 2
    useful = ff[get_today_range]
    print(df)
    # sys.exit(0)
    all_green_= df #df[df["Cluster"]=="Green"]

    all_safe_ = all_green_.shape[0]
        # print(all_green_["Cluster"])
    all_green_ = all_green_[all_green_[useful]=="Yes"].shape[0]

    return all_safe_,all_green_
def All_All_All(df,filter_4):
    total_employee = df.shape[0]
    safe_for_office = df[df["Cluster"]=="Green"]
    peak_load_all_safe,peak_load_values = peak_load(df)
    f_,preference_values = preference2(df)
    f_,space_values = space2(post_filter,filter_4)

    return total_employee,safe_for_office,peak_load_values,preference_values,space_values
def All_All_sub(df,filter_sub,filter_4):
    post_filter = df[df["Sub-Function"]==filter_sub]
    total_employee = post_filter.shape[0]
    safe_for_office = post_filter[post_filter["Cluster"]=="Green"].shape[0]
    peak_load_all_safe , peak_load_values = peak_load2(post_filter)
    f_,preference_values = preference2(post_filter)
    f_,space_values     = space2(post_filter,filter_4)
    return total_employee,safe_for_office,peak_load_values,preference_values,space_values
def All_fun_all(df,filter_f,filter_4):
    post_filter = df[df["Function"]==filter_f]
    total_employee = post_filter.shape[0]
    # print(total_employee)
    # sys.exit(0)
    safe_for_office = post_filter[post_filter["Cluster"]=="Green"].shape[0]
    peak_load_all_safe , peak_load_values = peak_load2(post_filter)
    f_,preference_values = preference2(post_filter)
    f_,space_values     = space2(post_filter,filter_4)
    return total_employee,safe_for_office,peak_load_values,preference_values,space_values
def All_fun_fun(df,filter_1,filter_2,filter_4):
    post_filter_1 = df[df["Function"]==filter_1]
    post_filter_2 = df[df["Sub-Function"]==filter_2]
    total_employee = post_filter_2.shape[0]
    safe_for_office = post_filter_2[post_filter_2["Cluster"]=="Green"].shape[0]
    peak_load_values,peak_load_values = peak_load2(post_filter_2)
    f_,preference_values = preference2(post_filter_2)
    f_,space_values     = space2(post_filter_2,filter_4)
    return total_employee,safe_for_office,peak_load_values,preference_values,space_values
def Fun_All_All(df,filter_1,filter_4):
    post_filter = df[df["WorkPlace"]==filter_1]
    total_employee = post_filter.shape[0]
    safe_for_office = post_filter[post_filter["Cluster"]=="Green"].shape[0]
    f_,peak_load_values = peak_load2(post_filter)
    f_,preference_values = preference2(post_filter)
    f_,space_values     = space2(post_filter,filter_4)
    return total_employee,safe_for_office,peak_load_values,preference_values,space_values
def Fun_All_Fun(df,filter_1,filter_2,filter_4):
    post_filter = df[df["WorkPlace"]==filter_1]
    post_filter_2 = post_filter[post_filter["Sub-Function"]==filter_2]
    total_employee = post_filter_2.shape[0]
    safe_for_office = post_filter_2[post_filter_2["Cluster"]=="Green"].shape[0]
    f_,peak_load_value = peak_load2(post_filter_2)
    f_,preference_values = preference2(post_filter_2)
    f_,space_values     = space2(post_filter_2,filter_4)
    return total_employee,safe_for_office,peak_load_values,preference_values,space_values
def Fun_Fun_All(df,filter_1,filter_2,filter_4):
    post_filter = df[df["WorkPlace"]==filter_1]
    post_filter_2 = post_filter[post_filter["Function"]==filter_2]
    total_employee = post_filter_2.shape[0]
    safe_for_office = post_filter_2[post_filter_2["Cluster"]=="Green"].shape[0]
    f_,peak_load_values = peak_load2(post_filter_2)
    f_,preference_values = preference2(post_filter_2)
    f_,space_values     = space2(post_filter_2,filter_4)
    return total_employee,safe_for_office,peak_load_values,preference_values,space_values
def Fun_Fun_Fun(df,filter_1,filter_2,filter_3,filter_4):
    post_filter = df[df["WorkPlace"]==filter_1]
    post_filter = post_filter[post_filter["Function"]==filter_2]
    total_employee = post_filter.shape[0]
    safe_for_office = post_filter[post_filter["Cluster"]=="Green"].shape[0]
    post_filter = post_filter[post_filter["Sub-Function"]==filter_3]
    f_,peak_load_values = peak_load2(post_filter)
    f_,preference_values = preference2(post_filter_2)
    f_,space_values     = space2(post_filter,filter_4)
    return total_employee,safe_for_office,peak_load_values,preference_values,space_values
def entry_point(df,filter_1,filter_2,filter_3,filter_4):
    if filter_1=="All" and filter_2 == "All" and filter_3 == "All":
        return upper_fucnt(All_All_All(df,filter_4))
    if filter_1=="All" and filter_2 == "All" and filter_3 != "All":
        return upper_fucnt(All_All_sub(df,filter_3,filter_4))
    if filter_1=="All" and filter_2 != "All" and filter_3 == "All":
        return upper_fucnt(All_fun_all(df,filter_2,filter_4))
    if filter_1=="All" and filter_2 != "All" and filter_3 != "All":
        return upper_fucnt(All_fun_fun(df,filter_2,filter_3,filter_4))
    if filter_1!="All" and filter_2 == "All" and filter_3 == "All":
        return upper_fucnt(Fun_All_All(df,filter_1,filter_4))
    if filter_1!="All" and filter_2 == "All" and filter_3 != "All":
        return upper_fucnt(Fun_All_Fun(df,filter_1,filter_3,filter_4))
    if filter_1!="All" and filter_2 != "All" and filter_3 == "All":
        return upper_fucnt(Fun_Fun_All(df,filter_1,filter_2,filter_4))
    if filter_1!="All" and filter_2 != "All" and filter_3 != "All":
        return upper_fucnt(Fun_Fun_Fun(df,filter_1,filter_2,filter_3,filter_4))







