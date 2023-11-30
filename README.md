## Telegram News Bot

### Project Description:

A Python-based Telegram News Bot. It fetches news articles based on user-specified keywords and delivers them to users. The bot uses the Telegram Bot API, GNews API, and Python libraries for functionality.

### TODO

- [ ] add Redis for message queue handling
- [ ] allow users to choose publications
- [ ] handle empty response (if the keyword does not return any news)

### Features:
- **Keyword-Based News Retrieval**: Users can request news articles by sending a command with a keyword. The bot fetches the latest news related to the keyword.

- **Formatted News Delivery**: The bot formats news articles with titles, descriptions, publication dates, and publisher names. It delivers news in Markdown format for easy reading.

- **User-Friendly Commands**: The bot responds to commands like "/start" (to begin interaction), "/news [keyword]" (to request news), and "/help" (to view available commands).

- **Error Handling**: The bot handles errors and skips news items that fail validation to ensure a smooth experience.

### Technologies Used:
- Python
- Telebot (Telegram Bot API wrapper)
- GNews API
- Pydantic (Data validation and parsing)
- dotenv (Environment variable management)

### How to Use:
1. Clone this GitHub repository.
2. Set up a Telegram bot and get an API token.
3. Create a `.env` file with your Telegram bot token as `TELEGRAM_TOKEN`.
4. Install dependencies with `pip install -r requirements.txt`.
5. Run the bot script (`bot.py`) to start the Telegram bot.
6. Interact with the bot by sending commands like "/start", "/news [keyword]", and "/help" in your Telegram chat.

## How to use with with Docker Compose

- it will create and start the container in detached mode:

```bash
docker-compose up -d
```

- Stop and remove the container:
  
```
docker-compose down
```



## How to Use (with Docker):

To run the Telegram News Bot using Docker, follow these steps:

1. Clone this GitHub repository to your local machine.

2. Ensure you have Docker installed on your system.

3. Set up a Telegram bot and obtain an API token.

4. Create a `.env` file in the project directory and set the `TELEGRAM_TOKEN` variable with your Telegram bot token.

5. Open a terminal and navigate to the project directory.

6. Build a Docker image for the bot by running the following command:

   ```bash
   docker build -t tg-news-bot .
   ```

   This command uses the provided Dockerfile (`Dockerfile`) to build an image named `tg-news-bot`.

7. Once the image is built, you can run the bot using the following command:

   ```bash
   docker run -d --name tg-news-bot-instance tg-news-bot
   ```

   This command starts a Docker container named `tg-news-bot-instance` using the `tg-news-bot` image in detached mode (`-d`), which means it runs in the background.

8. The Telegram News Bot is now up and running inside the Docker container. You can interact with the bot by sending commands like "/start", "/news [keyword]", and "/help" in your Telegram chat.

9. To stop the bot and the Docker container, use the following command:

   ```bash
   docker stop tg-news-bot-instance
   ```

   This command stops the container without removing it. To remove the container after stopping it, run:

   ```bash
   docker rm tg-news-bot-instance
   ```

   To remove the Docker image when you no longer need it, use:

   ```bash
   docker rmi tg-news-bot
   ```

Now you can run and manage the Telegram News Bot using Docker for a containerized environment.


### Other projects like this

- https://github.com/ESWZY/telegram-news
- https://rss.app/bots/google-telegram-bot

### Disclaimer:
This project is for educational and informational purposes only. It does not endorse or promote any specific news source or content. Use responsibly and verify information from trusted sources.
