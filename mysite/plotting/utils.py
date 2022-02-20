import uuid, base64
from .models import *
from io import BytesIO
from matplotlib import pyplot


def get_graph():
    buffer = BytesIO()
    pyplot.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_chart(chart_type, data, **kwargs):
    pyplot.switch_backend('AGG')
    fig = pyplot.figure(figsize=(10, 4))
    X = data
    if chart_type == '#1':
        print("Histogram")
        pyplot.hist(X)
    elif chart_type == '#2':
        print("Line graph")
        pyplot.plot(X, color='gray', marker='o', linestyle='dashed')
    else:
        print("Apparently...chart_type not identified")
    pyplot.tight_layout()
    chart = get_graph()
    return chart
