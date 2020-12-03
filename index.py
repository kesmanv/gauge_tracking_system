import dash
import plotly
import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
import dash_bootstrap_components as dbc
import sqlite3
import pandas as pd

from app import app
from layouts import gauge_layout
from database import transforms

app.layout = gauge_layout.layout

if __name__ == '__main__':
    app.run_server(debug=True)