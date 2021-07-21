alt.Chart(adults).mark_point(filled=True).encode(
    alt.X('age', scale=alt.Scale(zero=False), title = 'Age'),
    alt.Y('hours-per-week', scale=alt.Scale(type='log'), title = 'Working Hours'),
    alt.Size('count(sex)', scale=alt.Scale(range=[0,1000]), title = 'Amount of Women'),
    alt.Color('education', title = 'Education Recieved'),
    alt.OpacityValue(0.7),
    tooltip = [
        alt.Tooltip('sex:N'),
        alt.Tooltip('count(sex):Q'),
        alt.Tooltip('native-country'),
        alt.Tooltip('education')
    ] 
).properties(
    #Chart Designs
    title = 'Scatter Graph',
    width=800, height=400
).transform_filter(
    #Filter, only show woman
    alt.FieldEqualPredicate(field='sex', equal=' Female')
).transform_filter(
    alt.FieldRangePredicate(field='age', range=[20, 35])
).transform_filter(
    alt.FieldOneOfPredicate(field='education', oneOf=[' Bachelors', ' Masters', ' Doctorate', ' Prof-school', ' Some-college'])
).interactive()