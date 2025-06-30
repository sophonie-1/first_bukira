# 🍋 Little Lemon Restaurant API

This project is a RESTful API built with Django REST Framework for **Little Lemon**, a fictional restaurant. The API supports menu item management, 
reservation handling, and user authentication—designed for frontend clients like mobile apps or web frontends.

## 🚀 Features

- 📋 CRUD operations for menu items
- 📅 Reservation creation and management
- 🔐 JWT-based user authentication (or session-based)
- 🧑‍🍳 Role-based access (e.g., staff can manage reservations)
- 🌐 Fully browsable API interface with DRF

## 🛠️ Tech Stack

- **Backend:** Django, Django REST Framework
- **Auth:** JWT / TokenAuth (based on implementation)
- **Database:** SQLite / PostgreSQL
- **Dev Tools:** Django Admin, DRF browsable API, Postman

## 📁 Project Structure
littlelemon/
├── menu/ # API for menu items
├── reservations/ # API for reservations
├── littlelemon_api/ # Project settings and URLs
├── requirements.txt
└── manage.py


```bash
git clone https://github.com/sophonie-1/first_bukira.git
cd first_bukira
cd Littlelemon
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt


these are endpoints for project
menu/ for Menu model
menu/<int:pk>/ for MenuItemView
restaurant/booking/ for Booking model
api-token-auth/ for generating user token
static-file/ for testing static files
