import pandas as pd
import altair as alt

#URL GitHub Link to Adult Data
adults = pd.read_csv("https://raw.githubusercontent.com/nicholaslhoest/ScieneFriendA2/main/adult.data.txt")

#Remove Limiter for Rows
alt.data_transformers.disable_max_rows()

alt.Chart(adults).mark_bar().encode(
    alt.Y('count(sex)', title = 'Amount of Women', scale=alt.Scale(type='log')),
    alt.X('native-country:N', title = 'Country Resides'),
    tooltip = ['sex','count(sex)']
).properties(
    #Chart Designs
    title = 'Frequency of Women based on Country and Age Requirements',
    width=800, height=400
).transform_filter(
    #Filter, only show woman
    alt.FieldEqualPredicate(field='sex', equal=' Female')
).transform_filter(
    alt.FieldRangePredicate(field='age', range=[20, 35])
).transform_filter(
    alt.FieldOneOfPredicate(field='native-country', oneOf=[' United-States', ' England', ' Puerto-Rico', ' Canada', ' Outlying-US(Guam-USVI-etc)', ' Philippines', ' Jamaica', ' Ireland', ' Scotland', ' Trinadad&Tobago', ' Holand-Netherlands'])
)