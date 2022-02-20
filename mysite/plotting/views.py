from django.shortcuts import render
from .models import DataSet, DataPoint
from .utils import get_chart
from .forms import PlotDisplay


# Create your views here.
def home(response):
    return render(response, "plotting/base.html", {})


def display(response, id):
    dset = DataSet.objects.get(id=id)
    diagram_type = '#1'
    form = PlotDisplay(response.POST)

    if response.method == 'POST':

        diagram_type = response.POST.get('diagram_type')
        chart = get_chart(diagram_type, [entry['x'] for entry in dset.datapoint_set.values()])

    else:
        chart = get_chart(diagram_type, [entry['x'] for entry in dset.datapoint_set.values()])

    return render(response, "plotting/display.html", {'chart': chart, 'id': id, 'name': dset.name, 'form': form})
