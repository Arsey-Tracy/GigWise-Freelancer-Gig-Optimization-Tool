import reflex as rx
from typing import TypedDict


class Gig(TypedDict):
    id: int
    title: str
    seller_name: str
    seller_level: str
    price: float
    rating: float
    reviews_count: int
    delivery_time: int
    image_url: str
    seller_avatar: str


class AppState(rx.State):
    """The main application state."""

    current_page: str = "Search"
    gigs: list[Gig] = [
        {
            "id": 1,
            "title": "I will design a stunning modern website in Figma",
            "seller_name": "stella_designs",
            "seller_level": "Top Rated",
            "price": 250.0,
            "rating": 5.0,
            "reviews_count": 120,
            "delivery_time": 3,
            "image_url": "/placeholder.svg",
            "seller_avatar": "stella_designs",
        },
        {
            "id": 2,
            "title": "I will create a professional logo for your business",
            "seller_name": "logo_master",
            "seller_level": "Level 2",
            "price": 75.0,
            "rating": 4.9,
            "reviews_count": 345,
            "delivery_time": 2,
            "image_url": "/placeholder.svg",
            "seller_avatar": "logo_master",
        },
        {
            "id": 3,
            "title": "I will write SEO-optimized articles for your blog",
            "seller_name": "word_smith",
            "seller_level": "Level 1",
            "price": 50.0,
            "rating": 4.8,
            "reviews_count": 89,
            "delivery_time": 5,
            "image_url": "/placeholder.svg",
            "seller_avatar": "word_smith",
        },
        {
            "id": 4,
            "title": "I will be your social media manager",
            "seller_name": "social_guru",
            "seller_level": "New Seller",
            "price": 400.0,
            "rating": 4.7,
            "reviews_count": 32,
            "delivery_time": 30,
            "image_url": "/placeholder.svg",
            "seller_avatar": "social_guru",
        },
        {
            "id": 5,
            "title": "I will develop a responsive WordPress website",
            "seller_name": "web_dev_pro",
            "seller_level": "Top Rated",
            "price": 800.0,
            "rating": 5.0,
            "reviews_count": 210,
            "delivery_time": 7,
            "image_url": "/placeholder.svg",
            "seller_avatar": "web_dev_pro",
        },
        {
            "id": 6,
            "title": "I will do a professional voice over in English",
            "seller_name": "voice_over_ace",
            "seller_level": "Level 2",
            "price": 100.0,
            "rating": 4.9,
            "reviews_count": 550,
            "delivery_time": 1,
            "image_url": "/placeholder.svg",
            "seller_avatar": "voice_over_ace",
        },
    ]

    @rx.event
    def set_page(self, page: str):
        """Set the current page."""
        self.current_page = page