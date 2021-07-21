import pandas as pd
import altair as alt

#URL GitHub Link to Adult Data
adults = pd.read_csv("https://raw.githubusercontent.com/nicholaslhoest/ScieneFriendA2/main/adult.data.txt")

#Remove Limiter for Rows
alt.data_transformers.disable_max_rows()

alt.Chart(adults).mark_circle().encode(
    alt.X(alt.repeat("column"), type='quantitative', bin=alt.BinParams(maxbins=30)),
    alt.Y(alt.repeat("row"), type='quantitative', bin=alt.BinParams(maxbins=30)),
    alt.OpacityValue(0.7),
    color='sex',
    size=alt.Size('count()', scale=alt.Scale(range=[0, 800]), title = 'Amount of Women'),
    
).properties(
    width=300,
    height=300
).repeat(
    row=['education-num', 'age', 'hours-per-week'],
    column=['hours-per-week', 'age', 'education-num']
).transform_filter(
    #Filter, only show woman
    alt.FieldEqualPredicate(field='sex', equal=' Female')
).transform_filter(
    alt.FieldRangePredicate(field='age', range=[20, 35])
).interactive()