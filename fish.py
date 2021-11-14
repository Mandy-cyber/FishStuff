#Yes this is a very original file name woooo
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import random
import time

df_fish = pd.read_csv('fish.csv')
df_fish = df_fish.replace(',','', regex=True)
df_fish['Estimated Fish Pop by Tonnes'] = df_fish['Estimated Fish Pop by Tonnes'].astype(float)
# print(df_fish.describe(include=[object]))
# print(df_fish.describe())

df_fish = df_fish['Body of Water']
print(df_fish.value_counts())

# listOfParishes = ['Hanover', 
#                 'Trelawny', 
#                 'Manchester', 
#                 'Portland', 
#                 'Saint Catherine', 
#                 'Clarendon', 
#                 'Kingston Parish', 
#                 'Saint James', 
#                 'Saint Thomas', 
#                 'Saint Andrew', 
#                 'Saint Ann',
#                 'Saint Elizabeth',
#                 'Saint Mary',
#                 'Westmoreland'
#                 ]

# df_fish = df_fish[['Parish', 'Catch Percentage']]
# avgCatchList = {}

# for parish in listOfParishes:
#     df_fish = df_fish.loc[df_fish['Parish'] == parish] #make a df with just the necessary parish values
#     sumCatch = df_fish['Catch Percentage'].sum() #sum of cell values
#     avgCatch = sumCatch / len(df_fish) #average catch percentage
#     avgCatchList[parish] = avgCatch #add to dict
#     df_fish = pd.read_csv('fish.csv') #reload the dataset afresh

# sortedCatchInfo = {} #new dict to use
# sortedKeys = sorted(avgCatchList, key=avgCatchList.get, reverse=True) #sort the key values of the old dict
# for w in sortedKeys:
#     sortedCatchInfo[w] = avgCatchList[w] #put those values into the new dict

# print(sortedCatchInfo)    

#-----------------------------------------------------------------------------------------------------------------#
#PLOTTING GRAPHS FOR NUMERICAL COLUMNS
# plt.rcParams["font.family"] = 'monospace'

# listOfColumns = ['Avg Weight/g',
#                 'Avg Length1 - vertical', 
#                 'Avg Length2 - diagonal', 
#                 'Avg Length3 - cross', 
#                 'Estimated Fish Pop by Tonnes',
#                 'Fish Caught Pop by Tonnes', 
#                 'Catch Percentage']
# listOfTitles = ["Average Weight (g) of a Fish",
#                 "Average Vertical Length (cm) of a Fish",
#                 "Average Diagonal Length (cm) of a Fish",
#                 "Average Cross Length (cm) of a Fish",
#                 'Estimated Fish Population (tonnes)',
#                 "Fish Caught Population (tonnes)",
#                 "Catch Percentage of Fish"]
# listOfColors = ["#700B97",
#                 "#B91646",
#                 "#89B5AF",
#                 "#FF5F7E",
#                 "#FBD148",
#                 "#FFABE1",
#                 "#6F69AC"]

# def createGraph(graphTitle, columnTitle, color):
#     fig, ax = plt.subplots(figsize=(6, 6))
#     ax.grid(color='grey', linestyle='-', linewidth=0.20)
#     ax.spines['top'].set_visible(False)
#     ax.spines['right'].set_visible(False)
#     ax.spines['left'].set_visible(False)
#     ax.yaxis.set_ticks_position('none')

#     ax.set(title=f"Graph showing Box Plot\n of The {graphTitle}")
#     boxplot = df_fish.boxplot(column=[columnTitle], color=f"{color}", notch=True)
#     plt.show()

# for x in range(len(listOfTitles)):
#     createGraph(listOfTitles[x], listOfColumns[x], listOfColors[x])

#-----------------------------------------------------------------------------------------------------------------#
# #PLOTTING GRAPHS FOR CATEGORICAL COLUMNS
# plt.rcParams["font.family"] = 'monospace'
# plt.rcParams['axes.autolimit_mode'] = 'round_numbers'

# listOfCatColumns1 = ['Species', 'Parish']
# listOfBarTitles = ["Graph Showing Frequency of Fish Species", "Graph Showing Frequency of Parishes"]
# c = ["#FFE3E3",
#     "#E4D8DC",
#     "#C9CCD5",
#     "#93B5C6",
#     "#96BAFF",
#     "#77ACF1",
#     "#0A81AB",
#     "#344FA1",
#     "#3F3697",
#     "#03256C",
#     "#001E6C",
#     "#002366",
#     "#170055",
#     "#261C2C"]


# listOfCatColumns2 = ['Environment Type', 'Body of Water']
# listOfPieTitles = ["Graph Showing Pie Chart of Environment Type Frequency", "Graph Showing Pie Chart of Body of Water Frequency"]

# # for x in listOfCatColumns1:
# #     data = df_fish[x].value_counts()
# #     data.plot(kind="bar")
# #     plt.show()

# def createBarChart(barTitle, barColTitle):
#     c.reverse()
#     fig, ax = plt.subplots(figsize=(8, 5))
#     ax.grid(color='grey', linestyle='-', linewidth=0.20)
#     ax.spines['top'].set_visible(False)
#     ax.spines['right'].set_visible(False)
#     ax.yaxis.set_ticks_position('none')

#     ax.set(title=f"{barTitle}")
#     data = df_fish[barColTitle].value_counts()
#     data.plot(kind="barh", color=c)
#     plt.locator_params(axis="x", integer=True)
#     plt.xlim(min(data),max(data))
#     plt.xticks(rotation=80)
#     plt.show()

# for x in range(len(listOfCatColumns1)):
#     createBarChart(listOfBarTitles[x], listOfCatColumns1[x])
    
# def createPieChart(pieTitle, pieColTitle): 
#     fig, ax = plt.subplots(figsize=(8, 5))
#     ax.set(title=f"{pieTitle}")
#     data = df_fish[pieColTitle].value_counts()
#     data.plot(kind="pie", autopct='%1.1f%%', colors=c, labels=["", "", "", ""])
#     plt.legend(labels=data.index)
#     plt.show()

# for x in range(len(listOfCatColumns2)):
#     createPieChart(listOfPieTitles[x], listOfCatColumns2[x])


