from dash import Dash, html

app = Dash(
    __name__,
    title="Example dashboard",
    url_base_pathname="/example_dashboard/"
)
server = app.server


app.layout = html.Div(
    [
        html.H1("Welcome to the example dashboard: does it redeploy?"),
        html.Div("This dashboard will be deployed on kubernetes")
    ]
)

if __name__ == "__main__":
    app.run_server(host='0.0.0.0', port=8888, debug=True)
