import pandas as pd
import altair as alt

#URL GitHub Link to Adult Data
adults = pd.read_csv("https://raw.githubusercontent.com/nicholaslhoest/ScieneFriendA2/main/adult.data.txt")

#Remove Limiter for Rows
alt.data_transformers.disable_max_rows()

#IV: Job sector, age, education - Scatter Matrix
#Table Creation
alt.Chart(adults).mark_circle().encode(
    alt.X(alt.repeat("column"), type='quantitative'),
    alt.Y(alt.repeat("row"), type='quantitative'),
    color='sex'
).properties(
    #Desing of Chart
    width=150,
    height=150
).repeat(
    row=['education-num', 'age', 'hours-per-week'],
    column=['hours-per-week', 'age', 'education-num']
).transform_filter(
    #Filter, only show woman
    alt.FieldEqualPredicate(field='sex', equal=' Female')
).transform_filter(
    #Filter age range
    alt.FieldRangePredicate(field='age', range=[20, 35])
).interactive() #make the graph interactive