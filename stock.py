from pandas_datareader import data
import datetime
from bokeh.plotting import figure, show, output_file
from bokeh.models.annotations import Title

start = datetime.datetime(2019, 7, 1)
end = datetime.datetime(2020,7,30)
stock = data.DataReader('GOOG', 'yahoo' , start, end)

def inc_dec(c, o):
    if c>o:
        return "Increase" 
    elif c<o:
        return "Decrease"
    else:
        return "Equal"

stock["Status"] = [inc_dec(c,o) for c,o in zip(stock.Close, stock.Open)]
stock["Middle"] = (stock.Open + stock.Close)/2
stock["Height"] = abs(stock.Close - stock.Open)
t=Title()
p = figure(x_axis_type='datetime', width=1000, height=300, aspect_scale=True, aspect_ratio=True)
t.text='Candlestick Chart'
p.title=t
p.grid.grid_line_alpha=0.3

hours_12=12*60*60*1000
p.segment(stock.index, stock.High, stock.index, stock.Low)

p.rect(stock.index[stock.Status=='Increase'], stock.Middle[stock.Status=='Increase'],
    hours_12, stock.Height[stock.Status=='Increase'],fill_color='#CCFFFF', line_color='Black')
p.rect(stock.index[stock.Status=='Decrease'], stock.Middle[stock.Status=='Decrease'],
    hours_12, stock.Height[stock.Status=='Decrease'],fill_color='#FF3333', line_color='Black')

output_file('Stock.html')
show(p)