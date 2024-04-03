#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing the pandas library and aliasing it as 'pd'.
import pandas as pd

# Importing the pyplot module from the matplotlib library.
import matplotlib.pyplot as plt


# In[2]:


# Reading the CSV file located at the specified path and storing the data in a DataFrame called 'df'.
df = pd.read_csv("C:\\Users\\RAHUL\\Downloads\\Dataset.csv")


# ### Level 3 task 2

# #### Identify the restaurants with the highest and lowest number of votes.

# In[3]:


# Sorting the DataFrame 'df' based on the values in the 'Votes' column in descending order.
# This creates a new DataFrame called 'df1' with restaurants sorted by votes.
df1 = df.sort_values(by='Votes', ascending=False)

# Selecting the first row of the sorted DataFrame 'df1', which corresponds to the restaurant with the highest number of votes.
# Storing this row in the variable 'highest_voted'.
highest_voted = df1.iloc[0]

# Printing information about the highest voted restaurant.
print("Highest voted restaurant is: ")
print(highest_voted)


# In[4]:


# Sorting the DataFrame 'df' based on the values in the 'Votes' column in ascending order.
# This creates a new DataFrame called 'df1' with restaurants sorted by votes.
df1 = df.sort_values(by='Votes')

# Selecting the first row of the sorted DataFrame 'df1', which corresponds to the restaurant with the lowest number of votes.
# Storing this row in the variable 'lowest_voted'.
lowest_voted = df1.iloc[0]

# Printing information about the lowest voted restaurant.
print("Lowest voted restaurant is: ")
print(lowest_voted)


# #### Analyze if there is a correlation between the number of votes and the rating of a restaurant.

# In[5]:


# Calculating the correlation between the 'Votes' column and the 'Aggregate rating' column in the DataFrame 'df'.
# The corr() function computes the Pearson correlation coefficient between two columns.
correlation = df['Votes'].corr(df['Aggregate rating'])

# Displaying the correlation coefficient.
correlation


# ### Level 3 task 3

# #### Analyze if there is a relationship between the price range and the availability of online delivery and table booking.
# 

# In[6]:


# Calculating the proportion of restaurants offering online delivery within each price range category.
# Grouping the DataFrame 'df' by the 'Price range' column and calculating value counts of 'Has Online delivery'.
# The normalize=True parameter calculates proportions instead of counts, and unstack() reshapes the result to a table-like structure.
# fillna(0) fills any missing values with 0.
price_vs_online = df.groupby('Price range')['Has Online delivery'].value_counts(normalize=True).unstack().fillna(0)

# Calculating the proportion of restaurants offering table booking within each price range category.
# Grouping the DataFrame 'df' by the 'Price range' column and calculating value counts of 'Has Table booking'.
# The normalize=True parameter calculates proportions instead of counts, and unstack() reshapes the result to a table-like structure.
# fillna(0) fills any missing values with 0.
price_vs_table = df.groupby('Price range')['Has Table booking'].value_counts(normalize=True).unstack().fillna(0)

# Printing the results.
print("Price Range vs Online Delivery:")
print(price_vs_online)
print("Price Range vs Table Booking:")
print(price_vs_table)


# #### Determine if higher-priced restaurants are more likely to offer these services.

# In[7]:


# Filtering the DataFrame 'df' to include only restaurants with a price range higher than the median price range.
higher_priced_restaurants = df[df['Price range'] > df['Price range'].median()]

# Calculating the proportion of higher-priced restaurants offering online delivery.
# The value_counts(normalize=True) function calculates proportions, and unstack() reshapes the result to a Series.
higher_price_vs_online = higher_priced_restaurants['Has Online delivery'].value_counts(normalize=True)

# Calculating the proportion of higher-priced restaurants offering table booking.
# The value_counts(normalize=True) function calculates proportions, and unstack() reshapes the result to a Series.
higher_price_vs_table = higher_priced_restaurants['Has Table booking'].value_counts(normalize=True)

# Printing the results.
print("Higher-Priced Restaurants vs Online Delivery:")
print(higher_price_vs_online)
print("Higher-Priced Restaurants vs Table Booking:")
print(higher_price_vs_table)


# In[ ]:




