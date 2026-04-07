# 🎯 Django Quiz Application

[![Django Version](https://img.shields.io/badge/Django-6.0.3-green.svg)](https://www.djangoproject.com/)
[![Bootstrap Version](https://img.shields.io/badge/Bootstrap-5.3-purple.svg)](https://getbootstrap.com/)
[![Python Version](https://img.shields.io/badge/Python-3.14-blue.svg)](https://www.python.org/)
[![License](https://img.shields.io/badge/License-MIT-red.svg)](LICENSE)
[![GitHub issues](https://img.shields.io/github/issues/codeit-sunny/Django-Quiz-Application.svg)](https://github.com/codeit-sunny/Django-Quiz-Application/issues)
[![GitHub stars](https://img.shields.io/github/stars/codeit-sunny/Django-Quiz-Application.svg)](https://github.com/codeit-sunny/Django-Quiz-Application/stargazers)

## 📖 Overview

**Django Quiz Application** is a modern, feature-rich online quiz platform built with Django Framework. It provides an interactive environment for users to test their knowledge, compete with others, and track their progress through an engaging leaderboard system.

### ✨ Features at a Glance

| Category | Features |
|----------|----------|
| **User Features** | Secure Authentication, Personalized Quiz, Real-time Feedback, Progress Tracking |
| **Quiz Features** | Multiple Choice Questions, Random Generation, One-time Attempt, Equal Marking |
| **Admin Features** | Full CRUD Operations, Inline Choice Management, Publication Control, Search & Filter |
| **Security** | CSRF Protection, Password Hashing, Session Management, XSS Prevention |

---

## 🚀 Live Demo

> **Repository:** [GitHub - codeit-sunny/Django-Quiz-Application](https://github.com/codeit-sunny/Django-Quiz-Application)

---

## 🛠️ Technology Stack

### Backend
| Technology | Version | Purpose |
|------------|---------|---------|
| Django | 6.0.3 | Web Framework |
| Python | 3.14+ | Programming Language |
| SQLite | 3.x | Database |
| django-crispy-forms | 2.6 | Form Styling |
| crispy-bootstrap5 | 2026.3 | Bootstrap 5 Integration |
| Pillow | 12.2.0 | Image Processing |

### Frontend
| Technology | Version | Purpose |
|------------|---------|---------|
| Bootstrap | 5.3 | UI Framework |
| Font Awesome | 6.5.1 | Icons |
| Google Fonts | - | Typography |
| AOS | 2.3.1 | Scroll Animations |

---

## 📋 Prerequisites

Before you begin, ensure you have the following installed:

- [Python](https://www.python.org/) 3.10 or higher
- [pip](https://pip.pypa.io/) (Python package manager)
- [Git](https://git-scm.com/) (Version control)
- Virtual Environment (recommended)

---

## 🔧 Installation Guide

### Step 1: Clone the Repository

```bash
git clone https://github.com/codeit-sunny/Django-Quiz-Application.git
cd Django-Quiz-Application
cd lets_quiz

📁 Project Structure

Django-Quiz-Application/
├── lets_quiz/              # Project configuration
│   ├── settings.py         # Django settings
│   ├── urls.py            # Main URL routing
│   └── wsgi.py            # WSGI configuration
├── quiz/                   # Main application
│   ├── migrations/        # Database migrations
│   ├── templates/         # HTML templates
│   ├── admin.py           # Admin interface
│   ├── models.py          # Database models
│   ├── views.py           # View controllers
│   ├── forms.py           # Form definitions
│   └── urls.py            # App URL routing
├── static/                # Static files (CSS, JS)
├── templates/             # Global templates
├── db.sqlite3            # SQLite database
└── manage.py             # Django management script

-> Access the Application
Open your browser and navigate to:

Main App: http://127.0.0.1:8000/

Admin Panel: http://127.0.0.1:8000/admin/
