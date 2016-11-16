import sqlite3

# Import plotly
import plotly.plotly as py
import plotly.graph_objs as go

# We can also do offline plotting using plotly
from plotly.offline import download_plotlyjs, init_notebook_mode, iplot

# Initiate the Plotly Notebook mode for plotting graphs offline inside a Jupyter Notebook Environment
#Run at the start of every ipython notebook to use plotly.offline. 
#This injects the plotly.js source files into the notebook.
init_notebook_mode(connected=True)

def query_SQLite(query, db):
    """
    Fetches all results of given query from SQLite database.
    Splits the resulting list of tuples into list of  y and x values.
    """
    conn = sqlite3.connect(db)
    c = conn.cursor()
    c.execute(query)
    rows =  c.fetchall()
    rows.reverse()
    conn.close() # We can close the connection if we are done with it.

    y = [str(i) for (i,j) in rows]
    x = [j for (i,j) in rows]
    return y, x


def plotly_barplot(x, y, ptitle):
    """Plots interactive horizontal barplot using plotly.
       x is a list representing values for each bar e.g. [0.18, 0.74].
       y is a list representing names of each bar e.g.['male', 'female'].
    """
    data = [go.Bar(
            x=x,
            y=y,
            orientation = 'h',
            marker=dict(
                color='rgba(50, 171, 96, 0.6)',
                line=dict(
                    color='rgba(50, 171, 96, 1.0)',
                    width=1),
            )            
    )]
    
    layout = go.Layout(autosize = False, width = 700, height = 400,
                       xaxis = dict(zeroline = False),
                       margin = dict(l = 120),
                       title = ptitle)

    # Adding labels
    annotations = [dict(x=xi, y=yi,
                        text = str(xi),
                        showarrow = False,
                       ) for xi,yi in zip(x,y)]

    layout['annotations'] = annotations
    
    fig = go.Figure(data = data, layout = layout)
    iplot(fig)