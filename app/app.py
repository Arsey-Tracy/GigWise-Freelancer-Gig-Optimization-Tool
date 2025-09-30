import reflex as rx
from app.states.state import AppState
from app.components.sidebar import sidebar
from app.pages.search import search_page
from app.pages.dashboard import dashboard_page
from app.pages.ai_assist import ai_assist_page
from app.pages.drafts import drafts_page


def index() -> rx.Component:
    """The main view for the app."""
    return rx.el.main(
        rx.el.div(
            sidebar(),
            rx.el.div(
                rx.match(
                    AppState.current_page,
                    ("Search", search_page()),
                    ("Dashboard", dashboard_page()),
                    ("AI Assist", ai_assist_page()),
                    ("Gig Drafts", drafts_page()),
                    search_page(),
                ),
                class_name="flex-1 h-screen overflow-y-auto p-4 sm:p-6 lg:p-8",
            ),
            class_name="flex min-h-screen bg-gray-50 text-gray-800",
        ),
        class_name="font-['Poppins']",
    )


app = rx.App(
    theme=rx.theme(appearance="light"),
    head_components=[
        rx.el.link(rel="preconnect", href="https://fonts.googleapis.com"),
        rx.el.link(rel="preconnect", href="https://fonts.gstatic.com", crossorigin=""),
        rx.el.link(
            href="https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;500;600;700&display=swap",
            rel="stylesheet",
        ),
    ],
)
app.add_page(index, title="GigWise - Fiverr Market Analysis")