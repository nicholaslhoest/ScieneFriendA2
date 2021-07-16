import pandas as pd
import altair as alt

#URL GitHub Link to Adult Data
adults = pd.read_csv("https://raw.githubusercontent.com/nicholaslhoest/ScieneFriendA2/main/adult.data.txt")

#Remove Limiter for Rows
alt.data_transformers.disable_max_rows()

#IV: Frequency of women by age - Bar Chart
#Table Creation
alt.Chart(adults).mark_bar().encode(
    #Axis
    alt.Y('count(sex)', title = 'Amount of Woman'),
    alt.X('age:Q', scale=alt.Scale(zero=False), title = 'Age'),
    #Color highlight 
    color=alt.condition(
        alt.datum.age == 25,  # If the age is 25 this test returns True,
        alt.value('orange'),     # which sets the bar orange.
        alt.value('steelblue')),   # And if it's not true it sets the bar steelblue.
    tooltip = ['sex','count(sex)']
).properties(
    #Chart Designs
    title = 'Frequency of Woman by Age',
    width=800, height=400
).transform_filter(
    #Filter, only show woman
    alt.FieldEqualPredicate(field='sex', equal=' Female')
)