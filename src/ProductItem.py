from dataclasses import dataclass, field

@dataclass
class ProductItem(Item):
    store: Optional[str] = field(default=None)
    name: Optional[str] = field(default=None)
    price: Optional[float] = field(default=None)
    link: Optional[str] = field(default=None)
