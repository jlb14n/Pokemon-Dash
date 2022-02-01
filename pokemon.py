import dash
import dash_core_components as dcc
from dash import dcc,html
import plotly.express as px
import pandas as pd
import pymssql

from config import database
from config import table
from config import username
from config import password
from config import server

app = dash.Dash(__name__)

conn = pymssql.connect(server,username,password,database)
cursor = conn.cursor()
query = f"SELECT * FROM {table}"
df = pd.read_sql(query,conn)

print(df.info())

fig = px.scatter(df, x="height", y="weight", title="Height versus Weight")

app.layout = html.Div(children=[
    html.H1(children='Hello Dash'),

    html.Div(children = '''
        Dash: A web application framework for your data.
    '''),

    dcc.Graph(
        id='Height vs Weight',
        figure = fig
    )    
])

if __name__ == '__main__':
    app.run_server(debug=True)