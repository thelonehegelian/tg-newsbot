from pydantic import BaseModel
from typing import List, Dict


class NewsItem(BaseModel):
    title: str
    description: str
    published_date: str
    url: str
    publisher: Dict[str, str]


class NewsFeed(BaseModel):
    news_items: List[NewsItem]
