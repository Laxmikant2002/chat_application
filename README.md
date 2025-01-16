# Django Project

## Overview

This project is a Django-based web application with the following features:
- Responsive webpage with a fixed navbar, collapsible left menu, main content area, and right-side panel.
- User authentication (sign up, log in, log out).
- Chat application with WebSocket support.
- Integration with AWS Lambda for specific functionalities.

## Features

### Frontend Development
1. Responsive webpage with:
   - Fixed navbar
   - Three sections: left menu, main content area, right-side panel
   - Footer
   - Collapsible left menu
2. JavaScript function to adjust page width based on screen size.

### Django
1. User authentication (sign up, log in).
2. Display all registered users in a collapsible left menu.
3. Allow logged-in users to initiate a chat.
4. Store user data and chat messages in the database.
5. Retrieve and display old messages in the chat interface.
6. Use WebSocket for real-time chat.
7. User-friendly and functional chat interface.

### AWS
1. AWS Lambda function to add two numbers and return the result.
2. AWS Lambda function to store a document or PDF file in an S3 bucket.

## Setup

### Create Virtual Environment

#### Mac
```sh
python3 -m venv venv
source venv/bin/activate
```
## Windows
    ```sh
    python3 -m venv venv
    .\venv\Scripts\activate.bat
    ```
## Install Dependencies
    ```sh
    pip install --upgrade pip
    pip install -r requirements.txt
    ```
## Migrate to Database
    ```sh
    python manage.py migrate
    python manage.py createsuperuser
    ```
## Run Application
    ```sh
    python manage.py runserver
    ```