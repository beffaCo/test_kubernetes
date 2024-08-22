import flask
from dash import Dash, html

flask_server = flask.Flask(__name__)
app = Dash(
    __name__,
    title="Example dashboard",
    url_base_pathname="/example_dashboard/"
)
server = app.server


app.layout = html.Div(
    [
        html.H1("Welcome to the example dashboard"),
        html.Div("This dashboard will be deployed on kubernetes")
    ]
)

if __name__ == "__main__":
    app.run_server(port=8888, debug=True)
