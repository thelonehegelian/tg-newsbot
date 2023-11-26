FROM python:3
WORKDIR /usr/src/tg-news
COPY . .

RUN ["pip", "install", "-r", "requirements.txt"]

CMD ["python", "-m", "src.main"]
