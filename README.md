# RECIPE NEST

## Setting Up the Project on Windows

### Prerequisites
- Ensure that Python is installed on your system. If not, download and install Python from [python.org](https://www.python.org/).

### Setting Up Virtual Environment

1. Install virtualenv:
    ```bash
    pip install virtualenv
    ```

2. Create a new virtual environment:
    ```bash
    python -m venv venv
    ```

3. Activate the virtual environment:
    ```bash
    .\venv\Scripts\activate
    ```

### Initializing Dependencies and Running the Server

4. Install Django in the virtual environment:
    ```bash
    pip install Django
    ```

5. Fork the main repository and Clone your forked repository:
    ```bash
    git clone https://github.com/<your username>/recipe.git
    ```

6. Navigate to the project directory:
    ```bash
    cd recipe
    ```

8. Install project dependencies:
    ```bash
    pip install -r requirements.txt
    ```

#### There's a need for initializing SECRET_KEY and .env.

1. Generate SECRET_KEY in python shell(python manage.py shell):
    ```bash
    from django.core.management.utils import get_random_secret_key
    print('SECRET_KEY=',get_random_secret_key())
    ```

2. Add SECRET_KEY in .env :
    
    ```bash
    SECRET_KEY= <YOUR GENERATED SECRET_KEY>
    EMAIL_HOST_USER = "<Your email Id>"
    EMAIL_HOST_PASSWORD = "<You email app password>" 

    LINK = <Your hosting link 'http://localhost:8000 (if using localhost)'>
    ```

9.  Make changes in database using makemigrations:
    ```bash
    python manage.py makemigrations
    ```

10. Update the actual database:
    ```bash
    python manage.py migrate
    ```

11. Create Superuser to access admin panel
    ```bash
    python manage.py createsuperuser
    ```

12. Try running the server:
    ```bash
    python manage.py runserver
    ```
