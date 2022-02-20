from django import forms

CHART_CHOICES = (
    ('#1', 'Histogram'),
    ('#2', 'Linie')
)


class PlotDisplay(forms.Form):
    diagram_type = forms.ChoiceField(choices=CHART_CHOICES)
