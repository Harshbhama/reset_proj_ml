import pandas as pd
import numpy as np
import sys
from sklearn import preprocessing

def Is_Department_Core_Of_Buisness_(string):
    if string == "Yes":
        return 3
    if string =="No":
        return 1
    if string  == "Other":
        return 2
    else:
        return 0

def current_role_(string):
    if str(string) in  ["Individual Contributor","Individual"]:
        return 1
    if str(string) == "Team Lead":
        return 2
    if str(string) == "Manager":
        return 3
    if str(string) == 'Sr. Management':
        return 4
    else:
        return 1.5

def deliverable_milestone_(string):
    if string == "Daily":
        return 4
    if string == "Weekly":
        return 2
    if string == "Fort-nightly":
        return 1
    if string == "Monthly":
        return 1
    
def Is_Critical_To_Core_Business_(string):
    if string == 'Strongly Agree':
        return 5
    if string == 'Largely Agree':
        return 4
    if string == 'Moderately Agree':
        return 3
    
    if string == 'Slightly Agree':
        return  2
    if string in ['disagree','Disagree']:
        return 1
    else :
        return 1
def Expirience(number):
    number =float(number)
    if 0<=number<=3:
        return 1
    if 3<number<=6:
        return 2
    if 6<number<=10:
        return 3
    if 10<number<=15:
        return 4
    if 15<number<=20:
        return 5
    if 20<number<=29:
        return 6
    if number>=30:
        return 7
def Nature_Of_interaction_(string):
    if  "Digital" in string:
        return  0
    if "In-person":
        return 2
    if "Both" in strings:
        return 1
    else:
        return 0
def Requires_Working_in_Close_Proximity_(string):
    if string == 'Strongly Agree':
        return 5
    if string == 'Largely Agree':
        return 4
    if string == 'Moderately Agree':
        return 3
    
    if string == 'Slightly Agree':
        return  2
    if string in ['disagree','Disagree']:
        return 1
    else:
        return 0
def Requires_Multiple_Intraction_with_People_(string):
    if string == 'Strongly Agree':
        return 5
    if string == 'Largely Agree':
        return 4
    if string == 'Moderately Agree':
        return 3
    
    if string == 'Slightly Agree':
        return  2
    if string in ['disagree','Disagree']:
        return 1
    else:
        return 0
#'Extended','Sporadic','Limited', 'Minimal', 'NA'
def Long_Duration_Of_Interation_Required_(string):
    if string == 'Extended':
        return 5
    if string == 'Sporadic':
        return 4
    if string == 'Limited':
        return 3
    
    if string == 'Minimal':
        return  2
    if string in ['NA']:
        return 1 
    else:
        return 0
def Employee_Screening_availaible_(string):
    if string == "Yes":
        return 1
    if string == "No":
        return 2
    else:
        return 0.5
def Required_for_Saturatory_Regulatory_(string):
    if string == 'Strongly Agree':
        return 5
    if string == 'Largely Agree':
        return 4
    if string == 'Moderately Agree':
        return 3
    
    if string == 'Slightly Agree':
        return  2
    if string in ['disagree','Disagree']:
        return 1
    else:
        return 2
#######################################Vulnerability_Preprocessing_functions################################

def age1(number):
     return number
def symptoms(string):
    count = 0
    if "No symptoms" in string:
        count+= 1
    if 'Cold' in string:
        count+=3
    if "Cough" in string:
        count+=3
    if "Fever" in string:
        count+=4
    if "Breathing Problem" in string:
        count+=5

    return count
def medical_history(string):
    if string== "Not Applicable":
        return 1
    if string =="No":
        return 1
    if string =="Yes":
        return 3
def recently_interacted_with_covid_positive(string):

    if string =="No":
        return 1
    if string =="Yes":
        return 3
def covid_positive_vicintiy_home_meters(string):
    # print(type(string))
    if str(int(float(string))) in ["10",'10000']:
        return 1
    if  str(int(float(string))) in ["5","5000"]:
        return 2
    if str(int(float(string))) in ["2000","2"]:
        return 4
    if str(int(float(string)))in ["1","10000"]:
        return 5
    if str(int(float(string))) == ["500","0.5"]:
        return 6
def covid_positive_vicintiy_work_meters(string):
    
    if str(int(float(string))) in ["10",'10000']:
        return 1
    if  str(int(float(string))) in ["500","5000"]:
        return 2
    if str(int(float(string))) in ["2000","2"]:
        return 4
    if str(int(float(string)))in ["1","10000"]:
        return 5
    if str(int(float(string))) == ["500","0.5"]:
        return 6
    
def zone_area(string):
    if string=="Containment Zone":
        return 5
    if string == "Red Zone":
        return 3
    if string in ["Orange Zone","No Classification Zone","None",None]:
        return 2
    if string == "Green Zone":
        return 1

def travel_destination_zone(string):
    if string=="Containment Zone":
        return 5
    if string == "Red Zone":
        return 3
    if string in ["Orange Zone","No Classification Zone",None,"None"]:
        return 2
    if string == "Green Zone":
        return 1
    else:
        return 0
def medical_history_details(string):
    count = 0
    if  "BP/Hypertension" in string:
        count+= 2
    if "Diabetes" in string:
        count+= 1
    if "Heart/Lung Disease" in string:
        count+=5
    if "Pregnant" in string:
        count+=4
    return count
def travel_history(string):
    if string == "Yes":
        return 3
    if string == "Not Applicable":
        return 1
    if string =="No":
        return 1
    else:
        return 1

####################################################Main Preprocessing  Function #######################

def pre_processing_criticality(df):
    values=[]
    df["Is_Department_Core_Of_Buisness"]      = df["Is_Department_Core_Of_Buisness"].apply(Is_Department_Core_Of_Buisness_)
    df["Is_Critical_To_Core_Business"]        = df["Is_Critical_To_Core_Business"].apply(Is_Critical_To_Core_Business_)
    df["Required for Saturatory/Regulatory"]  = df["Required for Saturatory/Regulatory"].apply(Required_for_Saturatory_Regulatory_)
    # print(df["Long Duration Of Interaction Required"])
    
    df["Expirience"]                          = df["Expirience"].apply(Expirience)
    df["Nature Of Interaction"]               = df["Nature Of Interaction"].apply(Nature_Of_interaction_)
    df["Requires Working in Close Proximity"] = df["Requires Working in Close Proximity"].apply(Requires_Working_in_Close_Proximity_)
    df["Current Role"]                         = df["Current Role"].apply(current_role_)
    df["Long Duration Of Interaction Required"]= df["Long Duration Of Interaction Required"].apply(Long_Duration_Of_Interation_Required_)
    df["Employee Screening availaible"]       = df["Employee Screening availaible"].apply(Employee_Screening_availaible_)
    df["Deliverable Milestone"]               = df["Deliverable Milestone"].apply(deliverable_milestone_)
    df["Requires Multiple Intraction with People"] = df["Requires Multiple Intraction with People"].apply(Requires_Multiple_Intraction_with_People_)
    df_clustering = df[["Is_Department_Core_Of_Buisness","Is_Critical_To_Core_Business","Required for Saturatory/Regulatory",
                        "Expirience","Nature Of Interaction","Requires Working in Close Proximity",
                        "Current Role","Long Duration Of Interaction Required","Employee Screening availaible"
                        ,"Deliverable Milestone","Requires Multiple Intraction with People"]]
    
    df_clustering.to_csv("./data_integrity/awesome2.csv")
    return df_clustering.values.tolist()

def pre_processing_vulnerability(df):
    """Medical History, Symptoms are pre-processed in map_database.py"""
    values  = []
    df["travel_history"] = df["travel_history"].apply(travel_history)
    df["age"]            = df["age"].apply(age1)
    df["recently_interacted_with_positive"] = df["recently_interacted_with_positive"].apply(recently_interacted_with_covid_positive)
    df["covid_positive_vicintiy_home_meters"] = df["covid_positive_vicintiy_home_meters"].apply(covid_positive_vicintiy_home_meters)
    df["covid_positive_vicintiy_work_meters"]     = df["covid_positive_vicintiy_work_meters"].apply(covid_positive_vicintiy_work_meters)
    df["zone"] = df["zone"].apply(zone_area)
    df["travel_destination_zone"] = df["travel_destination_zone"].apply(travel_destination_zone)
    df.to_csv("./data_integrity/done.csv")
    df_vulnerability  = df[["zone","travel_destination_zone","symptoms","medical_history_detail",
                            "recently_interacted_with_positive","covid_positive_vicintiy_home_meters"]]
    return df_vulnerability.values.tolist()

