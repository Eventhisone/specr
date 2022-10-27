
## SPECR


SPECR is an open source application for finding and viewing string patterns for both tennis and racquetball.
It's purpose is to make it easy to find the pattern for a particular racquet and to act as a reference during stringing.


## Motivation

When I first started stringing, I noticed that patterns aren't readily available. When I discovered a repository of patterns I found that the UI was no responsive and annoying to use while stringing.

The purpose of the this project is to be able to easily pull up stringing patterns. I hope this will also act as an archive of stringing pattterns.


## Tech Stack

<b>Built with</b>
- [Flask](https://flask.palletsprojects.com/)
- [ReactJS](https://reactjs.org/)


## Features

Coming soon...

## Installation

## Run Locally

Clone the project

```bash
  git clone git@github.com:Eventhisone/specr.git
```

Go to the project directory

```bash
  cd my-project
```

Build the docker containers

```bash
  docker build -f Dockerfile.api -t react-flask-app-api .
  docker build -f Dockerfile.api -t react-flask-app-client .
```

Start the containers

```bash
  docker compose up -d
```

View the client at `localhost:3000` and view the api at `localhost:5000`

### DB

DB Upgrade process:

```bash
docker-compose exec api flask db revision --autogenerate --message "<meesage>"
docker-compose exec api flask db stamp head
docker-compose exec api flask db migrate   
docker-compose exec api flask db upgrade
```

## API Reference

Coming soon...

## Tests

Coming soon...

## How to use?
If people like your project they’ll want to learn how they can use it. To do so include step by step guide to use your project.

## Contribute

Let people know how they can contribute into your project. A [contributing guideline](https://github.com/zulip/zulip-electron/blob/master/CONTRIBUTING.md) will be a big plus.

## License

[License](https://github.com/eventhisone/specr/blob/master/LICENSE.md)