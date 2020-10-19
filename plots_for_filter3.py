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
        list_1 = ["blue","green","orange","yellow","red"]
        k = []
        t = {"y":p["Total Employee"],"label":"Total Employee","color":list_1[0]}
        q = {"y":p["Safe For Office"],"label":"Safe For Office","color":list_1[1]}
        r = {"y":p["Post Spatial Constraints"],"label":"Post Spatial Constraints","color":list_1[2]}
        s = {"y":p["Post PeakLoad Constraints"],"label":"Post PeakLoad Constraints","color":list_1[3]}
        m = {"y":p["Post Prefrence Constraints"],"label":"Post Prefrence Constraints","color":list_1[4]}
        l = {"y":0,"label":","}
        return [t,q,r,s,m,l]
    

    mp = []  
#     print(dictionary.keys())
    for i in list(dictionary.keys()):
        print(i)
        print(i)
        cji = straight_(dictionary[i])
        mp.extend(cji)
        
    return mp
def find_perfect(df,filter_1,filter_2,filter_3):
    # df.to_csv("to hell.csv")
    if filter_3!="All":
        print("yeah")
        # print(filter_2)
        t1 = df[df["WorkPlace"]==filter_1]
        print(t1)
        # sys.exit()
        tx = t1[t1["Function"]==filter_2]
        t3 = tx[tx["Sub-Function"]==filter_3]
        # print(t3["Sub-Function"].tolist())
        # print(t3.shape)
        t4 = t3[t3["Cluster"]=="Green"]
        # # print(t2)
        
        # print(t3.shape[0],t4.shape[0])
        # sys.exit(0)
        # print(tx.shape[0],t3.shape[0])
        # sys.exit(0)
        return t3.shape[0],t4.shape[0]
    else:
        
        t1 = df[df["WorkPlace"]==filter_1]
        t2 = t1[t1["Cluster"]=="Green"]
        t2 = t2[t2["Function"]==filter_2] if filter_2 !="All" else t2
        # t3 = t2[t2["Sub-Function"]==filter_3]

        print(t2.shape[0],"!!!!!!!!!!!!!!!!!!!!!!!!!!!")
        return t1.shape[0],t2.shape[0]


def Entry_Point(df,filter_1,filter_2,filter_3):
    print(filter_1,filter_2,filter_3,"#################33")
    print(df.columns)
    # sys.exit(0)

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

        return upper_fucnt({"graph1":{"Total Employee":df_x.shape[0],"Safe For Office":df_z.shape[0],
                "Post Spatial Constraints":safe_accomodation2,"Post PeakLoad Constraints":peak_load_values2,
                "Post Prefrence Constraints":preference_values2},"graph2":{"Total Employee":df3.shape[0],"Safe For Office" : df4.shape[0],
                "Post Spatial Constraints":safe_accomodation,"Post PeakLoad Constraints":peak_load_values, 
                "Post Prefrence Constraints":preference_values}})

    print("ehe")
    df_kp1 = df[df["WorkPlace"]==filter_1]
    print(df_kp1.shape)

    df_kp2 = df_kp1[df_kp1["Function"]==filter_2] if filter_2 !="All" else df_kp1
    df_kp3 = df_kp2[df_kp2["Sub-Function"]==filter_3] if filter_3 !="All" else df_kp2
    dfkpx = df_kp3[df_kp3["Cluster"]=="Green"]
    return  upper_fucnt({"graph1":{"Total Employee":df_kp1.shape[0],"Safe For Office":dfkpx.shape[0],
                "Post Spatial Constraints":safe_accomodation,"Post PeakLoad Constraints":peak_load_values,
                "Post Prefrence Constraints":preference_values}})






 




    #make the sqft wala
    # visualize()   
def autolabel(rects,ax):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')


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
        # sys.exit(0)
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
    # sys.exit(0)
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
        # sys.exit(0)
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
    # sys.exit(0)
    
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
        # sys.exit(0)
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
        total_accomodation = math.ceil(area_function/safe_area)
        domaim_accomodation = math.ceil(area_subdomain/safe_area)
        # print(domaim_accomodation,"sssk")
        all_green_ = filter_2_data.shape[0]
        final_sitting_capacity =  domaim_accomodation
        
        # all_safe_ = filter_2_data.shape[0]
        return final_sitting_capacity
    else:
        # print('uuey')
        # df = df[df["Function"]==filter_1]
        # print(df)
        # ff = ["Peak Load/Deliverable Milestone 1-10","Peak Load/Deliverable Milestone 11-20","Peak Load/Deliverable Milestone 20-EOM"]
        # today_ = datetime.datetime.today().day
        # get_today_range = int(today_/10) if  int(today_/10)<3 else 2
        # useful = ff[get_today_range]
        filter_2_cluster=df[df["Cluster"]=="Green"]
        print(filter_2_cluster,"XXXX")
        # print(filter_2_cluster.shape,"filter_2_cluster")

        # filter_2_data    = filter_2_cluster[filter_2_cluster["Sub-Function"]==filter_2] #subfuction green
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
        # print(safe_area,"safe_area")
        total_accomodation = math.ceil(float(area_function)/float(safe_area))
        print(type(area_function),type(safe_area),total_accomodation,"total")
        # sys.exit(0)

        domaim_accomodation = math.ceil(float(area_subdomain)/safe_area)
        # print(domaim_accomodation,"domain Capacity")
        # filter_2_data    = all_green_[all_green_["Sub-Function"]==filter_2]
        # all_safe_ = all_green_.shape[0]
        
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


def visualize(df,a,d,t,b,c,filter_1,filter_2,filter_3):



    
    print("###############################################")
    print(a,d,t,b,c)

    labels = [filter_2,filter_3] if filter_2!="All" else [filter_2]
    x = np.arange(len(labels))
    total_emp = a
    safe = d
    men_means = b
    women_means = c
    space = t
    
    # print(labels,"@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@")
    x = np.arange(len(labels))  # the label locations
    width = 0.10  # the width of the bars
    
    fig, ax = plt.subplots()
    rectsx = ax.bar(x - width/2, total_emp, width, label="Total Employee",color="orange")
    rectsx2 = ax.bar(x + width/2,safe,width, label="Safe For Returning To Office",color="yellow")
    rectsx3 = ax.bar(x + .20 , space ,width, label="Post Space Constraints",color="pink")
    rects1 = ax.bar(x + 0.28, men_means, width, label="Post PeakLoad Preference",color="green")
    rects2 = ax.bar(x + 0.36, women_means, width, label="Post Employee Preference",color="blue")
#         rects3 = ax.bar(x+.52,women_means,.15,label=legendwa[2])
        # Add some text for labels, title and custom x-axis tick labels, etc.
    ax.set_ylabel('Number Of Employees')
    ax.set_title('Constraints Graph')
    ax.set_xticks(x)
    ax.set_xticklabels(labels,fontsize= 'medium')
    ax.legend(fancybox=True, framealpha=0.5,loc='upper center', shadow=True, fontsize='medium',bbox_to_anchor=(1, 1))
    xxx = 200
    autolabel(rectsx,ax)
    autolabel(rectsx2,ax)
    autolabel(rectsx3,ax)
    # autolabel(xxc)
    autolabel(rects1,ax)
    autolabel(rects2,ax)
#     autolabel(rects3)
#     mpld3.save_html(fig,"test2.html")
    
    fig.tight_layout()

    plt.show()

    tmpfile = BytesIO()
    # plt.show()
    fig.savefig(tmpfile, format='png')
    encoded = base64.b64encode(tmpfile.getvalue()).decode('utf-8')
    html = '' + '<img src=\'data:image/png;base64,{}\'>'.format(encoded) + ''
        
    
'''Headquarter - Mum    Finance Account Payble  6211    1000    600 35  Red Office  Yes No  Yes Peak Load/Deliverable Milestone 1-10
Bangalore   HR  Talent Acquisition  2356    1000    400 15  Green   Office  Yes Yes Yes Peak Load/Deliverable Milestone 1-10
Bangalore   Finance Account Payble  4095    1000    600 35  Green   Office  Yes No  No  Peak Load/Deliverable Milestone 11-20
Bangalore   Finance Account Payble  9826    1000    400 35  Red Work From Home  Yes Yes No  Peak Load/Deliverable Milestone 1-10
Headquarter - Mum   Finance Account Payble  9571    1000    400 35  Red Office  Yes Yes No  Peak Load/Deliverable Milestone 20-EOM
Bangalore   Finance Account Payble  3307    1000    400 35  Green   Office  Yes Yes Yes Peak Load/Deliverable Milestone 1-10
Headquarter - Mum   Finance Account Payble  7513    1000    400 35  Green   Office  No  No  No  Peak Load/Deliverable Milestone 20-EOM
Headquarter - Mum   Production  Development 6277    1000    500 18  Green   Office  Yes No  Yes Peak Load/Deliverable Milestone 11-20
Headquarter - Mum   HR  Talent Acquisition  1952    1000    400 15  Green   Work From Home  No  No  Yes Peak Load/Deliverable Milestone 1-10
Headquarter - Mum   HR  Talent Acquisition  6875    1000    400 15  Green   Office  No  Yes Yes Peak Load/Deliverable Milestone 20-EOM
Headquarter - Mum   HR  Talent Acquisition  3333    1000    400 15  Green   Office  Yes No  Yes Peak Load/Deliverable Milestone 1-10
Bangalore   HR  Recruting   3793    1000    400 15  Green   Office  No  Yes No  Peak Load/Deliverable Milestone 11-20
Bangalore   HR  Recruting   2827    1000    500 18  Green   Work From Home  No  No  No  Peak Load/Deliverable Milestone 20-EOM
Bangalore   HR  Talent Acquisition  1028    1000    500 18  Red Office  Yes Yes Yes Peak Load/Deliverable Milestone 1-10
Headquarter - Mum   HR  Talent Acquisition  4372    1000    500 18  Red Work From Home  Yes Yes Yes Peak Load/Deliverable Milestone 20-EOM
Headquarter - Mum   HR  Talent Acquisition  6363    1000    500 18  Green   Office  Yes Yes Yes Peak Load/Deliverable Milestone 1-10
Headquarter - Mum   Finance Account Payble  9571    1000    400 35  Red Office  Yes Yes No  Peak Load/Deliverable Milestone 20-EOM
Bangalore   Finance Account Receivable  3307    1000    400 35  Green   Office  Yes Yes Yes Peak Load/Deliverable Milestone 1-10
Headquarter - Mum   Finance Account Payble  7513    1000    400 35  Green   Work From Home  No  No  No  Peak Load/Deliverable Milestone 20-EOM
Headquarter - Mum   Finance Account Payble  6277    1000    500 18  Green   Office  Yes No  Yes Peak Load/Deliverable Milestone 11-20
Bangalore   HR  Recruting   2827    1000    500 18  Green   Work From Home  Yes No  No  Peak Load/Deliverable Milestone 20-EOM
Bangalore   HR  Recruting   2827    1000    500 18  Green   Office  Yes No  No  Peak Load/Deliverable Milestone 20-EOM
Bangalore   HR  Recruting   2827    1000    500 18  Red Office  Yes No  No  Peak Load/Deliverable Milestone 20-EOM
'''
    # plt.show()
# df = pd.read_csv("to hell.csv")

# # print(df.columns)
# # # sys.exit(0)
# print((Entry_Point(df,"Bangalore","Finance","Account Payble")))# do not send ""
