# Django API Project with Material-Admin Theme

Welcome to the Django API project, a RESTful web API built using Django, Django Rest Framework, and secured with Django Rest Framework SimpleJWT. The project also features a customized admin interface using the Material-Admin theme.

## Table of Contents
- [Introduction](#introduction)
- [Features](#features)
- [Technologies Used](#technologies-used)
- [Installation](#installation)
- [Usage](#usage)
- [Customization](#customization)
- [Contributing](#contributing)
- [License](#license)

## Introduction

This project is a Django-based API backend that utilizes Django Rest Framework for building RESTful APIs. It includes authentication using Django Rest Framework SimpleJWT and features a customized admin interface with the Material-Admin theme.

## Features

- RESTful API endpoints for various functionalities
- JWT-based authentication for secure access
- Customized admin interface with Material-Admin theme

## Technologies Used

- Django
- Django Rest Framework
- Django Rest Framework SimpleJWT
- Material-Admin theme

## Installation

1. **Clone the repository:**

    ```bash
    git clone https://github.com/your-username/your-django-api-project.git
    cd your-django-api-project
    ```

2. **Create a virtual environment:**

    ```bash
    python -m venv venv
    ```

3. **Activate the virtual environment:**

    - On Windows:

      ```bash
      venv\Scripts\activate
      ```

    - On macOS/Linux:

      ```bash
      source venv/bin/activate
      ```

4. **Install dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

5. **Run migrations:**

    ```bash
    python manage.py migrate
    ```

## Usage

1. **Run the development server:**

    ```bash
    python manage.py runserver
    ```

    The API will be accessible at [http://localhost:8000](http://localhost:8000) by default.

2. **Access the admin interface:**

    Open your web browser and navigate to [http://localhost:8000/admin](http://localhost:8000/admin) to use the customized Material-Admin theme.

## Customization

To customize the Material-Admin theme or make changes to the API, refer to the project's codebase. Explore the `templates` directory for admin theme customization and the `views.py` and `serializers.py` files for API-related modifications.

## Contributing

We welcome contributions from the community. If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request.
