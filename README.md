# CarServ — Car Service & Repair Management Platform

A full-stack web application for managing a car service business, built as a diploma project. It gives service owners a way to manage content and lets customers browse services and leave reviews.

**Live demo:** https://eugezavi-diploma-carserv.onrender.com/

---

## About this project

CarServ was built and developed by **Eugene Zavirukha**, 14, as a diploma project. The backend, database structure, and deployment setup were built from scratch in Django; the frontend is styled with Bootstrap 5.

---

## Features

- **Dynamic content** — services, testimonials, and contact details are stored in the database (SQLite locally, PostgreSQL in production) instead of hardcoded in templates, so they can be updated without touching code.
- **Clean app structure** — all Django apps live inside a dedicated `apps/` directory rather than the project root, keeping the codebase organized as it grows.
- **Authenticated reviews** — the contact page includes a review section restricted to logged-in users, which cuts down on spam and automatically attaches the reviewer's username without asking them to type it in.
- **Custom error pages** — branded 404 and 500 pages instead of Django's defaults.
- **Production-ready config** — environment variables handle secrets and database URLs, with separate settings for local development and the Render deployment.

---

## Tech stack

| Layer | Tools |
|---|---|
| Backend | Python 3.12, Django 5.1 |
| Frontend | HTML5, CSS3, SCSS, Bootstrap 5, JavaScript |
| Database | SQLite (local), PostgreSQL (production) |
| Deployment | Render, WhiteNoise (static files), dj-database-url |

---

## Security & deployment notes

- Secrets, the database URL, and `DEBUG` are all read from environment variables — none of them are committed to the repository.
- `make_superuser.py` is a small script written specifically for Render's free tier, so a superuser account exists automatically whenever the database gets reset on deploy.

![Report](static/img/car-repair-html-template.webp)
