import csv
import pandas as pd
import plotly.figure_factory as ff

data_frame = pd.read_csv("data.csv")

fig = ff.create_distplot([data_frame["Average Rating"].tolist()], ["Average Rating"], colors = ['red'])

fig.update_layout(
                font_family = "Courier New",
                font_size = 20,
                title_text = 'Average Ratings of Mobile Phones of different Brands on Amazon',
                title_x = 0.5,
                title_font_size = 30,
                title_font_family = "Times New Roman",
                title_font_color = "red",
                legend_font_size = 20,
                legend_font_color = "red")

fig.update_xaxes(color = "red")
fig.update_yaxes(color = "red")

fig.show()