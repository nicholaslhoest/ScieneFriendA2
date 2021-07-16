import pandas as pd
import altair as alt

#URL GitHub Link to Adult Data
adults = pd.read_csv("https://raw.githubusercontent.com/nicholaslhoest/ScieneFriendA2/main/adult.data.txt")

#Remove Limiter for Rows
alt.data_transformers.disable_max_rows()

#IV: Job vs. working hours - Layered histogram
#Table Creation
alt.Chart(adults).mark_area().encode(
    #Axis
    alt.X('count(sex)',scale=alt.Scale(type='sqrt'), title = 'Amount of Woman'),
    alt.Y('hours-per-week', scale=alt.Scale(zero=False), title = 'Hour'),
    alt.Color('occupation:N'),
    alt.OpacityValue(0.5),
    tooltip = ['sex','count(sex)'], 
).properties(
    #Chart Designs
    title = 'Jobs vs. Working Hours',
    width=800, height=400
).transform_filter(
    #Fitler by Occupation
    alt.FieldOneOfPredicate(field='occupation', oneOf=[' Sales', ' Tech-support', ' Other-service'])
).transform_filter(
    #Fitler by hours-per-week
    alt.FieldRangePredicate(field='hours-per-week', range=[30,40])
)