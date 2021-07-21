import pandas as pd
import altair as alt

#URL GitHub Link to Adult Data
adults = pd.read_csv("https://raw.githubusercontent.com/nicholaslhoest/ScieneFriendA2/main/adult.data.txt")

legend = pd.DataFrame(
  {'Female': [299, 758, 1063, 233, 32, 11],
   'Target Female': [77, 440, 808, 4153, 4888, 2406]}
)

#Remove Limiter for Rows
alt.data_transformers.disable_max_rows()

bluechart = alt.Chart(adults).mark_bar().encode(
    alt.Y('count(sex)', title = 'Amount of Women'),
    alt.X('age:Q', scale=alt.Scale(zero=False), title = 'Age'),
    tooltip = ['sex','count(sex)']
).properties(
    #Chart Designs
    title = 'Amount of Women by Age',
    width=800, height=400
).transform_filter(
    #Filter, only show woman
    alt.FieldEqualPredicate(field='sex', equal=' Female')
)

orangechart = alt.Chart(adults).mark_bar(color = 'orange').encode(
    alt.Y('count(sex)'),
    alt.X('age:Q', scale=alt.Scale(zero=False), title = 'Age'),
    tooltip = ['sex','count(sex)']
).properties(
    #Chart Designs
    title = 'Amount of Women by Age',
    width=800, height=400
).transform_filter(
    #Filter, only show woman
    alt.FieldEqualPredicate(field='sex', equal=' Female')
).transform_filter(
    #Filter, only show woman
    alt.FieldRangePredicate(field='age', range=[20, 35])
)

bluechart + orangechart