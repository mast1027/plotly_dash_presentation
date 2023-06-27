import dash_bootstrap_components as dbc
import pandas as pd
import plotly.express as px
from dash import Dash  # main class
from dash import Input  # input elements for callbacks
from dash import Output  # output elements for callbacks
from dash import callback  # callback on events, e.g. clicks
from dash import State, dash_table, dcc, html, no_update

from lib.ui_elements import alerts, buttons

# initial app setup
app = Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

# get data
df = pd.read_csv(
    "https://raw.githubusercontent.com/plotly/datasets/master/gapminder_unfiltered.csv"
)

# App layout
app.layout = dbc.Container(
    [
        html.Div(alerts),
        dbc.Row(
            [
                html.Div(
                    "App with Data, Graph, and Controls",
                    className="text-primary text-center fs-3",
                )
            ]
        ),
        dbc.Row(
            [
                dbc.RadioItems(
                    options=[
                        {"label": x, "value": x}
                        for x in ["pop", "lifeExp", "gdpPercap"]
                    ],
                    value="lifeExp",
                    inline=True,
                    id="radio-buttons-final",
                )
            ]
        ),
        dbc.Row(
            [
                dbc.Col(
                    [
                        dash_table.DataTable(
                            data=df.to_dict("records"),
                            page_size=12,
                            style_table={"overflowX": "auto"},
                        )
                    ],
                    width=6,
                ),
                dbc.Col([dcc.Graph(figure={}, id="my-first-graph-final")], width=6),
            ]
        ),
        dbc.Row([buttons]),
    ],
    fluid=True,
)


# Add controls to build the interaction
@callback(
    Output(component_id="my-first-graph-final", component_property="figure"),
    Input(component_id="radio-buttons-final", component_property="value"),
)
def update_graph(col_chosen):
    fig = px.histogram(df, x="continent", y=col_chosen, histfunc="avg")
    return fig


@callback(
    Output(component_id="alert-primary", component_property="is_open"),
    Input(component_id="button-primary", component_property="n_clicks"),
    State(component_id="alert-primary", component_property="is_open"),
)
def btn_primary(n_clicks, alert_open):
    if n_clicks is None:
        return no_update
    return not alert_open


@callback(
    Output(component_id="alert-secondary", component_property="is_open"),
    Input(component_id="button-secondary", component_property="n_clicks"),
    State(component_id="alert-secondary", component_property="is_open"),
)
def btn_secondary(n_clicks, alert_open):
    if n_clicks is None:
        return no_update
    return not alert_open


@callback(
    Output(component_id="alert-success", component_property="is_open"),
    Input(component_id="button-success", component_property="n_clicks"),
    State(component_id="alert-success", component_property="is_open"),
)
def btn_success(n_clicks, alert_open):
    if n_clicks is None:
        return no_update
    return not alert_open


@callback(
    Output(component_id="alert-warning", component_property="is_open"),
    Input(component_id="button-warning", component_property="n_clicks"),
    State(component_id="alert-warning", component_property="is_open"),
)
def btn_warning(n_clicks, alert_open):
    if n_clicks is None:
        return no_update
    return not alert_open


@callback(
    Output(component_id="alert-danger", component_property="is_open"),
    Input(component_id="button-danger", component_property="n_clicks"),
    State(component_id="alert-danger", component_property="is_open"),
)
def btn_danger(n_clicks, alert_open):
    if n_clicks is None:
        return no_update
    return not alert_open


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
