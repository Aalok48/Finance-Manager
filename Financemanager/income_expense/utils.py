import matplotlib.pyplot as plt
from io import BytesIO
import base64
import numpy as np

def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png=buffer.getvalue()
    buffer.close()
    graph=base64.b64encode(image_png).decode('utf-8')
    return graph

# first the get_plot is called by views.py and then the get_graph
def get_plot(x,y):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    date_indices = np.arange(len(x))
    bar_width = 0.5
    plt.bar(date_indices,y, width=bar_width)
    plt.xlabel('Date')
    plt.ylabel('Amount')
    plt.xticks(date_indices, x, rotation=45)
    plt.tight_layout()
    graph=get_graph()
    return graph

