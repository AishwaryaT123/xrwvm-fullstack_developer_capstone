# 🚗 Cars Dealership - Full Stack Capstone Project

A full-stack web application for **Cars Dealership**, a national car retailer in the U.S. Built as part of the IBM Full-Stack Cloud Development Capstone.

## Project Overview

This application allows users to:
- Browse dealership branches across the U.S.
- View and submit reviews for dealerships
- Filter dealers by state
- Perform sentiment analysis on reviews using Watson NLU

## Tech Stack

| Layer | Technology |
|-------|------------|
| Frontend | React.js |
| Backend | Django + Flask |
| Database | MongoDB + SQLite |
| Sentiment Analysis | Watson NLU (IBM Cloud) |
| Containerization | Docker |
| Orchestration | Kubernetes |
| Deployment | IBM Cloud Code Engine |
| CI/CD | GitHub Actions |

## Project Structure

```
agfzb-fullStack-Cloud-Devlopment/
├── server/
│   ├── djangoapp/           # Django app (models, views, urls)
│   ├── djangoproj/          # Django project settings
│   ├── database/            # MongoDB microservice (Node.js)
│   ├── microservices/
│   │   └── Watson_NLU/      # Sentiment analysis microservice
│   └── frontend/
│       ├── static/          # HTML static pages (About, Contact)
│       └── src/
│           └── components/  # React components
│               ├── Register/
│               ├── Dealers/
│               └── Header/
├── .github/
│   └── workflows/           # CI/CD GitHub Actions
└── README.md
```

## Setup & Run

### 1. Clone the repository
```bash
git clone https://github.com/AishwaryaT123/agfzb-fullStack-Cloud-Devlopment.git
cd agfzb-fullStack-Cloud-Devlopment
```

### 2. Backend (Django)
```bash
cd server
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```

### 3. Frontend (React)
```bash
cd server/frontend
npm install
npm start
```

### 4. Database Microservice (MongoDB)
```bash
cd server/database
npm install
node app.js
```

### 5. Sentiment Microservice
```bash
cd server/microservices/Watson_NLU
pip install -r requirements.txt
python app.py
```

## Features
- ✅ User Registration & Login
- ✅ View all dealerships
- ✅ Filter dealerships by state
- ✅ View dealer reviews
- ✅ Post reviews (authenticated users)
- ✅ Sentiment analysis on reviews
- ✅ Admin panel
- ✅ CI/CD with GitHub Actions
- ✅ Deployed on IBM Cloud Code Engine
