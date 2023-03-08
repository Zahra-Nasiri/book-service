
# book-service

This is book-service of library project and has connection with [communication-lyer](https://github.com/Zahra-Nasiri/communication-layer)
 and [user-service](https://github.com/Zahra-Nasiri/user-service)
 projects.


## Environment Variables

To run this project, you will need to add the following environment variables to your .env file

`MONGO_DB_URL`

`DB`

`book_collection`


## Tech Stack

* python
* fastapi
* mongodb




## Installation

Install my-project with pip

```bash
  python -m venv venv
  venv\scripts\avtivate
  pip install -r requirements.txt
```

## Running Tests

To run tests, run the following command

```bash
  pytest
```


## Run Locally

Clone the project

```bash
  git clone https://github.com/Zahra-Nasiri/book-service
```

Go to the project directory

```bash
  cd book-service
```

Install dependencies

```bash
  python -m venv venv
  venv\scripts\avtivate
  pip install -r requirements.txt
```

Start the server

```bash
  uvicorn main:app --reload
```

## API Reference

#### Get all books

```http
  GET /
```

#### Get a signle book by id

```http
  GET /{book_id}
```

#### Delete a single book by id

```http
  DELETE /{book_id}
```

#### Create a book

```http
  POST /
```

#### Update a single book by id

```http
  PATCH /{book_id}
```

## Authors

- [Zahra-Nasiri](https://github.com/Zahra-Nasiri)


## 🚀 About Me
I'm a  back-end developer...

you can read more about me on my [linkedin account](https://www.linkedin.com/in/zahra-nasirmohammadi-73584b241/)
