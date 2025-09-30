import reflex as rx
from .state import AppState, Gig


class SearchState(AppState):
    search_query: str = ""
    price_filter_max: int = 2000
    delivery_filter: int = 30
    sort_option: str = "rating"

    @rx.var
    def filtered_gigs(self) -> list[Gig]:
        """Filter gigs based on search query and filters."""
        return [
            gig
            for gig in self.gigs
            if self.search_query.lower() in gig["title"].lower()
            and gig["price"] <= self.price_filter_max
            and (gig["delivery_time"] <= self.delivery_filter)
        ]

    @rx.var
    def sorted_gigs(self) -> list[Gig]:
        """Sort the filtered gigs."""
        if self.sort_option == "rating":
            return sorted(self.filtered_gigs, key=lambda x: x["rating"], reverse=True)
        elif self.sort_option == "price_asc":
            return sorted(self.filtered_gigs, key=lambda x: x["price"])
        elif self.sort_option == "price_desc":
            return sorted(self.filtered_gigs, key=lambda x: x["price"], reverse=True)
        return self.filtered_gigs