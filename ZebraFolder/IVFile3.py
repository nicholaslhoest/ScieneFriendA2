import pandas as pd
import altair as alt

#URL GitHub Link to Adult Data
adults = pd.read_csv("https://raw.githubusercontent.com/nicholaslhoest/ScieneFriendA2/main/adult.data.txt")

#Remove Limiter for Rows
alt.data_transformers.disable_max_rows()

bluechart = alt.Chart(adults).mark_bar().encode(
    alt.Y('count(sex)', scale=alt.Scale(type='log')),
    alt.X('hours-per-week:Q', scale=alt.Scale(zero=False), title = 'Working Hours per Week'),
    tooltip = ['sex','count(sex)']
).properties(
    #Chart Designs
    title = 'Amount of Women by Working Hours Per Week',
    width=800, height=400
).transform_filter(
    #Filter, only show woman
    alt.FieldEqualPredicate(field='sex', equal=' Female')
)

orangechart = alt.Chart(adults).mark_bar().encode(
    alt.Y('count(sex)', title = 'Amount of Women', scale=alt.Scale(type='log')),
    alt.X('hours-per-week:Q', scale=alt.Scale(zero=False), title = 'Working Hours per Week'),
    color=alt.value("orange"),
    tooltip = ['sex','count(sex)']
).properties(
    #Chart Designs
    title = 'Amount of Women by Working Hours Per Week',
    width=800, height=400
).transform_filter(
    #Filter, only show woman
    alt.FieldEqualPredicate(field='sex', equal=' Female')
).transform_filter(
    #Filter, only show woman
    alt.FieldRangePredicate(field='hours-per-week', range=[20, 40])
)

bluechart + orangechart