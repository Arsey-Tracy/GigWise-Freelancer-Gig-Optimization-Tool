import reflex as rx


def placeholder_page(title: str, icon: str) -> rx.Component:
    return rx.el.div(
        rx.icon(tag=icon, class_name="h-16 w-16 text-gray-300"),
        rx.el.h2(f"{title} Page", class_name="text-2xl font-bold text-gray-400 mt-4"),
        rx.el.p("This feature is coming soon!", class_name="text-gray-400 mt-2"),
        class_name="flex flex-col items-center justify-center h-full w-full border-2 border-dashed border-gray-300 rounded-lg bg-gray-50",
    )


def dashboard_page() -> rx.Component:
    return placeholder_page("Dashboard", "layout-dashboard")