import dash

import dash_html_components as html
import dash_bootstrap_components as dbc 
from database import transforms


card_active = dbc.Card(
    [
        dbc.CardBody(
            [
                html.H1(transforms.df.shape[0], className='card-title', style={'color':'green'})
                ,html.H6("Active", className="card-subtitle")
            ]
        )
    ]
)

card_due = dbc.Card(
    [
        dbc.CardBody(
            [  
                html.H1(transforms.df.shape[0], className="card-title", style={'color':'orange'})
                ,html.H6("Due soon", className="card-subtitle")                 
            ]
        )
    ], outline=False
)

card_overdue = dbc.Card(
    [
        dbc.CardBody(
            [  
                html.H1(transforms.df.shape[0], className="card-title", style={'color':'red'})
                ,html.H6("Overdue", className="card-subtitle")                 
            ]
        )
    ], style={'width': '26rem'}
)

row_card = html.Div(
    [
        dbc.CardDeck(
            [
                card_active
                ,card_due
                ,card_overdue
            ]
        ),
    ], style={'padding': '25px'}
)