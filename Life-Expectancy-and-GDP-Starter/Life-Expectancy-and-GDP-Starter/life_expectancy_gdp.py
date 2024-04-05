#Importing the necessary files
import pandas as pd
import numpy
import matplotlib.pyplot as plt
import seaborn as sns

#Loading in the data
df = pd.read_csv("D:\\Coding Projects\\Python Projects\\Codecademy Projects\\Life-Expectancy-and-GDP-Starter\\Life-Expectancy-and-GDP-Starter\\all_data.csv")

#Here's the data for each country
chile_data = df[df["Country"] == "Chile"]
china_data = df[df["Country"] == "China"]
germany_data = df[df["Country"] == "Germany"]
mexico_data = df[df["Country"] == "Mexico"]
usa_data = df[df["Country"] == "United States of America"]
zimbabwe_data = df[df["Country"] == "Zimbabwe"]

#Print out columns of the dataframe
#print(df.columns)
#print(df["Country"])

#Scatterplot for Chile
sns.scatterplot(data=chile_data, x=chile_data["GDP"], y=chile_data["Life expectancy at birth (years)"])
plt.title("Chile")
plt.xlabel("GDP (US Dollars)")
plt.ylabel("Life expectancy at birth (years)")
plt.figure()

#Scatterplot for China
sns.scatterplot(data=china_data, x=china_data["GDP"], y=china_data["Life expectancy at birth (years)"])
plt.title("China")
plt.xlabel("GDP (US Dollars)")
plt.ylabel("Life expectancy at birth (years)")
plt.figure()

#Scatterplot for Germany
sns.scatterplot(data=germany_data, x=germany_data["GDP"], y=germany_data["Life expectancy at birth (years)"])
plt.title("Germany")
plt.xlabel("GDP (US Dollars)")
plt.ylabel("Life expectancy at birth (years)")
plt.figure()

#Scatterplot for Mexico
sns.scatterplot(data=mexico_data, x=mexico_data["GDP"], y=mexico_data["Life expectancy at birth (years)"])
plt.title("Mexico")
plt.xlabel("GDP (US Dollars)")
plt.ylabel("Life expectancy at birth (years)")
plt.figure()

#Scatterplot for America
sns.scatterplot(data=usa_data, x=usa_data["GDP"], y=usa_data["Life expectancy at birth (years)"])
plt.title("United States")
plt.xlabel("GDP (US Dollars)")
plt.ylabel("Life expectancy at birth (years)")
plt.figure()

#Scatterplot for Zimbabwe
sns.scatterplot(data=zimbabwe_data, x=zimbabwe_data["GDP"], y=zimbabwe_data["Life expectancy at birth (years)"])
plt.title("Zimbabwe")
plt.xlabel("GDP (US Dollars)")
plt.ylabel("Life expectancy at birth (years)")
plt.show()
plt.clf()