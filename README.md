# <p align="center">Fish Stuff </p> 
## *<p align="center">Describing a dataset of :fish: </p>*

<img src="https://user-images.githubusercontent.com/67931161/141594058-f8656f0b-58c8-44dc-befb-9b29d807377d.gif" align="center">
<br><br>

# **TABLE OF CONTENTS**
1. [The Problem](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#the-problem)
2. [The Data](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#the-data)
    - [Basic Overview](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#%EF%B8%8F-basic-overview)
    - [Statistics & Observations](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#-statistics--observations)
4. [Visualization](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#-visualization)
5. [Key Observations](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#-key-observations)
<br>

# **THE PROBLEM**
The problem shall go here</p>
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

The 'count' value remains constant throughout as there are no NULL values in any of the columns. It is also important to note that the standard deviation value for each column is large in relation to their mean values. This represents the broad spread of data within each column (the data values aren't very close to the mean), and this is further backed by the large interquartile ranges. In this scenario, the large standard deviation is not alarming as the dataset is simply showing recorded general observations across many different features. It would be [useful](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#-key-observations), however, to break the dataset down further and look at the standard deviation for e.g the 'Catch Percentage', parish by parish. This could be used by farmers to determine in which parish(es) they would be most likely to catch fish.

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
<p align="center"><img src="" align="center" height="500" width="750"/></p>
<br>

The pie charts act as a visual representation of the prior mentioned statistical data, and were created using `matplotlib` :
```python

```
<br>

COLUMN NAME | GRAPH | COLUMN NAME | GRAPH| 
:------------: | :---------------------: | :---------------------: | :---------------------: | 
**Species** | <img src="" height="300" width="275"/> | **Parish** | <img src="" height="300" width="275"/> 
**Envrionment Type** | <img src="" height="300" width="275"/> | **Body of Water** | <img src="" height="300" width="275"/> 

<br><br><br>


## 👩‍🌾 *Key Observations*
When analyzing the data there were two key observations,
SOMETHING INTERESTING | SOMETHING USEFUL |
:------------: | :---------------------: |
this is something interesting | this is something useful

[**_(back to top)_**](https://github.com/Mandy-cyber/FishStuff/blob/main/README.md#table-of-contents)
