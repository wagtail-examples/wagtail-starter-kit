# Wagtail Starter Kit

This is a starter kit for a Wagtail project. It includes a Docker setup for local development, a basic project structure, and some useful tools and libraries.

## Features

- Docker setup for local development
- Basic project structure
- Makefile for common tasks
- SQLite, PostgreSQL, or MySQL support

## Getting started

1. Clone this repository [https://github.com/wagtail-examples/wagtail-starter-kit.git](https://github.com/wagtail-examples/wagtail-starter-kit.git) to a location on your computer
2. Change into the project directory
3. Run `make build` to build the Docker containers
4. Run `make up` to start the Docker containers
5. Run `make migrate` to apply database migrations
6. Run `make createsuperuser` to create a superuser
7. Run `make run` to start the Django development server

### Quick start

There is a make command to run most of the steps above in one go:

```bash
make quickstart
```

You'll need to run `make superuser` separately.

## View the site

The site will be available at [http://localhost:8000](http://localhost:8000).

The Wagtail admin interface will be available at [http://localhost:8000/admin](http://localhost:8000/admin).

## Choose a databse (optional)

By default, the project uses PostgreSQL. If you'd like to use MySQL or Sqlite3 instead uncomment the required `DC` variable in the Makefile and comment out the others.
