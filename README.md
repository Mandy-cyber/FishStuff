# FishStuff
#### *Describing a dataset of fishy fish fish.*

![image](https://user-images.githubusercontent.com/67931161/141526269-4a6591ac-0201-46b5-8350-8cae3b97ff49.png)

## **BASIC OVERVIEW**
There are 159 rows (excluding the heading row) and 11 columns.

```python
df_fish = pd.read_csv('fish.csv') 
numOfRows = len(df_fish.axes[0]) #excludes first row
numOfCols = len(df_fish.axes[1])
print(numOfRows, numOfCols) #159, 11
```
<br>

COLUMN NAME | NUMERICAL/CATEGORICAL | DATA TYPE
------------ | --------------------- | -----------
**Species** | Categorical
**Avg Weight/g** | Numerical 
**Avg Length1 -vertical** | Numerical 
**Avg Length1 -diagonal** | Numerical
**Avg Length1 -cross** | Numerical
**Parish** | Categorical
**Environment Type** | Categorical  
**Body of Water** | Categorical
**Estimated Fish Pop. By Tonnes** | Numerical
**Fish Caught Pop. By Tonnes** | Numerical
**Catch Percentage* | Numerical


