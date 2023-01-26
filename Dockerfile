FROM python:3.10.6

WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python", "src/bot.py" ]
