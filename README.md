# AI Engineer Journey

My practice repo for learning to become an AI engineer. Each folder holds small exercises and projects, added as I learn.

## Contents

| Folder | What it covers |
|---|---|
| [`python/library-management`](python/library-management) | A library system practicing classes, properties, inheritance, dunder methods, and dataclasses |
| [`python/files`](python/files) | File handling practice: reading in chunks, writing, binary copy |
| [`python/JSON`](python/JSON) | JSON practice: `load`, `dump`, `loads`, `dumps`, and error handling |
| [`python/contact-book`](python/contact-book) | A contact book CLI with JSON storage, logging, custom exceptions, and `.env` config |
| [`python/type-hinting`](python/type-hinting) | Type hints, `mypy`, and Pydantic validation practice |

## Roadmap

- [x] Python OOP (classes, inheritance, dunder methods, dataclasses)
- [x] Files, JSON, exceptions, logging
- [x] Virtual environments, `requirements.txt`, `.env` files
- [ ] Type hints and Pydantic (in progress)
- [ ] CLI expense tracker
- [ ] FastAPI
- [ ] PostgreSQL
- [ ] LLMs and vector databases
- [ ] Deployment

## How to run a project

Each project folder has its own setup. For projects with a `requirements.txt`:

    cd python/<project-folder>
    python -m venv .venv
    .venv\Scripts\Activate.ps1
    pip install -r requirements.txt

(These are PowerShell commands for Windows.)