def peak_load_graph(df,filter_2,filter_3 = "None"):
    
    
    today_ = datetime.datetime.today().day
    get_today_range = int(today_/10) if  int(today_/10)<3 else 2
    
    ff = ["Peak Load/Deliverable Milestone 1-10","Peak Load/Deliverable Milestone 11-20","Peak Load/Deliverable Milestone 20-EOM"]
    useful = ff[get_today_range]
    legendwa  = ['Suited For Peak Load/Deliverable Milestone 1-10','Suited For Peak Load/Deliverable Milestone 11-20',"Suited For Peak Load/Deliverable Milestone 20-EOM"]
    
#     print(get_today_range)
    legendwa[get_today_range] = "Suited Post Peak Load"
#     df_2 = df[filter_2]
    df_2 = df[df["Function"]==filter_2]
    df_x = df_2[df_2["Cluster"]=="Green"]
    total_employe_filter_1   = df_2.shape[0]
    safe_to_call_filter_1     = df_2[df_2["Cluster"]=="Green"].shape[0]
    print(safe_to_call_filter_1)
    
    peak_delivarable_1_to_10_filter_1 = df_x[df_x["PeakLoad"] == useful].shape[0]
    preference = df_x[df_x["Prefrence"]=="Office"].shape[0]
#     peak_delivarable_10_to_20_filter_1 = df_2[df_2["PeakLoad"] == "Peak Load/Deliverable Milestone 11-20"].shape[0]
#     peak_delivarable_21_to_eom_filter_1 = df_2[df_2["PeakLoad"] == "Peak Load/Deliverable Milestone 20-EOM"].shape[0]
#     total_employe_filter_2   = 15
#     safe_to_call_filter_2 = 5
#     peak_delivarable_1_to_10_filter_2 = 3
#     peak_delivarable_10_to_20_filter_2 = 1
#     peak_delivarable_21_to_eom_filter_2 = 1
    
    if filter_3 != "All":
        df_3 = df[df["Sub-Function"]==filter_3]
        df_4 = df_3[df["Cluster"]=="Green"]
        total_employe_filter_2 = df_3.shape[0]
        safe_to_call_filter_2  = df_3[df_3["Cluster"]=="Green"].shape[0]
        peak_delivarable_1_to_10_filter_2 = df_4[df_4["PeakLoad"] == useful].shape[0]
        preference2 = df_4[df_4["Prefrence"]=="Office"].shape[0]
#         print(peak_delivarable_10_to_20_filter_2)
#         print(peak_delivarable_1_to_10_filter_1)
        
#         peak_delivarable_10_to_20_filter_1 = df_3[df_3["PeakLoad"] == "Peak Load/Deliverable Milestone 11-20"].shape[0]
#         peak_delivarable_21_to_eom_filter_1 = df_3[df_3["PeakLoad"] == "Peak Load/Deliverable Milestone 20-EOM"].shape[0]
# #     total_employe_filter_2   = 15
        

        labels = [filter_2.title(),filter_3]
        x = np.arange(len(labels))
        total_emp = [total_employe_filter_1,total_employe_filter_2]
        men_means = [peak_delivarable_1_to_10_filter_1, peak_delivarable_1_to_10_filter_2 ]
        women_means = [preference,preference2]

        x = np.arange(len(labels))  # the label locations
        width = 0.10  # the width of the bars
        lmn = area_wise(df,filter_2)
        fig, ax = plt.subplots()
        rectsx = ax.bar(x - width/2, total_emp, width, label="Total Employee",color="orange")
        rectsx2 = ax.bar(x + width/2, [safe_to_call_filter_1,safe_to_call_filter_2] ,width, label="Safe For Returning To Office",color="yellow")
        xxc     = ax.bar(x + .15, lmn[2], width, label="Post Spatial Constraints",color='pink')

        rects1 = ax.bar(x + 0.25, men_means, width, label="Post PeakLoad Preference",color="green")
        rects2 = ax.bar(x + 0.33, women_means, width, label="Post Employee Preference",color="blue")
#         rects3 = ax.bar(x+.52,women_means,.15,label=legendwa[2])
        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Number Of Employees')
        ax.set_title('Peak Load Constraints ')
        ax.set_xticks(x)
        ax.set_xticklabels(labels,fontsize= 'x-large')
        ax.legend()
        xxx = 200

    else:
        print("Yeah")
        labels = [filter_2.title()]
        x = np.arange(len(labels))
        total_emp = [total_employe_filter_1]
        men_means = [peak_delivarable_1_to_10_filter_1]
        prefe =  [preference]


        x = np.arange(len(labels))  # the label locations
        width = 0.05  # the width of the bars
        lmn = area_wise(df)
        fig, ax = plt.subplots()
        rectsx = ax.bar(x-width/2 , total_emp, width, label="Total Employee",color="red")
        rectsx2 = ax.bar(x + width/2, [safe_to_call_filter_1], width, label="Safe For Returning to Office",color='pink')
        xxc     = ax.bar(x + .075, lmn[2], width, label="Post Spatial Constraints",color='yellow')
        rects1 = ax.bar(x+.12, men_means, width, label=legendwa[0],color = "green")
        rects2 = ax.bar(x + 0.15, prefe, width, label="Post Employee Prefrence",color = "blue")
#         rects3 = ax.bar(x+.52,third,.15,label=legendwa[2])
        # Add some text for labels, title and custom x-axis tick labels, etc.
        ax.set_ylabel('Number Of Employees')
        ax.set_title('Post Constraints ')
        ax.set_xticks(x)
        ax.set_xticklabels(labels,fontsize= 'medium')
        ax.legend()
        xxx = 100

        
    def autolabel(rects):
        """Attach a text label above each bar in *rects*, displaying its height."""
        for rect in rects:
            height = rect.get_height()
            ax.annotate('{}'.format(height),
                        xy=(rect.get_x() + rect.get_width() / 2, height),
                        xytext=(0, 3),  # 3 points vertical offset
                        textcoords="offset points",
                        ha='center', va='bottom')

    autolabel(rectsx)
    autolabel(rectsx2)
    autolabel(xxc)
    autolabel(rects1)
    autolabel(rects2)