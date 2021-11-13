# <p align="center">Fish Stuff </p> 
## *<p align="center">Describing a dataset of :fish: </p>*

<img src="https://user-images.githubusercontent.com/67931161/141594058-f8656f0b-58c8-44dc-befb-9b29d807377d.gif" align="center">
<br><br>

# **THE PROBLEM**
The problem shall go here</p>
<br><br>

# **THE DATA**
## ☂️ Basic Overview
The dataset takes the shape **(159, 11)** , meaning there are 159 rows (excluding the heading row) and 11 columns.

```python
import pandas as pd
import matplotlib as plt
import numpy as np

df_fish = pd.read_csv('fish.csv') 
print(df_fish.shape)
```
With only 159 rows of data this is a considerably small dataset and hence any predictions derived from it would have low accuracy levels. This point will be furthered in the "Statistics & Observations" section.
<br>

### *Table Showing the Data Types of Each Column*

<img src="https://user-images.githubusercontent.com/67931161/141595161-f985b5de-b2c6-450a-aed9-cb68aa8e4e08.jpg" alt="List of column names highlighted either pink (signifying categorical data) or blue (numerical data)" align="right" height="400" width="315px"/>

COLUMN NAME | NUMERICAL/CATEGORICAL DATA | DATA TYPE
:------------: | :---------------------: | :-----------:
**Species** | Categorical | str
**Avg Weight/g** | Numerical | float
**Avg Length1 -vertical** | Numerical | float
**Avg Length1 -diagonal** | Numerical | float
**Avg Length1 -cross** | Numerical | float
**Parish** | Categorical | str
**Environment Type** | Categorical | str
**Body of Water** | Categorical | str
**Estimated Fish Pop. By Tonnes** | Numerical | float
**Fish Caught Pop. By Tonnes** | Numerical | int
**Catch Percentage** | Numerical | float
<br>

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
<img src="https://user-images.githubusercontent.com/67931161/141595982-9d52fecb-3a53-48a3-bbff-ec2e1734ce38.jpg" alt="table showing the statistical data of each numerical column"/>
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
<img src="https://user-images.githubusercontent.com/67931161/141597598-9739d299-bd33-40ce-beac-c43dfa5bf3c7.jpg" alt="table showing the statistical data of each categorical column"/>
<br><br>

## 🌈 Visualization
*For the visual learners, woo*
<br><br>

## 👩‍🌾 *Key Observations*
When analyzing the data there were two key observations,
SOMETHING INTERESTING | SOMETHING USEFUL |
:------------: | :---------------------: |
this is something interesting | this is something useful
