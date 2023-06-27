import dash_bootstrap_components as dbc

from dash import html

buttons = html.Div(
    [
        dbc.Button("Primary", color="primary", className="me-1", id="button-primary"),
        dbc.Button(
            "Secondary", color="secondary", className="me-1", id="button-secondary"
        ),
        dbc.Button("Success", color="success", className="me-1", id="button-success"),
        dbc.Button("Warning", color="warning", className="me-1", id="button-warning"),
        dbc.Button("Danger", color="danger", className="me-1", id="button-danger"),
        dbc.Button("Info", color="info", className="me-1", id="button-info"),
        dbc.Button("Light", color="light", className="me-1", id="button-light"),
        dbc.Button("Dark", color="dark", className="me-1", id="button-dark"),
        dbc.Button("Link", color="link", className="me-1", id="button-link"),
    ]
)

alerts = html.Div(
    [
        dbc.Alert(
            "This is a primary alert",
            color="primary",
            id="alert-primary",
            is_open=False,
        ),
        dbc.Alert(
            "This is a secondary alert",
            color="secondary",
            id="alert-secondary",
            is_open=False,
        ),
        dbc.Alert(
            "This is a success alert! Well done!",
            color="success",
            id="alert-success",
            is_open=False,
        ),
        dbc.Alert(
            "This is a warning alert... be careful...",
            color="warning",
            id="alert-warning",
            is_open=False,
        ),
        dbc.Alert(
            "This is a danger alert. Scary!",
            color="danger",
            id="alert-danger",
            is_open=False,
        ),
        dbc.Alert(
            "This is an info alert. Good to know!",
            color="info",
            id="alert-info",
            is_open=False,
        ),
        dbc.Alert(
            "This is a light alert", color="light", id="alert-light", is_open=False
        ),
        dbc.Alert("This is a dark alert", color="dark", id="alert-dark", is_open=False),
    ]
)
