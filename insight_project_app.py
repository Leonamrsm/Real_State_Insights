import pandas as pd
import numpy as np 
import streamlit as st
import plotly.express as px

st.set_page_config(page_title="House Rockect Insights", page_icon="📊",
                   layout="wide")


c1, c2 = st.columns((1,5))


st.write('')
HR_format = '<p style="font-family:sans-serif;' \
                'color:#FFFFFF;' \
                'font-size: 300%;' \
                'font-weight: bold;' \
                'font-style: italic;' \
                'text-align: left;' \
                '">House Rocket Company</p>'
st.markdown(HR_format, unsafe_allow_html=True)

welcome_format = '<p style="font-family:sans-serif;' \
                    'color:#FFFFFF;' \
                    'font-size: 25px;' \
                    'font-style: italic;' \
                    'text-align: left;' \
                    '">Seattle Real Estate Investment Data Report from May 2014 to May 2015 </p>'
st.markdown(welcome_format, unsafe_allow_html=True)

st.sidebar.markdown('**House Rocket** is a company that works with the purchase and sale of real estate. '
                          'The goal of this insight project is to find the best business opportunities.')

st.sidebar.write("For more information about the project, go to: "
                         "[GitHub](https://github.com/Leonamrsm/Real_State_Insights_Project)")

@st.cache(allow_output_mutation=True)
def get_data(path):
    return pd.read_csv(path)

def set_feature(df):
    # If there is duplicate data with same id, it will be removed 
    df = df.drop_duplicates(subset=['id'])
    # Transform date from object to datetime
    df['date'] = pd.to_datetime(df['date'])

    # Creation of New Features
    df['month'] = df['date'].dt.month
    df['year'] = df['date'].dt.year
    df['year_month'] = df['date'].dt.strftime('%Y-%m')

    df['season'] = df['month'].apply(lambda x: 'summer' if (x > 5) & (x < 8) else
                                            'spring' if (x > 2) & (x < 5) else
                                            'fall' if (x > 8) & (x < 12) else
                                            'winter')

    df['condition_str'] = df['condition'].apply(lambda x: 'good' if x >= 4 else
                                                        'average' if x == 3 else         
                                                        'bad')

    df['grade_str'] = df['grade'].apply(lambda x: 'low' if x <= 3 else
                                                'average' if x < 11 else
                                                'high')

    df['view_str'] = df['view'].apply(lambda x:   'bad' if x < 2 else
                                                'average' if x == 2 else
                                                'good')    

    return df

def overview_data(df):

    st.header("Data Overview")
    exp_data = st.expander("Click here to expand and see the dataset general information", expanded=False)
    
    with exp_data:

        st.write(df.head(50))
        st.subheader("Data Dimensions")
        st.write("Number of Registers:", df.shape[0])
        st.write("Number of Attributes:", df.shape[1])

        st.subheader("Date Interval of Home Sales")
        st.write("", df['date'].min())
        st.write("", df['date'].max())

        st.header('Descriptive Statistics')

        num_attributes = df.select_dtypes(include = ['int64', 'float64'])
        num_attributes = num_attributes.drop(['id'], axis = 1)
        # central tendency - mean, median
        mean = pd.DataFrame( num_attributes.apply(np.mean))
        median = pd.DataFrame(num_attributes.apply(np.median))
        # dispersion - sdt, min, max
        std = pd.DataFrame(num_attributes.std())
        min_ = pd.DataFrame(num_attributes.apply(np.min))
        max_ = pd.DataFrame(num_attributes.apply(np.max))

        pdList = [max_, min_, mean, median, std] 

        df2= pd.concat(pdList, axis=1).reset_index()
        df2.columns = ['attributes','max', 'min', 'mean', 'median', 'std']

        st.dataframe(df2, height=500)

    return None

def insights(df):
    st.header('Business Hypotheses')
    st.write('Below are the business hypotheses that were raised, and whether these are true or not.')

    c1,c2 = st.columns(2)
    # ========================================================== H1 ==========================================================


    c1.subheader('H1: Properties with waterfront, are 100% more expensive, on average')

    h1 = df[['price', 'waterfront']].groupby('waterfront').mean().reset_index()
    h1['waterfront'] = h1['waterfront'].apply(lambda x: 'No' if x == 0 else 'Yes')  

    fig = px.bar(h1, x='waterfront', y = 'price', color = 'waterfront',  labels={"waterfront": "Has waterfront?",
                                                                                 "price": "Price"},
                                                                                  template= 'seaborn')
    fig.update_layout(showlegend = False)

    c1.plotly_chart(fig, use_container_width=True)

    # ========================================================== H2 ==========================================================

    c2.subheader('H2: Properties with build date less than 1955, are 50% cheaper, on average')

    mean_price_below_1955 = df.loc[df['yr_built'] <=1955, 'price'].mean()
    mean_price_above_1955 = df.loc[df['yr_built'] > 1955, 'price'].mean()

    x=['<= 1955', '> 1955']
    y=[mean_price_below_1955, mean_price_above_1955]

    fig = px.bar(x=x, y=y, color=x, labels={"x": "Year Built","y": "Price"}, template= 'seaborn')
    fig.update_layout(showlegend = False)

    c2.plotly_chart(fig, use_container_width=True)

    c1,c2 = st.columns(2)
    # ========================================================== H3 ==========================================================


    c1.subheader('H3: Properties in bad condition but good view are 20% cheaper than properties with average condition and average view')

    mean_price_bad_condition_good_view = df.loc[(df['view_str']=='good') & (df['condition_str']=='bad'), 'price'].mean()
    mean_price_avg_condition_avg_view = df.loc[(df['view_str']=='average') & (df['condition_str']=='average'), 'price'].mean()

    x=['Good Condition/Bad View', 'Avg Condition/Avg View']
    y=[mean_price_bad_condition_good_view, mean_price_avg_condition_avg_view]

    fig = px.bar(x=x, y=y, color=x, labels={"y": "Price"}, template= 'seaborn')
    fig.update_layout(showlegend = False)

    c1.plotly_chart(fig, use_container_width=True)

    # ========================================================== H4 ==========================================================

    c2.subheader('H4: Property price growth year after year (YoY) is 10%')

    h4 = df[['price', 'year']].groupby('year').mean().reset_index()
    h4['year'] = h4['year'].astype(str)

    fig = px.bar(h4, x='year', y='price', color='year',labels={"x": "Year Built","y": "Price"}, template= 'seaborn')
    fig.update_layout(showlegend = False)

    c2.plotly_chart(fig, use_container_width=True)

    c1,c2 = st.columns(2)
    # ========================================================== H5 ==========================================================

    c1.subheader('H5: Properties with 3 bathrooms have a MoM (Month over Month) growth of 15%')

    h5 = df.loc[df['bathrooms']==3, ['price', 'year_month']].groupby('year_month').mean().reset_index()

    fig = px.line(h5, x='year_month', y='price',labels={"y": "Price"}, template= 'seaborn')
    fig.update_layout(showlegend = False)
    
    c1.plotly_chart(fig, use_container_width=True)

    # ========================================================== H6 ==========================================================

    c2.subheader('H6: Properties that have already been renovated are on average 40% more expensive')

    mean_price_not_renovated = df.loc[df['yr_renovated']==0,'price'].mean()
    mean_price_renovated = df.loc[df['yr_renovated']!=0,'price'].mean()

    x=['No', 'Yes']
    y=[mean_price_not_renovated, mean_price_renovated]

    fig = px.bar(x=x, y=y, color=x, labels={"x": "Is renovated?", "y": "Price"}, template= 'seaborn')
    fig.update_layout(showlegend = False)
    
    c2.plotly_chart(fig, use_container_width=True)

    c1, c2 = st.columns(2)
    # ========================================================== H7 ==========================================================

    c1.subheader('H7: The average property price is 10% higher during the summer and spring')

    h7 = df[['price', 'season']].groupby(['season']).mean().reset_index()

    mean_price_summer_spring = h7.loc[(h7['season']=='summer') | (h7['season']=='spring'), 'price'].values[0]
    mean_price_winter_fall = h7.loc[(h7['season']=='winter') | (h7['season']=='fall'), 'price'].values[0]

    x=['Summer & Spring', 'Winter & Fall']
    y=[mean_price_summer_spring, mean_price_winter_fall]

    fig = px.bar(x=x, y=y, color=x, labels={"y": "Mean Price", "x": "Seasons"}, template= 'seaborn')
    fig.update_layout(showlegend = False)
    
    c1.plotly_chart(fig, use_container_width=True)

    # ========================================================== H8 ==========================================================

    c2.subheader('H8: The average property price with basement and good condition is 40% higher than poroperties without basement and good condition')

    mean_price_with_basement = df.loc[(df['sqft_basement']!=0) & (df['condition']>=4),'price'].mean()
    mean_price_without_basement = df.loc[(df['sqft_basement']==0) & (df['condition']>=4),'price'].mean()

    x=['No', 'Yes']
    y=[mean_price_without_basement, mean_price_with_basement]

    fig = px.bar(x=x, y=y, color=x, labels={"x": "Has basement?", "y": "Average Price"}, template= 'seaborn')
    fig.update_layout(showlegend = False)
    
    c2.plotly_chart(fig, use_container_width=True)

    c1,c2 = st.columns(2)
    # ========================================================== H9 ==========================================================

    c1.subheader('H9: The growth in the price of properties in good condition is 20% with the grade')

    h9 = df.loc[(df['condition_str'] == 'good'), ['price', 'grade_str']].groupby('grade_str').mean().reset_index()

    mean_price_low_condition = h9.loc[h9['grade_str']=='low','price'].values[0]
    mean_price_average_condition = h9.loc[h9['grade_str']=='average','price'].values[0]
    mean_price_high_condition = h9.loc[h9['grade_str']=='high','price'].values[0]

    x=['low', 'average', 'high']
    y=[mean_price_low_condition, mean_price_average_condition, mean_price_high_condition]

    fig = px.bar(x=x, y=y, color=x, labels={"y": "Mean Price", "x": "Grade"}, template= 'seaborn')
    fig.update_layout(showlegend = False)
    
    c1.plotly_chart(fig, use_container_width=True)

    # ========================================================== H10 ==========================================================

    c2.subheader('H10: Properties in good condition and good view are, in average, 20% more expensive than properties in condition and average view')

    mean_price_good_condition_good_view = df.loc[(df['view_str']=='good') & (df['condition_str']=='good'), 'price'].mean()
    mean_price_good_condition_avg_view = df.loc[(df['view_str']=='average') & (df['condition_str']=='good'), 'price'].mean()

    x=['Good Condition - Good View', 'Good Condition - Average View']
    y=[mean_price_good_condition_good_view, mean_price_good_condition_avg_view]

    fig = px.bar(x=x, y=y, color=x, labels={"x": "View and Condition States", "y": "Mean Price"}, template= 'seaborn')
    fig.update_layout(showlegend = False)
    
    c2.plotly_chart(fig, use_container_width=True)

    return None

def insights_table ():
    st.title("Summary of Hypotheses")
    hipoteses = pd.DataFrame({
    'Result': ['False', 'False', 'False', 'False', 'False', 'True', 'False', 'True', 'False', 'True'],
    'Decision Making':['Buy houses with waterfront that are cheap', 
                        'Investing in properties regardless of the construction date', 
                        'Acquire properties in poor condition but with good view if the cost of the renovation is not more than 80% of the property price', 
                        'Investing in properties regardless of the year built', 
                        'The average price MoM of properties with 3 bathrooms does not vary linearly', 
                        'Invest in unrenovated properties and renovate them for sale', 
                        'Acquire properties in the fall/winter and sell them in the spring/summer', 
                        'Acquire real estate without a basement to build a basement for sale', 
                        'Acquire properties with low levels of design and renovate them in order to increase the level of design for sale', 
                        'Acquire properties with good conditions but an average view to renovate them in order to obtain a better view, thus profiting more from the sale']}, 
    index=['H1', 'H2', 'H3', 'H4', 'H5', 'H6', 'H7', 'H8', 'H9', 'H10'])

    hipoteses = hipoteses.style.set_table_styles([dict(selector='th', props=[('text-align', 'left')])])
    hipoteses.set_properties(**{'text-align': 'left'}).hide_index()
    st.table(hipoteses)
    return None

def filter_houses_to_buy(df):

    st.sidebar.title('Business Questions Options')


    # ========================================================== Filter by year Built ==========================================================
    st.sidebar.header('Select Year Build Range')

    min_year_built = df['yr_built'].min()
    max_year_built = df['yr_built'].max()

    f_min_year_built = st.sidebar.slider('Min Year Built', int(min_year_built), int(max_year_built), int(min_year_built))
    f_max_year_built = st.sidebar.slider('Max Year Built', int(min_year_built), int(max_year_built), int(max_year_built))

    df = df[(df['yr_built'] >= f_min_year_built) & (df['yr_built'] <= f_max_year_built)]

    # ========================================================== Filter by Price ================================================================
    st.sidebar.header('Select Price Range')
    
    min_price = int(df['price'].min())
    max_price = int(df['price'].max())

    f_min_price = st.sidebar.slider('Min Price', min_price, max_price, min_price)
    f_max_price = st.sidebar.slider('Max Price', min_price, max_price, max_price)

    df = df[(df['price'] >= f_min_price) & (df['price'] <= f_max_price)]

    # ========================================================== Filter by Profit ================================================================
    st.sidebar.header('Select Profit Range')
    
    min_profit = int(df['profit'].min())
    max_profit = int(df['profit'].max())

    f_min_profit = st.sidebar.slider('Min Profit', min_profit, max_profit, min_profit)
    f_max_profit = st.sidebar.slider('Max Profit', min_profit, max_profit, max_profit)

    df = df[(df['profit'] >= f_min_profit) & (df['profit'] <= f_max_profit)]

    # ========================================================== Filter by Seasons ================================================================
    st.sidebar.header('Select the Seasons to Sell')
    
    values = list(df['season'].sort_values().unique())
    f_bedrooms = st.sidebar.multiselect('Seasons', values)
    df = df.loc[df['season'].isin(f_bedrooms) if f_bedrooms != [] else [True]*len(df)]

    return df

def business_questions(df):
    st.title('Business Questions')
    st.subheader('1. What properties should House Rocket buy and for what price?')
    st.subheader('2. Once the house has been purchased, what is the best time to sell it and at what price?')

    # ========================================================== Question 1 ==========================================================

    dfq1 = df[['zipcode', 'price']].groupby('zipcode').median().reset_index()
    dfq1 = dfq1.rename(columns={'price' : 'median_price'})
    dfq1 = pd.merge(df, dfq1, on='zipcode', how = 'inner')

    dfq1['buy'] = dfq1[['price', 'median_price', 'condition_str']].apply(
        lambda x: 'Yes' if (x['price'] < x['median_price']) & (x['condition_str'] == 'good') else 'No', axis =1)

    # Properties to buy
    houses_to_buy = dfq1[dfq1['buy']=='Yes']

    # ========================================================== Question 2 ==========================================================

    dfq2 = houses_to_buy[['zipcode', 'season','price']].groupby(['season', 'zipcode']).median().reset_index()
    dfq2 = dfq2.rename(columns = {'price' : 'median_price_by_region_season'} ) 

    houses_to_buy = pd.merge(houses_to_buy, dfq2, on=['zipcode', 'season'], how = 'inner')

    for index, row in houses_to_buy.iterrows():
        if (row['median_price_by_region_season'] > row['price']):
            houses_to_buy.loc[index, 'sale_price'] =  row['price'] * 1.1
        else:
            houses_to_buy.loc[index, 'sale_price'] = row['price'] * 1.3

    houses_to_buy['profit'] = houses_to_buy['sale_price'] - houses_to_buy['price']

    houses_to_buy = filter_houses_to_buy(houses_to_buy)

    st.write('There are ', len(houses_to_buy), ' recommended properties for purchase')
    st.write('The total estimated profit from the sale of properties is US$', int(houses_to_buy['profit'].sum()))


    st.dataframe(houses_to_buy[['id', 'zipcode', 'price', 'sale_price', 'profit', 'season', 'bedrooms', 'bathrooms', 'sqft_living', 
                                'sqft_lot', 'floors', 'waterfront', 'view', 'condition', 'grade', 'sqft_above', 'sqft_basement', 
                                'yr_built', 'yr_renovated', 'lat', 'long', 'sqft_living15', 'sqft_lot15']])

    st.write('The map below shows the recommended properties for purchase, and in which season they should be purchased. The properties are divided by color, according to the expected profit.')

    fig = px.scatter_mapbox(houses_to_buy,
                    lat='lat',
                    lon='long',
                    size='price',
                    color='profit',
                    text = 'season',
                    color_continuous_scale=px.colors.sequential.Rainbow,
                    size_max=15,
                    zoom=10)

    fig.update_layout(mapbox_style='open-street-map')
    fig.update_layout(height=600, margin={'r':0, 't':0, 'l':0, 'b':0})
    st.plotly_chart(fig, use_container_width=True)

    return None

if __name__ == '__main__':
    # data extraction
    path = './kc_house_data.csv'
    df = get_data(path)
    df = set_feature(df)
    overview_data(df)
    insights(df)
    insights_table()
    business_questions(df)

