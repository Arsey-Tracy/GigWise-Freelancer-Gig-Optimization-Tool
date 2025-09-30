import reflex as rx
from app.states.state import AppState


def nav_item(icon: str, text: str, page: str) -> rx.Component:
    """A navigation item with an icon and text."""
    return rx.el.div(
        rx.el.a(
            rx.icon(tag=icon, class_name="w-5 h-5"),
            rx.el.span(text, class_name="text-sm font-medium"),
            href="#",
            on_click=lambda: AppState.set_page(page),
            class_name=rx.cond(
                AppState.current_page == page,
                "flex items-center gap-3 rounded-md px-3 py-2 text-emerald-600 bg-emerald-50 transition-all",
                "flex items-center gap-3 rounded-md px-3 py-2 text-gray-500 hover:text-gray-900 hover:bg-gray-100 transition-all",
            ),
        )
    )


def sidebar() -> rx.Component:
    """The sidebar for navigation."""
    return rx.el.aside(
        rx.el.div(
            rx.el.div(
                rx.icon(tag="bar-chart-big", class_name="h-8 w-8 text-emerald-600"),
                rx.el.h1("GigWise", class_name="text-xl font-bold text-gray-900"),
                class_name="flex items-center gap-2 px-4",
            ),
            rx.el.nav(
                nav_item("search", "Search", "Search"),
                nav_item("layout-dashboard", "Dashboard", "Dashboard"),
                nav_item("sparkles", "AI Assist", "AI Assist"),
                nav_item("file-pen-line", "Gig Drafts", "Gig Drafts"),
                class_name="flex flex-col gap-1",
            ),
            class_name="flex-1 flex flex-col gap-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.image(
                    src=f"https://api.dicebear.com/9.x/initials/svg?seed=Guest",
                    class_name="h-10 w-10 rounded-full",
                ),
                rx.el.div(
                    rx.el.p(
                        "Guest User", class_name="text-sm font-semibold text-gray-800"
                    ),
                    rx.el.p("Free Plan", class_name="text-xs text-gray-500"),
                    class_name="flex-1",
                ),
                rx.icon(tag="send_horizontal", class_name="h-5 w-5 text-gray-500"),
                class_name="flex items-center gap-3",
            ),
            class_name="bg-gray-100 p-3 rounded-lg",
        ),
        class_name="w-64 flex flex-col border-r border-gray-200 bg-white p-4",
    )