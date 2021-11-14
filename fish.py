#Yes this is a very original file name woooo
#Comment out what is not in use or else you'll run into issues ofc
import pandas as pd
import matplotlib.pyplot as plt
#Don't believe I used these three imports but just in case I did, here they are
import numpy as np 
import random
import time

#LOADING THE DATASET
df_fish = pd.read_csv('fish.csv')

#-----------------------------------------------------------------------------------------------------------------#
#FIXING THE ESTIMATED FISH POP ISSUE (changing str-->float)
df_fish = df_fish.replace(',','', regex=True)
df_fish['Estimated Fish Pop by Tonnes'] = df_fish['Estimated Fish Pop by Tonnes'].astype(float)

#-----------------------------------------------------------------------------------------------------------------#
#DESCRIBING THE DATASET
print(df_fish.describe())
print(df_fish.describe(include=[object]))

#-----------------------------------------------------------------------------------------------------------------#
#GETTING BODY OF WATER FREQUENCIES
df_fish = df_fish['Body of Water']
print(df_fish.value_counts())

#-----------------------------------------------------------------------------------------------------------------#
#CALCULATING THE AVERAGE CATCH RATE PARISH BY PARISH
listOfParishes = ['Hanover', 
                'Trelawny', 
                'Manchester', 
                'Portland', 
                'Saint Catherine', 
                'Clarendon', 
                'Kingston Parish', 
                'Saint James', 
                'Saint Thomas', 
                'Saint Andrew', 
                'Saint Ann',
                'Saint Elizabeth',
                'Saint Mary',
                'Westmoreland'
                ]

df_fish = df_fish[['Parish', 'Catch Percentage']] #make df with the only two columns necessary
avgCatchList = {}

for parish in listOfParishes:
    df_fish = df_fish.loc[df_fish['Parish'] == parish] #make a df with just the necessary parish values
    sumCatch = df_fish['Catch Percentage'].sum() #sum of cell values
    avgCatch = sumCatch / len(df_fish) #average catch percentage
    avgCatchList[parish] = avgCatch #add to dict
    df_fish = pd.read_csv('fish.csv') #reload the dataset afresh

sortedCatchInfo = {} #new dict to use
sortedKeys = sorted(avgCatchList, key=avgCatchList.get, reverse=True) #sort the key values of the old dict
for w in sortedKeys:
    sortedCatchInfo[w] = avgCatchList[w] #put those values into the new dict

print(sortedCatchInfo)    

#-----------------------------------------------------------------------------------------------------------------#
#PLOTTING GRAPHS FOR NUMERICAL COLUMNS
listOfColumns = ['Avg Weight/g',
                'Avg Length1 - vertical', 
                'Avg Length2 - diagonal', 
                'Avg Length3 - cross', 
                'Estimated Fish Pop by Tonnes',
                'Fish Caught Pop by Tonnes', 
                'Catch Percentage']
listOfTitles = ["Average Weight (g) of a Fish",
                "Average Vertical Length (cm) of a Fish",
                "Average Diagonal Length (cm) of a Fish",
                "Average Cross Length (cm) of a Fish",
                'Estimated Fish Population (tonnes)',
                "Fish Caught Population (tonnes)",
                "Catch Percentage of Fish"]
listOfColors = ["#700B97",
                "#B91646",
                "#89B5AF",
                "#FF5F7E",
                "#FBD148",
                "#FFABE1",
                "#6F69AC"] 

plt.rcParams["font.family"] = 'monospace' #changing font

def createGraph(graphTitle, columnTitle, color):
    fig, ax = plt.subplots(figsize=(6, 6))
    #Just to make things look a little bit nicer
    ax.grid(color='grey', linestyle='-', linewidth=0.20)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.spines['left'].set_visible(False)
    ax.yaxis.set_ticks_position('none')

    ax.set(title=f"Graph showing Box Plot\n of The {graphTitle}")
    boxplot = df_fish.boxplot(column=[columnTitle], color=f"{color}", notch=True)
    plt.show()

for x in range(len(listOfTitles)):
    createGraph(listOfTitles[x], listOfColumns[x], listOfColors[x])

#-----------------------------------------------------------------------------------------------------------------#
#PLOTTING GRAPHS FOR CATEGORICAL COLUMNS
listOfCatColumns1 = ['Species', 'Parish']
listOfBarTitles = ["Graph Showing Frequency of Fish Species", "Graph Showing Frequency of Parishes"]
c = ["#FFE3E3",
    "#E4D8DC",
    "#C9CCD5",
    "#93B5C6",
    "#96BAFF",
    "#77ACF1",
    "#0A81AB",
    "#344FA1",
    "#3F3697",
    "#03256C",
    "#001E6C",
    "#002366",
    "#170055",
    "#261C2C"] #do you know how much time I wasted choosing these colors? wow

listOfCatColumns2 = ['Environment Type', 'Body of Water']
listOfPieTitles = ["Graph Showing Pie Chart of Environment Type Frequency", "Graph Showing Pie Chart of Body of Water Frequency"]

plt.rcParams["font.family"] = 'monospace'
plt.rcParams['axes.autolimit_mode'] = 'round_numbers'

def createBarChart(barTitle, barColTitle):
    c.reverse() #reverse order of colors so starts from lightest
    fig, ax = plt.subplots(figsize=(8, 5))
    #Making things pretty again
    ax.grid(color='grey', linestyle='-', linewidth=0.20)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('none')

    ax.set(title=f"{barTitle}")
    data = df_fish[barColTitle].value_counts() #data will be the frequency of each value in the column
    data.plot(kind="barh", color=c) #'barh' makes it a horizontal bar chart
    plt.locator_params(axis="x", integer=True) #make sure x axis values are integers
    plt.xlim(min(data),max(data)) #show the min and max values from the data as the min and max x axis values
    plt.xticks(rotation=80) #rotate x-axis labels just for funsies
    plt.show()

for x in range(len(listOfCatColumns1)):
    createBarChart(listOfBarTitles[x], listOfCatColumns1[x])
    
def createPieChart(pieTitle, pieColTitle): 
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set(title=f"{pieTitle}")
    data = df_fish[pieColTitle].value_counts()
    data.plot(kind="pie", autopct='%1.1f%%', colors=c, labels=["", "", "", ""]) #generate a pie chart, show percentages, get colors from list, replace labels with blank spaces
    plt.legend(labels=data.index) #create a legend (which i think is aka a key)
    plt.show()

for x in range(len(listOfCatColumns2)):
    createPieChart(listOfPieTitles[x], listOfCatColumns2[x])


