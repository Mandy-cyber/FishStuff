# <p align="center">Fish Stuff </p> 
## *<p align="center">Describing a dataset of :fish: </p>*

<img src="https://user-images.githubusercontent.com/67931161/141594058-f8656f0b-58c8-44dc-befb-9b29d807377d.gif" align="center">
<br><br>

# **TABLE OF CONTENTS**
1. [Intro](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#intro)
2. [The Data](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#the-data)
    - [Basic Overview](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#%EF%B8%8F-basic-overview)
    - [Statistics & Observations](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#-statistics--observations)
4. [Visualization](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#-visualization)
    - [Box Plots](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#numerical-columns-1)
    - [Pie & Bar Charts](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#categorical-columns-1)
6. [Key Observations](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#-key-observations)
7. [Conclusion](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#-conclusion)
<br>

# **INTRO**
The mission, that I have in fact accepted, is to describe a dataset containing data about 🐠. The description should include statistics, visualization, as well as something *interesting* and something *useful*. Having never 'described' a dataset before, it should be pretty entertaining to see what I find and uh.. how I find it. Alrighty, here we go.
<br>[**_(back to top)_**](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#table-of-contents)
<br><br>

# **THE DATA**
## ☂️ Basic Overview
The dataset takes the shape **(159, 11)** , meaning there are 159 rows (excluding the heading row) and 11 columns.

```python
import pandas as pd
import matplotlib as plt

df_fish = pd.read_csv('fish.csv') 
print(df_fish.shape)
```
With only 159 rows of data this is a considerably small dataset and hence any predictions derived from it would have low accuracy levels. This point will be furthered in the [Statistics & Observations](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#-statistics--observations) section.
<br>[**_(back to top)_**](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#table-of-contents)
<br>

### *Table Showing the Data Types of Each Column*

<img src="https://user-images.githubusercontent.com/67931161/141595161-f985b5de-b2c6-450a-aed9-cb68aa8e4e08.jpg" alt="List of column names highlighted either pink (signifying categorical data) or blue (numerical data)" align="right" height="400" width="315px"/>

COLUMN NAME | NUMERICAL/CATEGORICAL DATA | DATA TYPE
:------------: | :---------------------: | :-----------:
**Species** | Categorical | str
**Avg Weight/g** | Numerical | float
**Avg Length1 -vertical** | Numerical | float
**Avg Length2 -diagonal** | Numerical | float
**Avg Length3 -cross** | Numerical | float
**Parish** | Categorical | str
**Environment Type** | Categorical | str
**Body of Water** | Categorical | str
**Estimated Fish Pop. By Tonnes** | Numerical | float
**Fish Caught Pop. By Tonnes** | Numerical | int
**Catch Percentage** | Numerical | float

[**_(back to top)_**](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#table-of-contents)
<br><br>

## 🔢 Statistics & Observations
### *Numerical Columns*
For each numerical column, the following statistical data was found using `df_fish.describe()` :
<ul>
  <li><b>COUNT</b> - number of (non-NULL) values in column</li>
  <li><b>MEAN</b> - average</li>
  <li><b>STD</b> - standard deviation</li>
  <li><b>MIN</b> - smallest value</li>
  <li><b>25%</b> - lower percentile</li>
  <li><b>50%</b> - median</li>
  <li><b>75%</b> - upper percentile</li>
  <li><b>MAX</b> - largest value</li>
</ul>

<img src="https://user-images.githubusercontent.com/67931161/141653628-b0c1171d-2173-46d3-8ea6-91f9cc700be8.jpg" alt="table showing the statistical data of each numerical column"/>

The 'count' value remains constant throughout as there are no NULL values in any of the columns. It is also important to note that the standard deviation value for each column is large in relation to their mean values. This represents the broad spread of data within each column (the data values aren't very close to the mean), and this is further backed by the large interquartile ranges. In this scenario, the large standard deviation is not alarming as the dataset is simply showing recorded general observations across many different features. It would be [useful](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#-key-observations), however, to break the dataset down further and look at the mean for e.g the 'Catch Percentage', parish by parish. This could be used by fisherfolk to determine in which parish(es) they would be most likely to catch fish.

What the data also shows is an invalid weight. The 'min' value for the 'Avg Weight/g' was zero grams, which is, of course, not a valid weight (*weight > zero*). In addition, the large standard deviation values hints at the possibility of outliers, which will be confirmed through [box-plot visualizations](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#-visualization). In a scenario where the mean value is more significant, the trimmed mean (TrMean) could be calculated to reduce the impact of these outliers.

*N.B - Initially 'Estimated Fish Pop by Tonnes' was not being described with the other numerical columns, and was instead being considered categorical by pandas. At a second look of the dataset, I realized this was due to the presence of commas in some of the cell values. To fix this, the following was done:*
```python
df_fish = df_fish.replace(',','', regex=True)
df_fish['Estimated Fish Pop by Tonnes'] = df_fish['Estimated Fish Pop by Tonnes'].astype(float)
```
[**_(back to top)_**](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#table-of-contents)
<br>

---
<br>

### *Categorical Columns*
For each categorical column, the following statistical data was found using `df_fish.describe(include=[object])` :
<ul>
  <li><b>COUNT</b> - same as in numerical (constant value in this dataset)</li>
  <li><b>UNIQUE</b> - number of non-repeated (unique) values</li>
  <li><b>TOP</b> - the most common value (mode)</li>
  <li><b>FREQ</b> - the frequency of the mode</li>
</ul>
<img src="https://user-images.githubusercontent.com/67931161/141653691-80ea9857-0d8c-4fa9-a005-c08e72c2e195.jpg" alt="table showing the statistical data of each categorical column"/>

Once again, the count value remains the same across the columns for the reason mentioned earlier. Looking at the rest of the data, something that stood out was that the Perch species had the same frequency as Hanover in the dataset; however, after additional investigation it was seen that there were no Perch fish recorded in Hanover. The most Perch was found in St. Ann.

The data also shows that just over 50% of the recorded species were found in Saltwater environments, and roughly 55% of the recorded species were found in River bodies of water.

[**_(back to top)_**](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#table-of-contents)
<br><br><br>

## 🌈 Visualization
*For the visual learners, woooo.*
### *Numerical Columns*
<p align="center"><img src="https://user-images.githubusercontent.com/67931161/141651524-bd32cf06-095b-4744-b9da-5881054d2db7.gif" align="center" height="500" width="750"/></p>
<br>

The boxplots act as a visual representation of the prior mentioned statistical data, and were created using `matplotlib` :
```python
#listOfTitles, listOfColumns and listOfColors are not shown (to reduce space)
plt.rcParams["font.family"] = 'monospace'

def createGraph(graphTitle, columnTitle, color):
    fig, ax = plt.subplots(figsize=(6, 6))
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
```
<br>

COLUMN NAME | GRAPH | COLUMN NAME | GRAPH| 
:------------: | :---------------------: | :---------------------: | :---------------------: | 
**Avg Weight/g** | <img src="https://user-images.githubusercontent.com/67931161/141651644-7f368fa1-fd3f-4d36-96d1-360d7477871f.png" height="300" width="275"/> | **Avg Length2 -diagonal** | <img src="https://user-images.githubusercontent.com/67931161/141651939-a068129b-852c-4020-ac1f-6fd0ddebb408.png" height="300" width="275"/>
**Avg Length3 -vertical** | <img src="https://user-images.githubusercontent.com/67931161/141651864-37212aaf-eb5b-4174-bf6f-7a91f145099a.png" height="300" width="275"/> | **Avg Length1 -cross** | <img src="https://user-images.githubusercontent.com/67931161/141651940-5b79869e-d144-401e-a290-ef7ec58059c8.png" height="300" width="275"/> 
| **Fish Caught Pop. By Tonnes** | <img src="https://user-images.githubusercontent.com/67931161/141652003-1baebf8e-a3bb-40b5-9bb4-c5e1201f8409.png" height="300" width="275"/> | **Catch Percentage** | <img src="https://user-images.githubusercontent.com/67931161/141652196-bc50b234-3f0d-48fd-bb93-84b8667f7654.png" height="300" width="275"/>
**Estimated Fish Pop. By Tonnes** | <img src="https://user-images.githubusercontent.com/67931161/141654008-8f397670-b239-4d50-a113-e2327061ca63.png" height="300" width="275"/>

*N.B - The notches represent the confidence interval (default 95% is used) for the median values - truthfully, I just really liked how the notches looked, oops. Additionally, the circles represent suspected outliers. Five of the seven graphs have outliers, with four of the graphs having => 3 outliers, and the fifth graph having > 3 outliers.*
<br>[**_(back to top)_**](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#table-of-contents)
<br><br><br>

### *Categorical Columns*
<p align="center"><img src="https://user-images.githubusercontent.com/67931161/141657925-e1a3a7ba-2339-49ab-8a5a-8b0fae9954db.jpg" align="center" height="500" width="750"/></p>
<br>

The pie and bar charts act as visual representations of the prior mentioned statistical data, and were created using `matplotlib` :
```python
#again some lists are not shown in the code to save on space
#BAR CHARTS
def createBarChart(barTitle, barColTitle):
    c.reverse()
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.grid(color='grey', linestyle='-', linewidth=0.20)
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    ax.yaxis.set_ticks_position('none')

    ax.set(title=f"{barTitle}")
    data = df_fish[barColTitle].value_counts()
    data.plot(kind="barh", color=c)
    plt.locator_params(axis="x", integer=True)
    plt.xlim(min(data),max(data))
    plt.xticks(rotation=80)
    plt.show()

for x in range(len(listOfCatColumns1)):
    createBarChart(listOfBarTitles[x], listOfCatColumns1[x])

#PIE CHARTS
def createPieChart(pieTitle, pieColTitle): 
    fig, ax = plt.subplots(figsize=(8, 5))
    ax.set(title=f"{pieTitle}")
    data = df_fish[pieColTitle].value_counts()
    data.plot(kind="pie", autopct='%1.1f%%', colors=c, labels=["", "", "", ""])
    plt.legend(labels=data.index)
    plt.show()

for x in range(len(listOfCatColumns2)):
    createPieChart(listOfPieTitles[x], listOfCatColumns2[x])
```
<br>

COLUMN NAME | GRAPH | COLUMN NAME | GRAPH| 
:------------: | :---------------------: | :---------------------: | :---------------------: | 
**Species** | <img src="https://user-images.githubusercontent.com/67931161/141657560-baf7f994-6a45-4219-8a1e-d0af11298e71.png" height="275" width="400"/> | **Parish** | <img src="https://user-images.githubusercontent.com/67931161/141657570-7e5f2c67-eb47-48c7-9e88-0bf543de6d62.png" height="275" width="400"/> 
**Envrionment Type** | <img src="https://user-images.githubusercontent.com/67931161/141657578-b5059ad3-bc64-47d3-8246-2bc11b5b30a9.png" height="275" width="400"/> | **Body of Water** | <img src="https://user-images.githubusercontent.com/67931161/141657584-36f6722e-7488-4561-9ff6-40895be713c5.png" height="275" width="400"/> 

*N.B - You can click on one of the images to open it in a new tab and see it at a larger scale <3.*
<br><br><br>

## 🎣 *Key Observations*
### 1. Something Useful
As mentioned earlier, it would be useful
> to break the dataset down further and look at the mean for e.g the 'Catch Percentage', parish by parish.

This would primarily be useful for fisherfolk as it would help them to determine which parish(es) they would be most likely to catch fish. The below code was used,
```python
#the listOfParishes is not shown in order to save space
df_fish = df_fish[['Parish', 'Catch Percentage']]
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
```
<br>

*I would show the dictionary output in the terminal but it's rather ugly[^1], so I've formatted it properly to 3 s.f here,*
<br><br>
<img src="https://user-images.githubusercontent.com/67931161/141660418-1bbededc-0bc4-4a23-8c5b-e3b7e5e7dd60.jpg" alt="Welcome to Clarendon, home to a 0.137 Catch Percentage!" align="right" height="400" width="500px"/>


| Parish | Catch Percentage
| :-----: |:-----: |
**Clarendon** | 0.137
**Saint Andrew** | 0.131
**Saint Ann** | 0.126
**Saint James** | 0.118
**Manchester** | 0.114
**Saint Thomas** | 0.113
**Portland** | 0.113
**Saint Mary** | 0.111
**Hanover** | 0.105
**Westmoreland** | 0.101
**Trelawny** | 0.100
**Saint Catherine** | 0.096
**Kingston Parish** | 0.092
**Saint Elizabeth** | 0.088

[**_(back to top)_**](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#table-of-contents)

<br><br>

### 2. Something Interesting
Something interesting, at least to me, was
> just over 50% of the recorded species were found in Saltwater environments, and roughly 55% of the recorded species were found in River bodies of water.

Now, according to my ninth grade geography, 
* Saltwater = oceans, seas, and lagoons
* Freshwater = rivers, lakes, and other smaller bodies of water
* Estuartine =  that awkward space between a saltwater body of water, and a freshwater BoW
* Aquaculture = manmade bodies of water

Of course, there are cases where e.g lagoons have freshwater or lakes have saltwater, however, these scenarios sum to less than 1% of the global total of freshwater and saltwater[^2]. I am hence confident in calling these scenarios negligle, and therefore oceans, seas, and lagoons should host 50% of the recorded species (as mentioned earlier). Looking at the dataset, there are no ocean bodies of water, but there are sea sides and lagoons. Using the below code, confirmed by the pie chart, the frequency of each body of water was found:
```python 
df_fish = df_fish['Body of Water']
print(df_fish.value_counts())
```
<br>
<img src="https://user-images.githubusercontent.com/67931161/141657584-36f6722e-7488-4561-9ff6-40895be713c5.png" align="right" height="275" width="375"/> 

| Body of Water | Frequency
|:-----: | :-----: |
**River** | 88
**Sea Side** | 32
**Lagoon** | 28
**Aquaculture** | 11

This shows that 37.7% of all bodies of water in this dataset should, theoretically, be considered Saltwater environments. However, the actual figure of Saltwater environments seen in the pie chart is 51.6% - a figure *13.9%* greater. This, of course, begs the question  **"what percentage of Jamaican rivers have high salinity."** 

<img src="https://user-images.githubusercontent.com/67931161/141657578-b5059ad3-bc64-47d3-8246-2bc11b5b30a9.png" align="left" height="275" width="375"/>
<br>

The answer to which may or may not be in the depths of an 118 page document[^3].

[**_(back to top)_**](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#table-of-contents)

<br><br><br><br><br><br><br>

## 👋 *Conclusion*
Well this was fun - describing and analyzing a seemingly randomly-generated dataset of fish. To recount what was done, 
- [x] A basic overview of the data
- [x] Statistically describing the data
- [x] Visualizing the data
- [x] Observing something *interesting*
- [x] Observing something *useful*
- [x] Making this document a tad exciting

[**_(back to top)_**](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#table-of-contents)

<br><br>

[^1]: For those still curious, here is what it looked like.
[^2]: Sources for this information
    * [Total global saltwater and freshwater estimates](https://www.grida.no/resources/5808)
    * [What percentage of lakes are saltwater](https://www.sidmartinbio.org/what-percentage-of-lakes-are-salt-water/#:~:text=Saline%20lakes%20and%20inland,and%20streams%20(0.0001%20percent.))
[^3]: Document - [Water Resources Assessment of Jamaica](https://www.sam.usace.army.mil/Portals/46/docs/military/engineering/docs/WRA/Jamaica/Jamaica%20WRA%20-%20English.pdf)
