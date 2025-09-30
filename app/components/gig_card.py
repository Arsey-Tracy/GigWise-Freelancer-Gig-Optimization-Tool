import reflex as rx
from app.states.state import Gig


def seller_badge(level: str) -> rx.Component:
    return rx.el.span(
        level,
        class_name=rx.match(
            level,
            (
                "Top Rated",
                "px-2 py-1 text-xs font-medium text-green-700 bg-green-100 rounded-full",
            ),
            (
                "Level 2",
                "px-2 py-1 text-xs font-medium text-blue-700 bg-blue-100 rounded-full",
            ),
            (
                "Level 1",
                "px-2 py-1 text-xs font-medium text-yellow-700 bg-yellow-100 rounded-full",
            ),
            (
                "New Seller",
                "px-2 py-1 text-xs font-medium text-gray-700 bg-gray-100 rounded-full",
            ),
            "px-2 py-1 text-xs font-medium text-gray-700 bg-gray-100 rounded-full",
        ),
    )


def gig_card(gig: Gig) -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.image(
                src=gig["image_url"], class_name="w-full h-40 object-cover rounded-t-lg"
            ),
            class_name="relative",
        ),
        rx.el.div(
            rx.el.div(
                rx.image(
                    src=f"https://api.dicebear.com/9.x/notionists/svg?seed={gig['seller_name']}",
                    class_name="h-8 w-8 rounded-full border-2 border-white",
                ),
                rx.el.div(
                    rx.el.p(
                        gig["seller_name"],
                        class_name="text-sm font-semibold text-gray-800",
                    ),
                    seller_badge(gig["seller_level"]),
                    class_name="flex-1 flex items-center justify-between",
                ),
                class_name="flex items-center gap-3",
            ),
            rx.el.p(
                gig["title"],
                class_name="mt-2 text-sm font-medium text-gray-700 h-10 overflow-hidden leading-tight",
            ),
            rx.el.div(
                rx.icon(
                    tag="star", class_name="w-4 h-4 text-yellow-400 fill-yellow-400"
                ),
                rx.el.span(
                    f"{gig['rating']:.1f}", class_name="text-sm font-bold text-gray-800"
                ),
                rx.el.span(
                    f"({gig['reviews_count']})", class_name="text-sm text-gray-500"
                ),
                class_name="flex items-center gap-1 mt-3",
            ),
            class_name="p-4",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.p("DELIVERY", class_name="text-xs text-gray-500 font-medium"),
                rx.el.p(
                    f"{gig['delivery_time']} Day(s)", class_name="text-sm font-semibold"
                ),
                class_name="text-center",
            ),
            rx.el.div(
                rx.el.p("PRICE", class_name="text-xs text-gray-500 font-medium"),
                rx.el.p(
                    f"${gig['price']:.2f}",
                    class_name="text-sm font-semibold text-emerald-600",
                ),
                class_name="text-center",
            ),
            class_name="flex justify-around items-center border-t border-gray-100 py-2 px-4",
        ),
        class_name="bg-white rounded-lg border border-gray-200 shadow-sm hover:shadow-md transition-shadow duration-200 flex flex-col justify-between",
    )