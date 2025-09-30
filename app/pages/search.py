import reflex as rx
from app.states.search_state import SearchState
from app.components.gig_card import gig_card


def search_page() -> rx.Component:
    return rx.el.div(
        rx.el.div(
            rx.el.h2("Gig Search", class_name="text-2xl font-bold text-gray-900"),
            rx.el.p(
                "Analyze the Fiverr market to optimize your gigs.",
                class_name="text-gray-500 mt-1",
            ),
            class_name="mb-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.icon(
                    tag="search",
                    class_name="absolute left-3 top-1/2 -translate-y-1/2 text-gray-400",
                ),
                rx.el.input(
                    placeholder="Search for gigs (e.g., 'logo design')",
                    default_value=SearchState.search_query,
                    on_change=SearchState.set_search_query,
                    class_name="w-full pl-10 pr-4 py-2.5 border border-gray-300 rounded-md focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 transition-all",
                ),
                class_name="relative flex-grow",
            ),
            class_name="flex items-center gap-4 mb-6",
        ),
        rx.el.div(
            rx.el.div(
                rx.el.label(
                    f"Max Price: ${SearchState.price_filter_max}",
                    class_name="text-sm font-medium text-gray-700 mb-2 block",
                ),
                rx.el.input(
                    type="range",
                    min=0,
                    max=5000,
                    step=50,
                    default_value=SearchState.price_filter_max.to_string(),
                    on_change=SearchState.set_price_filter_max.debounce(300),
                    class_name="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-emerald-600",
                ),
                class_name="flex-1",
            ),
            rx.el.div(
                rx.el.label(
                    f"Max Delivery Time: {SearchState.delivery_filter} days",
                    class_name="text-sm font-medium text-gray-700 mb-2 block",
                ),
                rx.el.input(
                    type="range",
                    min=1,
                    max=30,
                    step=1,
                    default_value=SearchState.delivery_filter.to_string(),
                    on_change=SearchState.set_delivery_filter.debounce(300),
                    class_name="w-full h-2 bg-gray-200 rounded-lg appearance-none cursor-pointer accent-emerald-600",
                ),
                class_name="flex-1",
            ),
            rx.el.div(
                rx.el.label(
                    "Sort By", class_name="text-sm font-medium text-gray-700 mb-2 block"
                ),
                rx.el.select(
                    rx.el.option("Top Rated", value="rating"),
                    rx.el.option("Price: Low to High", value="price_asc"),
                    rx.el.option("Price: High to Low", value="price_desc"),
                    value=SearchState.sort_option,
                    on_change=SearchState.set_sort_option,
                    class_name="w-full px-3 py-2 border border-gray-300 rounded-md focus:ring-2 focus:ring-emerald-500 focus:border-emerald-500 transition-all appearance-none bg-white",
                ),
                class_name="flex-1",
            ),
            class_name="grid grid-cols-1 md:grid-cols-3 gap-6 mb-8 p-4 bg-gray-100 rounded-lg",
        ),
        rx.el.div(
            rx.foreach(SearchState.sorted_gigs, gig_card),
            class_name="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 xl:grid-cols-4 gap-6",
        ),
        class_name="w-full",
    )