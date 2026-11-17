# Contact Book CLI

A menu-driven contact manager that stores contacts in a JSON file, with logging and custom exceptions.

## Features

- Add, list, search, and delete contacts
- Contacts are saved to JSON after every change and loaded on startup
- Case-insensitive duplicate check and search
- Custom exceptions (`ContactNotFoundError`, `DuplicateContactError`)
- Events and errors logged to `app.log`
- Data file path set through a `.env` file

## Setup

    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install -r requirements.txt
    copy .env.example .env

## Run

    python contact_book.py

## Configuration

| Variable | Default | Meaning |
|---|---|---|
| `DATA_FILE` | `contacts.json` | Where contacts are stored |

## What I practiced

Dataclasses, custom exceptions, file handling, JSON, logging, `pathlib`, and environment variables with `python-dotenv`.