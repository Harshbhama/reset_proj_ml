import matplotlib.pyplot as plt
import numpy as np
#import mpld3
import random
from matplotlib.colors import ListedColormap
import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
import pandas as pd
import sys
def plot1(data):
    #print("sjnsjnsjsnjsnsjn")

    fig, ax = plt.subplots()
    N = 100
    xa = data["criticality_prediction"]
    xb = data["vulnerability_prediction"]

    def x_1(num):
        if num == 0:
            return random.randint(0,11)
        
        if num == 1:
            return random.randint(12,24) #11 to 20
        
        if num==2:
            return random.randint(25,36) #21 to 30
        if num ==3:
            return random.randint(37,48)
    def y_1(num):
        if num == 0:
            return random.randint(0,11)
        
        if num == 1:
            return random.randint(12,24)
        if num ==2:
            return random.randint(25,36)
        if num ==3:
            return random.randint(37,48)
    
    #print("Ssnksnknsksnknsn")
    # sys.exit(0)
    ccl = [(0,0),(0,1),(0,2),(1,0),(1,1),(1,2),(2,0),(2,1),(2,2)]
    tags = ['orange',"orange","darkgreen","crimson","orange","orange","crimson","crimson",'crimson']

    # labels2 = ["Low Vulnerability - Low Criticality","Low Criticality - Medium Vulnerability","Low Vulnerability - High Criticality",
    #         "Medium Vulnerability - Low Criticality","Medium Vulnerability - Medium Criticality","Medium Vulnerability - High Criticality",
    #         "High Vulnerability - Low Criticality","High Vulnerability - Medium Criticality","High Vulnerability - High Criticality"]

    # uncomment when shit fuck up
    labels2 = ["Low Vulnerability - Low Criticality","Low Vulnerability - Medium Criticality","Low Vulnerability - High Criticality",
    		"Medium Vulnerability - Low Criticality","Medium Vulnerability - Medium Criticality","Medium Vulnerability - High Criticality",
    		"High Vulnerability - Low Criticality","High Vulnerability - Medium Criticality","High Vulnerability - High Criticality"]
    kk_a = []
    kk_b = []
    labelwa = []
    kk_tags = []
    # data["Cluster"]=tags
    for i in zip(xb,xa):
        tb = ccl.index((i[0],i[1]))
        kk_tags.append(tags[tb])
        labelwa.append(labels2[tb])
        
    #     #print(i[0])
        x1 = x_1(i[0])
        x2 = y_1(i[1])
        kk_a.append(x1)
        kk_b.append(x2)

    data["Cluster"] = kk_tags
    c1 = []
    for m in labelwa:
        val = m.split(" - ")
        print(val,"############################33")
        print(val)
        val = ", ".join([val[1],val[0]])
        print(val,"sksks")
        # sys.exit(0)
        # print(val)
        c1.append(val)
        print(c1)
    labelwa = c1
    print(labelwa)
    df_x = pd.DataFrame({"x":kk_b,
                         "y":kk_a,
                         "emp_id":data["emp_id"].astype(str).tolist(),
                         "labels":c1,
                         "color":kk_tags})
    df_x['json'] = df_x.apply(lambda x: x.to_dict(), axis=1)
    # #print(df_x["json"].tolist())
    data.to_csv("jingalalal.csv")
    t = kk_tags
    return t,df_x["json"].tolist(),data




        


    # fig, ax = plt.subplots()
    # red_patch = mpatches.Patch(color='red', label='Medium Vulnerability-Low Criticality\nHigh Vulnerability-Low Criticality\nHigh Vulnerability-Medium Criticality\nHigh Vulnerability-High Criticality')
    # pink_patch = mpatches.Patch(color='lightpink', label="Medium Vulnerability-Medium Criticality")
    # yellow_patch = mpatches.Patch(color='Yellow', label="High Vulnerability-High Criticality")
    # wheat_patch = mpatches.Patch(color='Wheat', label="Low Vulnerability-Low Criticality")
    # pale_patch = mpatches.Patch(color='Palegreen', label="Low Vulnerability-Medium Criticality")
    # green_patch = mpatches.Patch(color='green', label="Low Vulnerability-High Criticality")
    # # plt.figure(figsize=(9,9))
    # classes = ['A', 'B', 'C',"D","E","F","G","H","I"]
    # plt.ylabel('vulnerability', fontsize=18)
    # plt.xlabel('criticality', fontsize=16)
    # # fig = plt.figure()
    # ax.grid(color='black', linestyle='solid')
    # scatter = ax.scatter(kk_b,kk_a, c=kk_tags, s=50, alpha=1,cmap=plt.cm.jet)

    # # plt.legend(handles=scatter.legend_elements(), labels=classes)
    # # plt.legend(loc ='best',handles=[red_patch],fontsize='small')
    # bbox_to_anchor=(1.1, 1.05)

    # tooltip = mpld3.plugins.PointLabelTooltip(scatter, labels=labelwa)
    # mpld3.plugins.connect(fig, tooltip)

    # # mpld3.show()
    # # plt.legend(bbox_to_anchor,loc ='upper right',handles=[red_patch,pink_patch,yellow_patch,wheat_patch,pale_patch,green_patch],fontsize='x-small')
    # # hola= mpld3.save_html(scatter,'2myfig.html',template_type='simple')

    # mpld3.save_html(fig,"./output/graph.html")
    
    
