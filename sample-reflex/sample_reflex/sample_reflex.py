"""The main Dashboard App."""

from rxconfig import config

import reflex as rx

from sample_reflex.styles import BACKGROUND_COLOR, FONT_FAMILY, THEME, STYLESHEETS

from sample_reflex.pages.tools import tools
from sample_reflex.pages.team import team
from sample_reflex.pages.index import index

# Create app instance and add index page.
app = rx.App(
    theme=THEME,
    stylesheets=STYLESHEETS,
)

app.add_page(index, route="/")
app.add_page(tools, route="/tools")
app.add_page(team, route="/team")
