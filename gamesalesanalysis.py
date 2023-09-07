# -*- coding: utf-8 -*-
"""GameSalesAnalysis.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1AQp1LNFSLEMws1RmlcKZZ7SPPrwfSD98

#Comparison of video game sales and GDP per resident in the world

The topic of this paper is the impact of GDP on video game sales in certain parts of the world. Main
the idea is to monitor GDP growth or decline depending on the year and place of sale, and to conclude whether and how much it affects
GDP affects game sales. The main sales areas that will be studied are the North
America and Japan (there is also data for Europe, but Europe has too many countries to
could conclude something). The assumption is that GDP affects sales, which I will try to prove.
I will also conclude which are the most popular video game genres, platforms and publishers.

1. Collection of data sources

The data was collected through the following sources:

Video Game Sales: https://www.kaggle.com/datasets/gregorut/videogamesales?resource=download

GDP by selected country: https://data.oecd.org/gdp/gross-domestic-product-gdp.htm#indicator-chart

The first dataset was downloaded from the Kaggle site. There are exactly 16,598 games in this dataset.
The following information can be found for each game:
* Rank – the place of the game by the total number of sales. First place is the best-selling game
looking at total sales worldwide.
* Name – name of the game
* Platform – the game release platform
* Year – the year the game was released
* Genre – genre of the game
* Publisher – publishing house of the game
* NA_Sales – sales in North America (in millions)
* EU_Sales – sales in Europe (in millions)
* JP_Sales – sales in Japan (in millions)
* Other_sales – sales in other parts of the world (in millions)
* Global_sales – total sales in the world

Second dataset is available at data.oecd.org. On this page it is possible to select a range
the year in which I want to take over GDP. The oldest game from the first data set is from 1980, and the newest from
2010 (there are also more recent ones, but in too few numbers, so these games will not be taken into account). Cause of
for this reason I will choose the range of years from 1980 to 2010
The essential data from this set for analysis are:
* Location – abbreviation of the country
* Indicator – indication that it is GDP ("gross domestic product" in English, GDP)
* Measure – dollar per capita label
* Time - year
* Value – GDP value

## 2. Cleaning data
"""

from google.colab import drive
drive.mount('/content/drive')

# importing libraries
import pandas as pd
import matplotlib.pyplot as plt

# reading first dataframe - vgsales.csv
df1 = pd.read_csv("/content/drive/MyDrive/vgsales.csv")

# reading second dataframe - DP_LIVE_01062022142735936.csv
df2 = pd.read_csv("/content/drive/MyDrive/DP_LIVE_01062022142735936.csv")

"""## Cleaning first dataframe"""

# Checking how many games have values that are null
 df1.isnull().sum()

"""271 video games don't have a year record, so I'll discard those records (actually I'll take all values ​​where there are years)"""

# Creating new dataframe
df11 = df1[df1['Year'].notna()]

# Checking null values again
df11.isnull().sum()

"""There are 36 games left without a record of who is the publisher, but that is not the focus of this seminar, so I will keep those records"""

df11.info()

"""Taking games from 1980 to 2010"""

df11['Year'] = df11['Year'].astype(int, errors = 'raise')

first_dataframe = df11[ (df11["Year"] > 1979) & (df11["Year"] < 2011) ]

"""# Cleaning second dataframe"""

df2

for col in df2.columns:
    print(col)

"""Column division by commas"""

df2[['Location', 'Indicator', 'Subject', 'Measure', 'Frequency', 'Time', 'Value', 'Flag Codes']] = df2['LOCATION,"INDICATOR","SUBJECT","MEASURE","FREQUENCY","TIME","Value","Flag Codes"'].str.split(',', expand=True)

"""Deleting frist column"""

df22 = df2.drop('LOCATION,"INDICATOR","SUBJECT","MEASURE","FREQUENCY","TIME","Value","Flag Codes"', axis=1)

"""It is necessary to remove the quotation marks from the Time field, so that it can join the datasets by that field"""

df22 = df22.replace('"', '', regex=True)

df22['Time'] = df22['Time'].astype(int, errors = 'raise')

df22['Value'] = df22['Value'].astype(float, errors = 'raise')

df22

df22.rename(columns = {'Time':'Year'}, inplace = True)

"""At the center of the research are North America (I will take the 3 largest countries; USA, Canada and Mexico) and Japan"""

df22 = df22[ (df22["Location"] == "MEX") | (df22["Location"] == "USA")  | (df22["Location"] == "CAN" ) | (df22["Location"] == "JPN")]

"""I leave the location, time and GDP value"""

second_dataframe = df22.drop(['Indicator', 'Subject', 'Measure', 'Frequency', 'Flag Codes'], axis = 1)

second_dataframeJPN = second_dataframe[ second_dataframe["Location"] == "JPN"]

second_dataframeCAN = second_dataframe[ second_dataframe["Location"] == "CAN"]

second_dataframeUSA = second_dataframe[ second_dataframe["Location"] == "USA"]

second_dataframeMEX = second_dataframe[ second_dataframe["Location"] == "MEX"]

"""# Merging all dataframes

Adding Canada's GDP
"""

first_dataframe = first_dataframe.merge(second_dataframeCAN, on = "Year")

first_dataframe = first_dataframe.drop(['Location'], axis = 1)

first_dataframe.rename(columns = {'Value':'GDP_Japan'}, inplace = True)

first_dataframe

"""Adding Japan's GDP"""

first_dataframe = first_dataframe.merge(second_dataframeJPN, on = "Year")

first_dataframe = first_dataframe.drop(['Location'], axis = 1)

first_dataframe.rename(columns = {'Value':'GDP_Canada'}, inplace = True)

"""Adding USA's GDP"""

first_dataframe = first_dataframe.merge(second_dataframeUSA, on = "Year")

first_dataframe = first_dataframe.drop(['Location'], axis = 1)

first_dataframe.rename(columns = {'Value':'GDP_USA'}, inplace = True)

"""Adding Mexico's GDP"""

first_dataframe = first_dataframe.merge(second_dataframeMEX, on = "Year")

first_dataframe = first_dataframe.drop(['Location'], axis = 1)

first_dataframe.rename(columns = {'Value':'GDP_Mexico'}, inplace = True)

Merged_dataframe = first_dataframe

Merged_dataframe

"""Visualisations

The amount of games under the dataset, the games are relatively well balanced
"""

sumByPlatform = Merged_dataframe.groupby(["Platform"], sort=True).count()
top10 = sumByPlatform.sort_values("Rank",  ascending= False).head(10)
top10.iloc[:,1].plot.pie(subplots= True)
plt.ylabel("Platform")
plt.title("Amount of games by platform")

"""1. Top 10 most sold games"""

maxbyPlatform = Merged_dataframe.groupby(["Name"], sort=False)['Global_Sales'].max()
sortedMax = maxbyPlatform.sort_values(ascending = False)
top10 = sortedMax.head(10)
top10.plot.barh();
plt.title("Top 10 games")
plt.ylabel("Name")
plt.xlabel("Sales in millions")
plt.grid(linewidth = 0.4)

"""Most sold game is Wii Sports

2. Most popular platforms
"""

sumPlatforms = Merged_dataframe.groupby(["Platform"], sort=False)['Global_Sales'].sum()
sortedSum = sumPlatforms.sort_values(ascending = False)
sorted7 = sortedSum.head(7)
sorted7.plot.bar()
plt.title("Platforms with most selling")
plt.ylabel("Selling in millions")
plt.xlabel("Platform")
plt.grid(linewidth = 0.4)

"""The best selling games are Playstation 2 games with even more than 1200 million in total sales.

3. Most popular genres
"""

sumaGenre = Merged_dataframe.groupby(["Genre"], sort=False)['Global_Sales'].sum()
sortedGenre = sumaGenre.sort_values(ascending = False)
sorted7 = sortedGenre.head(7)
sorted7.plot.barh()
plt.title("Sales in millions")
plt.ylabel("Genres with most selling")
plt.xlabel("Sales in millions")
plt.grid(linewidth = 0.4)

"""Action games are by far the best sellers, followed by sports games and platformers

4. Top 10 publishers in the world
"""

sumPublisher = Merged_dataframe.groupby(["Publisher"], sort=False)['Global_Sales'].sum()
sortedPublisher = sumPublisher.sort_values(ascending = False)
sorted10 = sortedPublisher.head(10)
sorted10.plot.barh()
plt.title("Sales in millions")
plt.ylabel("Total sales of all publishers")
plt.xlabel("Publisher")
plt.grid(linewidth = 0.4)

"""Nintendo leads convincingly.

5. Comparison of sales in North America and Japan by year
"""

salesNA = Merged_dataframe.groupby(["Year"], sort = True)['NA_Sales'].sum()
salesJAP = Merged_dataframe.groupby(["Year"], sort = True)['JP_Sales'].sum()

fig, ax = plt.subplots()

ax.plot(salesNA, color = 'green', label = "Sales in North America")
ax.plot(salesJAP, color = 'red', label = "Sales in Japan")
ax.legend(loc = 'upper left')
plt.grid(linewidth = 0.4)
plt.show()

"""Visible decline after 2007, especially in North America, in Japan there is no visible decline, but there is no increase either.

6.  Comparison of GDP of all analyzed countries
"""

GDP_byYearJapan = Merged_dataframe.groupby(["Year"], sort = True)['GDP_Japan'].max()
GDP_byYearUSA = Merged_dataframe.groupby(["Year"], sort = True)['GDP_USA'].max()
GDP_byYearCanada = Merged_dataframe.groupby(["Year"], sort = True)['GDP_Canada'].max()
GDP_byYearMexico = Merged_dataframe.groupby(["Year"], sort = True)['GDP_Mexico'].max()

fig, ax = plt.subplots()

ax.plot(GDP_byYearJapan, color = 'green', label = "GDP Japan")
ax.plot(GDP_byYearUSA, color = 'blue', label = "GDP USA")
ax.plot(GDP_byYearCanada, color = 'red', label = "GDP Canada")
ax.plot(GDP_byYearMexico, color = 'orange', label = "GDP Mexico")
ax.legend(loc = 'upper left')
plt.title("Comparison of GDP")
plt.grid(linewidth = 0.4)
plt.show()

"""Also a visible decline after ~ 2007. Assumption - World financial crisis after 2007

7. How much did the crisis affect sales in Europe?
"""

salesEU = Merged_dataframe.groupby(["Year"], sort = True)['EU_Sales'].sum()

salesEU.plot()
plt.ylabel("Sales in millions")
plt.xlabel("Year")
plt.title("Sales in Europe")
plt.grid(linewidth = 0.4)

"""A slight decline is visible after 2009

8. Comparison of Europe with North America and Japan
"""

fig, ax = plt.subplots()

ax.plot(salesNA, color = 'green', label = "Sales in North America")
ax.plot(salesJAP, color = 'red', label = "Sales in Japan")
ax.plot(salesEU, color = 'blue', label = "Sales in Europe", linestyle = ":")
ax.legend(loc = 'upper left')
plt.grid(linewidth = 0.4)
plt.show()

"""By far the most games were sold in North America, almost twice as much in Europe and the least in Japan

9. How does the rest of the world compare to the 3 main areas?
"""

salesRest = Merged_dataframe.groupby(["Year"], sort = True)['Other_Sales'].sum()

fig, ax = plt.subplots()

ax.plot(salesNA, color = 'green', label = "Sales in North America")
ax.plot(salesJAP, color = 'red', label = "Prodaja u Japanu")
ax.plot(salesEU, color = 'orange', label = "Prodaja u Europi")
ax.plot(salesRest, color = "blue", label ="Prodaja u ostatku svijeta", linestyle = ":")
ax.legend(loc = 'upper left')
plt.grid(linewidth = 0.4)
plt.show()

"""Until 1995 it was almost negligible, after 2005 it was even higher than in Japan"""