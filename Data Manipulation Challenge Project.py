#!/usr/bin/env python
# coding: utf-8

# In[1]:


#First, let's import the pandas module so we can manipulate our data.
import pandas as pd

#This line helps us display the full contents of a column.
pd.set_option('display.max_colwidth', -1)

#Step 2
#Let's load in the dataframe.
df = pd.read_csv('jeopardy.csv')

#We'll need to print out the head and columns to visualize our data.
print(df.head(20))
print(df.columns)

#It looks like there's an unnecesary space at the start of some columns. Let's fix it.
df = df.rename(columns={' Air Date': 'Air Date', ' Round': 'Round', ' Category': 'Category', ' Value': 'Value', ' Question': 'Question', ' Answer': 'Answer'})

#We'll need to print out the columns again to make sure nothing's wrong.
print(df.columns)

#Step 3
#Now let's filter out the words as told in Step 3.
def filter_dataset(data, words):
  filtered_data = df[df['Question'].apply(lambda x: all(word in x for word in words))]
  return filtered_data

#Step 4
#Let's see if our function is working properly.
print(filter_dataset(df, 'viking'))

#Step 5
#Before converting, we need to check for non-numeric symbols
print(df['Value'])

#Let's remove non-numeric symbols and whitespace to prevent our code from crashing.
df['Value'] = [value.replace('$', '') for value in df['Value']]
df['Value'] = [value.replace(',', '') for value in df['Value']]
df['Value'] = [value.replace(' ', '') for value in df['Value']]
df['Value'] = pd.to_numeric(df['Value'], errors='coerce')
df['Value'].dropna(inplace=True)

#Let's print the code again to make sure there's nothing wrong.
print(df['Value'])

#We can convert now.
df['Value'] = df['Value'].astype(float)

#We'll need to print out our values to make sure.
print(df['Value'])

#Step 6
#Now let's write our unique answers function.
def count_unique_answers(data):
  return data['Answer'].value_counts()

#Once again, let's test our function to see if it'll work.
print(count_unique_answers(df))


# In[ ]:




