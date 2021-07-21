import pandas as pd
import altair as alt

#URL GitHub Link to Adult Data
adults = pd.read_csv("https://raw.githubusercontent.com/nicholaslhoest/ScieneFriendA2/main/adult.data.txt")

#Remove Limiter for Rows
alt.data_transformers.disable_max_rows()

alt.Chart(adults).mark_bar(size = 8).encode(
    alt.Y('count(occupation)',scale=alt.Scale(type='sqrt'), title = 'Amount of Women'),
    alt.X('hours-per-week', scale=alt.Scale(zero=False), title = 'Hour'),
    alt.Color('occupation:N'),
    alt.OpacityValue(0.5),
    tooltip = ['sex','count(sex)','occupation'], 
).properties(
    #Chart Designs
    title = 'Jobs vs. Working Hours',
    width=800, height=400
).transform_filter(
    #Filter, only show woman
    alt.FieldEqualPredicate(field='sex', equal=' Female')
).transform_filter(
    alt.FieldOneOfPredicate(field='occupation', oneOf=[' Sales', ' Tech-support', ' Puerto-Rico', ' Other-service', ' Machine-op-inspct'])
).interactive()
