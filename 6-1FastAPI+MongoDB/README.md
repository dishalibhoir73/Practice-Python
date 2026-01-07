---

# FastAPI CRUD with MongoDB

## Description

A basic CRUD (Create, Read, Update, Delete) REST API built using **FastAPI** and **MongoDB** as part of a hands-on assignment.

---

## Tech Stack

* Python
* FastAPI
* MongoDB
* PyMongo
* Uvicorn

---

## Project Structure

```
.
├── main.py
├── routers/
├── models/
├── schemas/
├── config/
├── tests/
└── README.md
```

---

## Setup & Run

### 1. Create virtual environment

```bash
python -m venv venv
```

Activate:

```bash
.\venv\Scripts\Activate.ps1
```

---

### 2. Install dependencies

```bash
python -m pip install fastapi uvicorn pymongo
```

---

### 3. Run server

```bash
uvicorn main:app --reload
```

## API Docs

```
http://127.0.0.1:8000/docs
```

---
