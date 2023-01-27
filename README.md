# quick-zip-bot

![GitHub](https://img.shields.io/github/license/svex99/quick-zip-bot)
![Github](https://img.shields.io/static/v1?label=python&message=3.10.0&color=succes)
![Github](https://img.shields.io/static/v1?label=&message=asyncio&color=informational)
![Github](https://img.shields.io/static/v1?label=&message=telethon&color=informational)

Minimalist Telegram bot to zip files.

## Features

- Full async, not blocking I/O.

- Concurrent download and zipping of files.

## Usage

1. Send the command `/add`, this notifies the bot that you are going to send some files to zip in a single file.
2. Send the files (photos, videos, documents, etc.) you want to add, total size must not exceed 1.95 GB.
3. Send `/zip <filename>` command where filename (admitted characters: A-Za-z0-9_) is the name of the zip you want to get. Ex: `/zip summer_photos` will create a zip file with name `summer_photos.zip`.

Send `/cancel` instead of `/zip` if you want to finish the process and not create the zip file.

## Deployment

### Environment Variables

You need to define the environment variables required for the bot to work. Where or how to define them depends on the method used to run the bot. You can use locally an .env file like `.env.example`.

|  Variable   | Required  |                               Description                                |
| :---------: | :-------: | :----------------------------------------------------------------------: |
|  `API_ID`   |    yes    |       Your personal Telegram API ID from https://my.telegram.org.        |
| `API_HASH`  |    yes    |      Your personal Telegram API hash from https://my.telegram.org.       |
| `BOT_TOKEN` |    yes    | The token of your bot created with [@botfather](https://t.me/botfather). |
| `CONC_MAX`  | default=3 |            Max amount of files to be downloaded concurrently.            |

### Locally

Create a virtual environment to install the dependencies isolated of other projects you are working on.

```
$ python -m venv env
$ source env/bin/activate
```

Install the dependencies and run the bot.

```
$ pip install -r requirements.txt
$ python src/bot.py
```

### Docker

Build the image with the provided Dockerfile.

```
$ docker image build -t quick-zip-bot .
```

Run the image with your .env file.

```
$ docker container run -d --name quick-zip-bot --env-file .env quick-zip-bot
```

### Railway

> 500h/month for free, no credit card required

1. Fork this repository to your GitHub account, and give it a star :).
2. Login or create your [Railway](https://railway.app) account as needed.
3. Create a new project on Railway by choosing `GitHub Repo` option and selecting the repository you forked on step 1.
4. Click the new project created and go to `Variables` section, where you must set the environment variables.
5. You are ready to use the bot when deployment is ready, this may take a bit.

## Contribute

I'll be happy to receive any issue or pull request to improve the bot, fell free to contribute.
