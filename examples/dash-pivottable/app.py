import json as js
import dash
from dash.dependencies import Input, Output
import dash_html_components as html
import dash_pivottable
#from data import data


def Header(name, app):
    img_style = {"float": "right", "height": 40, "margin-right": 10}
    dash_logo = html.Img(src=app.get_asset_url("huawei.jpg"), style=img_style)
    ghub_logo = html.Img(src=app.get_asset_url("github.jpg"), style=img_style)

    return html.Div(
        [
            html.H1(name, style={"margin": 10, "display": "inline"}),
            html.A(dash_logo, href="https://www.huawei.com/cn/"),
            html.A(ghub_logo, href="https://github.com/CAKGOD"),
            html.Hr(),
        ]
    )


with open('./data/data.json') as f:
    temp = js.loads(f.readline())
    data = temp[0:1] + temp[-5000:]

app = dash.Dash(__name__)
app.title = "开源智能装备智库舆情监控"
server = app.server

app.layout = html.Div(
    [
        Header("开源智能装备智库舆情监控", app),
        dash_pivottable.PivotTable(
            menuLimit=50000,
            id="table",
            data=data,
            cols=["time"],
            colOrder="key_a_to_z",
            rows=["keywords"],
            rowOrder="key_a_to_z",
            rendererName="Table Col Heatmap",
            aggregatorName="Count",
            vals=["count"],
            valueFilter={"time": {'unknown': False}},
        ),
        html.Div(id="output"),
    ]
)


@app.callback(
    Output("output", "children"),
    [
        Input("table", "cols"),
        Input("table", "rows"),
        Input("table", "rowOrder"),
        Input("table", "colOrder"),
        Input("table", "aggregatorName"),
        Input("table", "rendererName"),
    ],
)

def display_props(cols, rows, row_order, col_order, aggregator, renderer):
    return [
        html.P(str(cols), id="columns"),
        html.P(str(rows), id="rows"),
        html.P(str(row_order), id="row_order"),
        html.P(str(col_order), id="col_order"),
        html.P(str(aggregator), id="aggregator"),
        html.P(str(renderer), id="renderer"),
    ]


if __name__ == "__main__":
    app.run_server(debug=True)
