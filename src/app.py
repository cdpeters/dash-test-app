"""Overall app layout for a multi-page application.

Variables:
    app
"""

import dash
from dash import Dash, html

from components.sidebar import create_sidebar_component

# Creates app, sets external stylesheets, and configures the app to be multi-page.
app = Dash(
    name=__name__,
    use_pages=True,
    title="Dash Test App",
    assets_ignore="input.css",
)

# Place the navbar and the container for page content within the app.
app.layout = html.Div(
    [
        # Sidebar.
        html.Div(
            create_sidebar_component(page_registry=dash.page_registry),
            className="bg-slate-800 h-screen w-36 fixed overflow-auto",
        ),
        # Main Content.
        html.Div(
            [
                # Topbar.
                html.Div(
                    [html.Div("Topbar")],
                    className="""bg-slate-700 text-emerald-50 px-4 py-2 flex
                    items-center""",
                ),
                # Location for page contents.
                dash.page_container,
                # Footer.
                html.Div(
                    [
                        html.Div("Footer", className="px-4 py-2 text-emerald-50"),
                        html.A(
                            html.Img(src="/assets/github.svg", className="h-4"),
                            href="https://github.com/cdpeters/dash-test-app",
                        ),
                    ],
                    className="bg-slate-700 flex items-center",
                ),
            ],
            className="bg-slate-50 h-auto flex-grow ml-36",
        ),
        # # Hidden sidebar sized div to move the navbar and content out from under the
        # # sidebar.
        # html.Div(),
        # html.Div(
        #     [
        #         topbar_component,
        #     ],
        # ),
    ],
    className="flex",
)

if __name__ == "__main__":
    app.run(debug=True)
