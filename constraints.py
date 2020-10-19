import pandas as pd 
import math
import sys

def area_wise(df,filter_1=True):

    if True:#filter_1=="All":

        total_area_office = 100
        total_area = int(100) #1000  Whole office area
        total_capacity  = 4 #all the employees # 50
        total_green    = df[df["Cluster"]=="Green"].shape[0] #all the employees without risk  # 20
        safe_radius_guideline = 4 # 5
        safe_area_required_per_person = math.pi*safe_radius_guideline**2 # to be calculated
        Number_of_accomodations = math.ceil(total_area/safe_area_required_per_person) # safe acco on guidelines
        print(Number_of_accomodations)
        # sys.exit()
        green_left_outs       = total_green - Number_of_accomodations if total_green>Number_of_accomodations else Number_of_accomodations-total_green


        domain_1_area = int(50) #area designated to domain # 600
        # domain_2_area = int(sys.argv[6])  #400 
        domain_1_head_count  =  int(5) #35
        # domain_2_head_count = int(sys.argv[8]) #15
        
   
        domain_1_green      = df[df["Cluster"]=="Green"].shape[0] # 15 
        # domain_2_green      = int(sys.argv[10]) #5
        print(domain_1_green)
        count=1

        print(domain_1_green,domain_1_head_count,domain_1_area,"slsls")
        # sys.exit()
        domain_1_to_be_called = 0
        domain_2_to_be_called = 0
        while count<=Number_of_accomodations:
        	print(count,domain_1_to_be_called)
        	if domain_1_to_be_called<domain_1_green:
        		print(domain_1_to_be_called<=domain_1_green)
        		domain_1_to_be_called+=1
        		count+=1
        	else:
        		pass
    else:
        pass

    print(domain_1_head_count,domain_1_green,domain_1_to_be_called)
    return [domain_1_head_count,domain_1_green,domain_1_to_be_called]

# df = pd.read_csv("plotting_data.csv")
# dfx = df[df["WorkPlace"] == "Bangalore"]
# area_wise(dfx,"All")