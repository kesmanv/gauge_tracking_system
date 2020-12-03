import dash_bootstrap_components as dbc

nav = dbc.Nav(
    [
        dbc.NavLink("Dashboard", active=True, href="#"),
        dbc.NavLink("QAS", href="#"),
        dbc.NavLink("Gauges", href="/"),
        dbc.NavLink("Root Cause Analysis", disabled=True, href="#"),
    ]
)