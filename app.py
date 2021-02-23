## Bokeh server for button click

from bokeh.io import curdoc
from bokeh.layouts import row
from bokeh.models import ColumnDataSource
from bokeh.models.widgets import Button
from bokeh.plotting import figure
from bokeh.layouts import column, row
from bokeh.models import Spinner
import pandas as pd
df=pd.read_csv('df.csv')


source = ColumnDataSource(df)
y_list= source.data['favorite_count'].tolist()


plot_figure = figure(plot_height=450, plot_width=600,
              tools="save,reset",
               toolbar_location="below")

points = plot_figure.scatter('retweet_count', 'favorite_count', source=source, size=10)
spinner = Spinner(title="Glyph size", low=1, high=40, step=0.5, value=4, width=80)
spinner.js_link('value', points.glyph, 'size')
button = Button(label="Click to set plot title", button_type="success")
# visualization of retweeting tweets and favorite tweets from the home timeline at a time t

def button_click():
    plot_figure.title.text = 'Button Clicked'

button.on_click(button_click)

layout=row(row(column(spinner, width=100), plot_figure))

curdoc().add_root(layout)
curdoc().title = "Button Bokeh Server"