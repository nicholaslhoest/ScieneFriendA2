import pandas as pd
import altair as alt

#URL GitHub Link to Adult Data
adults = pd.read_csv("https://raw.githubusercontent.com/nicholaslhoest/ScieneFriendA2/main/adult.data.txt")

#Remove Limiter for Rows
alt.data_transformers.disable_max_rows()

#IV: Frequency of women by country - Bar Chart
#Table Creation
alt.Chart(adults).mark_bar().encode(
    #Axis
    alt.Y('count(sex)', title = 'Amount of Woman'),
    alt.X('native-country:N', title = 'Country Resides'),
    alt.Color('sex'),
    tooltip = ['sex','count(sex)']
).properties(
    #Chart Designs
    title = 'Frequency of Woman by Country',
    width=800, height=400
).transform_filter(
    #Filter, only show woman
    alt.FieldEqualPredicate(field='sex', equal=' Female')
)