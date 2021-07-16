import pandas as pd
import altair as alt

#URL GitHub Link to Adult Data
adults = pd.read_csv("https://raw.githubusercontent.com/nicholaslhoest/ScieneFriendA2/main/adult.data.txt")

#Remove Limiter for Rows
alt.data_transformers.disable_max_rows()

#IV: Compare highest country of suitable women in above categories with education level 
# of another country (comparison of what is more important) - Bubble Graph
#Table Creation
alt.Chart(adults).mark_point(filled=True).encode(
    #Axis
    alt.X('native-country:N'),
    alt.Y('count()'),
    alt.Size('count(native-country)', scale=alt.Scale(range=[0,1000])),
    alt.Color('education'),
    tooltip = [
        alt.Tooltip('sex:N'),
        alt.Tooltip('count(sex):Q'),
        alt.Tooltip('native-country')
    ] 
).transform_filter(
    #Filter, only show woman
    alt.FieldEqualPredicate(field='sex', equal=' Female')
).transform_filter(
     #Filter age range
    alt.FieldRangePredicate(field='age', range=[20, 35])
)