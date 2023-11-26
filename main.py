import os
import telebot
from dotenv import load_dotenv
from gnews import GNews
from pydantic import BaseModel, ValidationError
from typing import List, Dict

# Load environment variables
load_dotenv()
TELEGRAM_TOKEN = os.getenv("TELEGRAM_TOKEN")
if not TELEGRAM_TOKEN:
    raise ValueError("TELEGRAM_TOKEN is not set in the environment")

# Initialize bot
bot = telebot.TeleBot(str(TELEGRAM_TOKEN))

print("Running bot")

google_news = GNews()


class NewsItem(BaseModel):
    title: str = ""
    description: str = ""
    published_date: str = ""
    url: str = ""
    publisher: Dict[str, str] = {}


class NewsFeed(BaseModel):
    news_items: List[NewsItem]


def get_news_by_keyword(keyword, num_results=5):
    data = google_news.get_news(keyword)
    news_items = []
    if data is None:
        return NewsFeed(news_items=news_items)
    for item in data:
        try:
            news_item = NewsItem(**item)
            news_items.append(news_item)
        except ValidationError as e:
            print(f"Skipping item due to validation error: {e}")
            continue
    return NewsFeed(news_items=news_items[:num_results])


def format_news(news):
    if news is None or not news.news_items:
        return "No news found"
    formatted_news = []
    for news_item in news.news_items:
        news_text = (
            f"*Title*: [{news_item.title}]({news_item.url})\n"
            f"*Description*: {news_item.description}\n"
            f"*Published Date*: {news_item.published_date}\n"
            f"*Publisher*: {news_item.publisher.get('name', 'N/A')}\n"
        )
        formatted_news.append(news_text)
    return "\n".join(formatted_news)


@bot.message_handler(commands=["start"])
def send_welcome(message):
    bot.reply_to(message, "Hello! I'm your friendly bot.")


@bot.message_handler(commands=["news"])
def send_news(message):
    keyword = message.text.partition(" ")[2]  # Assuming keyword follows command
    print("Getting news for keyword: " + keyword)
    news = get_news_by_keyword(keyword)
    formatted_news = format_news(news)
    print("Formatted news: " + formatted_news)
    bot.reply_to(message, formatted_news, parse_mode="Markdown")


@bot.message_handler(commands=["help"])
def send_help(message):
    help_text = "Available commands: /start, /news [keyword], /help"
    bot.reply_to(message, help_text)


@bot.message_handler(func=lambda m: True)
def echo_all(message):
    bot.reply_to(message, "Echo: " + message.text)


# Start polling
bot.polling()
