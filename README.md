# House Rocket Project

## Insights from a real state portfolio analysis.

# 1. Business Problem.

House Rocket is a company that works with the purchase and sale of real estate. The objective of this project is to find the best business opportunities, that is, to maximize revenue. The best strategy is to buy houses in great condition at low prices and sell those properties at a higher price. The attributes of houses make them more or less attractive, influencing the attractiveness of the properties and, consequently, their price. The questions to be answered are:

1. Which houses should the CEO of House Rocket buy and at what purchase price?

2. Once the house is owned by the company, what is the best time to sell it and what would be the sale price?


# 2. Data

Data for this project can be found at: https://www.kaggle.com/harlfoxem/housesalesprediction/discussion/207885. Below is the definition for each of the 21 attributes:

* The variables on original dataset goes as follows:<br>

Variable | Definition
------------ | -------------
|id | Unique ID for each property available|
|date | Date that the property was available|
|price | Sale price of each property |
|bedrooms | Number of bedrooms|
|bathrooms | Number of bathrooms, where .5 accounts for a room with a toilet but no shower, and .75 or ¾ bath is a bathroom that contains one sink, one toilet and either a shower or a bath.|
|sqft_living | Square footage of the apartments interior living space|
|sqft_lot | Square footage of the land space|
|floors | Number of floors|
|waterfront | A dummy variable for whether the apartment was overlooking the waterfront or not|
|view | An index from 0 to 4 of how good the view of the property was|
|condition | An index from 1 to 5 on the condition of the apartment|
|grade | An index from 1 to 13, where 1-3 falls short of building construction and design, 7 has an average level of construction and design, and 11-13 have a high quality level of construction and design.|
|sqft_above | The square footage of the interior housing space that is above ground level|
|sqft_basement | The square footage of the interior housing space that is below ground level|
|yr_built | The year the property was initially built|
|yr_renovated | The year of the property’s last renovation|
|zipcode | What zipcode area the property is in|
|lat | Lattitude|
|long | Longitude|
|sqft_living15 | The square footage of interior housing living space for the nearest 15 neighbors|
|sqft_lot15 | The square footage of the land lots of the nearest 15 neighbors|

# 3. Business Assumptions.

The assumptions about the business problem is as follows:

- The following assumptions were considered for this project:
- Values ​​equal to zero in **yr_renovated** are houses that have never been renovated.
- The value equal to 33 in the **bathroom** column was considered an error and therefore it was excluded from the analysis
- The column **price** means the price that the house was / will be purchased by the House Rocket company
- Duplicate ID values ​​have been removed and only the most recent purchase is considered
- The location and condition of the property were decisive characteristics in the purchase or not of the property
- The season of the year was the decisive characteristic for the time when the property was sold


# 4. Solution Strategy

My strategy to solve this challenge was:

Understanding the business model
Understanding the business problem
Collecting the data
Data Description
Data Filtering
Feature Engineering
Exploratory Data Analysis
Insights Conclusion
Dashboard deploy on Heroku


**Step 01. Data Extraction:** Exctract the data drom [Kaggle](https://www.kaggle.com/harlfoxem/housesalesprediction/discussion/207885).

**Step 01. Data Description:** My goal is to use statistics metrics to identify data outside the scope of business.

**Step 02. Feature Engineering:** Derive new attributes based on the original variables to better describe the phenomenon that will be modeled.

**Step 03. Data Filtering:** Filter rows and select columns that do not contain information for modeling or that do not match the scope of the business.

**Step 04. Exploratory Data Analysis:** Explore the data to find insights and better understand the impact of variables on model learning.

**Step 05. Data Preparation:** Prepare the data so that the Machine Learning models can learn the specific behavior.

**Step 06. Feature Selection:** Selection of the most significant attributes for training the model.

**Step 07. Machine Learning Modelling:** Machine Learning model training

**Step 08. Hyperparameter Fine Tunning:** Choose the best values for each of the parameters of the model selected from the previous step.

**Step 09. Convert Model Performance to Business Values:** Convert the performance of the Machine Learning model into a business result.

**Step 10. Deploy Modelo to Production:** Publish the model in a cloud environment so that other people or services can use the results to improve the business decision.

# 4. Top 3 Data Insights

**Hypothesis 01:** The cases of heart diseases does not significantly depend on the height.

**False.** As observed, up to ~165 cm there are significantly more cases of heart diseases. Then, above this height, there are fewer cases.

**Hypothesis 02:** The are more cases of heart diseases for people who smokes than for people who does not.

**False.** As observed, the great majority of cases are among people who doesn't smoke.

**Hypothesis 03:** The are more cases of heart diseases for people who intakes alcohol than for people who does not.

**False.** As observed, the great majority of cases are among people who doesn't intake alcohol.


# 7. Business Results


# 8. Conclusions

# 9. Lessons Learned

# 10. Next Steps to Improve

**1.** **Develop an app** that intakes a portfolio of patients and assigns for each patient its respective probability of presenting a cardiovascular disease.

**2.** **Run a Design Discovery** to uncover facts that could be missing in our analysis in order to enrich the data that we have and improve the model performance.

**3.** Build a **model retraining pipeline**.


