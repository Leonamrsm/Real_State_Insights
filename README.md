# House Rocket Project

## Insights from a real state portfolio analysis

To view the developed app that presents views for each of the hypotheses raised and answers the business questions, go to https://insights-house-rocket.herokuapp.com/

# 1. Business Problem

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
Dashboard deploy on [Heroku](https://insights-house-rocket.herokuapp.com/)


**Step 01. Data Extraction:** Exctract the data from [Kaggle](https://www.kaggle.com/harlfoxem/housesalesprediction/discussion/207885).

**Step 02. Data Description:** My goal is to use statistics metrics to identify data outside the scope of business.

**Step 03. Feature Engineering:** Derive new attributes based on the original variables to better describe the phenomenon that will be modeled.

**Step 04. Data Filtering:** Filter rows and select columns that do not contain information for modeling or that do not match the scope of the business.

**Step 05. Exploratory Data Analysis:** Explore the data to find insights and better understand the impact of variables on model learning.

**Step 06. Answer business problems:** Estimating the profit that can be made from buy and sell recommendations

**Step 07. Deploy the model:** Publish the model in a cloud environment so that other people can see the results obtained.

# 4. Top Insights

| Hipótese                                                     | Resultado  | Tradução para negócio                                        |
| ------------------------------------------------------------ | ---------- | ------------------------------------------------------------ |
| **H1** - Properties with waterfront, are 100% more expensive, on average?| False | Buy houses with waterfront that are cheap                    |
| **H2** - Properties with build date less than 1955, are 50% cheaper, on average? | False      | Investing in properties regardless of the construction date      |
| **H3** - Properties in bad condition but good view are 20% cheaper than properties with average condition and average view | True | Acquire properties in poor condition but with good view if the cost of the renovation is not more than 80% of the property price |
| **H4** - Property price growth year after year (YoY) is 10% | False | Investing in properties regardless of the year built  |
| **H5** - Properties with 3 bathrooms have a MoM (Month over Month) growth of 15% | False      | The average price MoM of properties with 3 bathrooms does not vary linearly |
| **H6** - Properties that have already been renovated (yr_renovated != 0) are on average 40% more expensive | True | Invest in unrenovated properties and renovate them for sale |
| **H7** - The average property price is 10% higher during the summer and spring | False      | The average property price is 4.49% higher during the summer and spring. Acquire properties in the fall/winter and sell them in the spring/summer |
| **H8** - The average property price with basement and good condition is 40% higher than poroperties without basement and good condition   | True      | Acquire properties in good condition without a basement to build a basement for sale                 |
| **H9** - The growth in the price of properties in good condition is 20% with the grade | False | Acquire properties with low levels of design and renovate them in order to increase the level of design for sale            |
| **H10** - Properties in good condition and good view are, in average, 40% more expensive than properties in condition and average view | True      | Acquire properties with good conditions but an average view to renovate them in order to obtain a better view, thus profiting more from the sale                 |


# 7. Business Results

The following strategies for buying and selling properties were defined in order to answer the business questions:

**Purchase conditions**:

- Group data by region (postal code)
- Within each region, find the median property price
- Suggest that properties that are below the median price for each region and that are chosen in good condition be purchased

Once the house has been purchased, what is the best time to sell it and at what price?

- Group data by region (postal code) and by seasonality (Summer, Inter, etc).
- Within each region and seasonality, calculate the median price

**Sale conditions**:

1. If the purchase price is higher than the region median + seasonality
      - The sale price will be equal to the purchase price + 10%
2. If the purchase price is less than the region median + seasonality.
      - The sale price will be equal to the purchase price + 30%


# 8. Conclusions

# 9. Lessons Learned

# 10. Next Steps to Improve

**1.** **Develop an app** that intakes a portfolio of patients and assigns for each patient its respective probability of presenting a cardiovascular disease.

**2.** **Run a Design Discovery** to uncover facts that could be missing in our analysis in order to enrich the data that we have and improve the model performance.

**3.** Build a **model retraining pipeline**.


