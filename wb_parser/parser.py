from dataclasses import dataclass

@dataclass
class Product:
    url: str = ''
    article: str = ''
    name: str = ''
    price: float = 0.0
    description: str = ''
    image_urls: str = ''
    characteristics: dict[str, str] = None
    seller_name: str = ''
    seller_url: str = ''
    sizes: str = ''
    stock: int = 0
    rating: float = 0.0
    reviews_count: int = 0

    def __post_init__(self):
        if self.characteristics is None:
            self.characteristics = {}