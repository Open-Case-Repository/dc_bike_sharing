# Predicting Demand for Washington D.C.'s Bike Share System

_Version 1.0_  
_Author(s): Jon Reifschneider, Duke University School of Engineering_

# Case Scenario
You have just been hired as the first data scientist working for Capital Bikeshare, the organization which runs the Washington D.C. bike sharing system. The first major project they have asked you to work on is to build a model to predict demand for the shared bikes in the system for each hour of each day.

Having an accurate understanding of the expected demand is critical to the successful operation of Capital Bikeshare. If they underestimate demand and have too few bikes available, potential users of the system are not able to find a bike to use and so get upset and are less likely to use the system in the future.

In your initial discussions with your new colleagues, you determine that there are two main drivers of demand for bikes:
1) Time - the demand varies by day and by hour
2) Weather - weather conditions cause fluctuations in demand

Our objective in this project is to maximize the accuracy of our prediction model by creating an optimal feature set from the data we have available. The model you will use has already been set up for you in a separate script (a linear regression model) which you should not change. Your job is to prepare the data and define an optimal set of features which maximizes the model performance.


# About this Teaching Case
**Level:** Advanced Beginner  
**Language:** Python  
**Libraries:** pandas, matplotlib, scikit learn  
**Industry:** Transportation & Tourism

**Learning Topic(s):**  
- Data Manipulation
- Exploratory Data Analysis
- Feature Engineering & Feature Selection  

**Learning Objectives**  
- Understand how to create features for time-series data
- Learn to perform univariate feature selection to evaluate and reduce features
- Learn how to use encoding methods for categorical features
- Gain practice in merging, manipulating and visualizing data in pandas and matplotlib

**Pre-requisites**  
- Basic proficiency in Python and pandas

**Case Structure**  
This teaching case is structured to follow the ***modified CRISP-DM data science methodology*** used in Duke University's AI for Product Innovation graduate programs. 

**Datasets Used**  
Data used in this case is modified from the following original sources:  
Bike sharing data: Capital Bikeshare, available at https://www.capitalbikeshare.com/system-data  
Weather data: FreeMeteo weather compiled by University of Porto, available at https://www.kaggle.com/marklvl/bike-sharing-dataset