#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Importing the pandas library and aliasing it as 'pd'.
import pandas as pd

# Importing the pyplot module from the matplotlib library and aliasing it as 'plt'.
import matplotlib.pyplot as plt


# In[2]:


# Reading the CSV file located at the specified path and storing the data in a DataFrame called 'df'.
df = pd.read_csv("C:\\Users\\RAHUL\\Downloads\\Dataset.csv")

# Displaying the DataFrame 'df' to view its contents.
df


# ### Level 1 task 1

# #### Determine the top three most common cuisines in the dataset.

# In[3]:


# Calculating the count of each unique cuisine in the 'Cuisines' column of the DataFrame 'df'.
# The value_counts() function returns a Series containing counts of unique values, sorted in descending order by default.
# The sort parameter is set to True to sort the counts, and ascending parameter is set to False to sort in descending order.
total_cuisines = df['Cuisines'].value_counts(sort=True, ascending=False)

# Displaying the Series 'total_cuisines' containing the count of each unique cuisine.
total_cuisines


# In[4]:


# Selecting the top three cuisines with the highest counts from the 'total_cuisines' Series.
# The head() function is used to select the first n rows (default is 5) of the Series.
# In this case, we specify 3 to get the top three cuisines.
top_three = total_cuisines.head(3)

# Displaying the top three cuisines with the highest counts.
top_three


# #### Calculate the percentage of restaurants that serve each of the top cuisines.

# In[5]:


# Calculating the total number of restaurants in the DataFrame 'df'.
# The len() function returns the number of rows in the DataFrame, which corresponds to the total number of restaurants.
total_restaurants = len(df)

# Displaying the total number of restaurants.
total_restaurants


# In[6]:


percentage=(top_three/total_restaurants)*100


# In[7]:


percentage


# ### Level 1 task 2

# #### Identify the city with the highest number of restaurants in the dataset.

# In[6]:


# Grouping the DataFrame 'df' by the "City" column and counting the number of restaurants in each city.
# The groupby() function is used to group the DataFrame by the "City" column.
# The count() function is then applied to the "Restaurant Name" column within each group to count the number of restaurants.
restaurant_city = df.groupby("City")["Restaurant Name"].count()

# Displaying the number of restaurants in each city.
restaurant_city


# In[7]:


# Finding the city with the highest restaurant count.
# The idxmax() function returns the index (i.e., the city name) corresponding to the maximum value in the 'restaurant_city' Series.
# This effectively gives us the city with the highest restaurant count.
city_high_restaurant_count = restaurant_city.idxmax()

# Displaying the city with the highest restaurant count.
city_high_restaurant_count


# In[8]:


# Finding the maximum number of restaurants in any city.
# The max() function returns the maximum value in the 'restaurant_city' Series, which represents the highest restaurant count among all cities.
no_of_restaurant = restaurant_city.max()

# Displaying the maximum number of restaurants.
no_of_restaurant


# In[11]:


print("The city with highest number of restaurants is" ,city_high_restaurant_count, "and it has", no_of_restaurant, "restaurants" )


# #### Calculate the average rating for restaurants in each city.

# In[9]:


# Calculating the average aggregate rating for restaurants in each city.
# The groupby() function is used to group the DataFrame 'df' by the "City" column.
# Then, the mean() function is applied to the "Aggregate rating" column within each group to calculate the average rating.
avg_rating = df.groupby("City")["Aggregate rating"].mean()

# Displaying the average aggregate rating for restaurants in each city.
avg_rating


# #### Determine the city with the highest average rating.
# 

# In[10]:


# Finding the city with the highest average aggregate rating.
# The idxmax() function returns the index (i.e., the city name) corresponding to the maximum value in the 'avg_rating' Series.
# This effectively gives us the city with the highest average aggregate rating among all cities.
city_with_highest_rating = avg_rating.idxmax()

# Displaying the city with the highest average aggregate rating.
city_with_highest_rating


# In[11]:


# Finding the highest average aggregate rating among all cities.
# The max() function returns the maximum value in the 'avg_rating' Series, which represents the highest average rating among all cities.
highest_rating = avg_rating.max()

# Displaying the highest average aggregate rating.
highest_rating


# In[15]:


print("The city with highest avg rating is", city_with_highest_rating, "and the rating is", higest_rating)


# ### Level 1 task 3

# #### Create a histogram or bar chart to visualize the distribution of price ranges among the restaurants.

# In[12]:


# Counting the occurrences of each price range in the "Price range" column of the DataFrame 'df'.
# The value_counts() function returns a Series with counts of unique values in descending order by default.
# The sort_index() function is then used to sort the counts by index (i.e., by price range).
price_ranges = df["Price range"].value_counts().sort_index()

# Displaying the counts of restaurants for each price range.
price_ranges


# In[13]:


# Creating a bar plot to visualize the distribution of price ranges among the restaurants.
# The plt.bar() function is used to create a bar plot.
# The price_ranges.index contains the price ranges (x-axis), and price_ranges.values contains the corresponding counts (y-axis).
# The color parameter is set to 'orange' to specify the color of the bars.
plt.bar(price_ranges.index, price_ranges.values, color='orange')

# Adding a title to the plot.
plt.title("Distribution of price ranges among the restaurants.")

# Adding a label to the x-axis.
plt.xlabel("Price")

# Adding a label to the y-axis.
plt.ylabel("Number of restaurants")

# Displaying the plot.
plt.show()


# #### Calculate the percentage of restaurants in each price range category.
# 

# In[14]:


# Calculating the total number of restaurants in the DataFrame 'df'.
# The count() function is used to count the non-null values in the "Restaurant Name" column, which represents the total number of restaurants.
total_restaurants = df["Restaurant Name"].count()

# Displaying the total number of restaurants.
total_restaurants


# In[15]:


# Calculating the percentage of restaurants for each price range among the total number of restaurants.
# We multiply each count in the 'price_ranges' Series by 100 to convert them into percentages.
# Then, we divide each value by the total number of restaurants to get the percentage.
percentage = (price_ranges * 100) / total_restaurants

# Displaying the percentage of restaurants for each price range.
percentage


# In[25]:


percentage


# ### Level 1 task  4

# #### Determine the percentage of restaurants that offer online delivery.

# In[16]:


# Filtering the DataFrame 'df' to include only rows where the 'Has Online delivery' column has the value 'Yes'.
# This creates a new DataFrame called 'with_delivery' containing only the rows with online delivery available.
with_delivery = df[df['Has Online delivery'] == 'Yes']

# Displaying the DataFrame containing restaurants with online delivery available.
with_delivery


# In[27]:


percentage1 = (len(with_delivery)*100)/len(df)
print("Percentage of restaurants that offer online delivery is",percentage1,"%.")


# #### Compare the average ratings of restaurants with and without online delivery.
# 

# In[17]:


# Filtering the DataFrame 'df' to include only rows where the 'Has Online delivery' column has the value 'No'.
# This creates a new DataFrame called 'without_delivery' containing only the rows without online delivery available.
without_delivery = df[df['Has Online delivery'] == 'No']

# Displaying the DataFrame containing restaurants without online delivery available.
without_delivery


# In[18]:


avg_delivery = with_delivery['Aggregate rating'].mean()
avg_no_delivery = without_delivery['Aggregate rating'].mean()
print("Average rating of restaurants with online delivery is", avg_delivery)
print("Average rating of restaurants without online delivery is", avg_no_delivery)


# In[ ]:




