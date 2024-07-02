# Recipe Project

This Recipe Project is a web application designed to allow users to add, view, and interact with recipes. Built with Django for the backend and utilizing HTML, CSS, and JavaScript for the frontend, the application offers a seamless and engaging user experience.

## Features

- **Add Recipes**: Users can easily add their favorite recipes, complete with a list of ingredients.
- **Like Recipes**: Show appreciation for great recipes by liking them. All liked recipes are conveniently displayed on a dedicated "Liked" page.
- **Recipe Timer**: Each recipe page includes a built-in timer to help users manage their cooking time efficiently.
- **Video Integration**: Enhance your cooking experience by adding videos to recipes, providing visual instructions and tips.

## Setting Up the Project

### Prerequisites
- Ensure that Python is installed on your system. If not, download and install Python from [python.org](https://www.python.org/).

### Setting Up the Project on Windows

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

7. Install project dependencies:
    ```bash
    pip install -r requirements.txt
    ```

8. Generate SECRET_KEY in python shell:
    ```bash
    python manage.py shell
    from django.core.management.utils import get_random_secret_key
    print('SECRET_KEY=',get_random_secret_key())
    ```

9. Add SECRET_KEY in .env:
    ```bash
    SECRET_KEY= <YOUR GENERATED SECRET_KEY>
    EMAIL_HOST_USER = "<Your email Id>"
    EMAIL_HOST_PASSWORD = "<Your email app password>"
    LINK = <Your hosting link 'http://localhost:8000 (if using localhost)'>
    ```

10. Make changes in the database using makemigrations:
    ```bash
    python manage.py makemigrations
    ```

11. Update the actual database:
    ```bash
    python manage.py migrate
    ```

12. Create a superuser to access the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

13. Try running the server:
    ```bash
    python manage.py runserver
    ```

### Setting Up the Project on Linux

1. Install virtualenv:
    ```bash
    pip install virtualenv
    ```

2. Create a new virtual environment:
    ```bash
    python3 -m venv venv
    ```

3. Activate the virtual environment:
    ```bash
    source venv/bin/activate
    ```

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

7. Install project dependencies:
    ```bash
    pip install -r requirements.txt
    ```

8. Generate SECRET_KEY in python shell:
    ```bash
    python manage.py shell
    from django.core.management.utils import get_random_secret_key
    print('SECRET_KEY=',get_random_secret_key())
    ```

9. Add SECRET_KEY in .env:
    ```bash
    SECRET_KEY= <YOUR GENERATED SECRET_KEY>
    EMAIL_HOST_USER = "<Your email Id>"
    EMAIL_HOST_PASSWORD = "<Your email app password>"
    LINK = <Your hosting link 'http://localhost:8000 (if using localhost)'>
    ```

10. Make changes in the database using makemigrations:
    ```bash
    python manage.py makemigrations
    ```

11. Update the actual database:
    ```bash
    python manage.py migrate
    ```

12. Create a superuser to access the admin panel:
    ```bash
    python manage.py createsuperuser
    ```

13. Try running the server:
    ```bash
    python manage.py runserver
    ```

## Usage

- Visit `http://127.0.0.1:8000` in your web browser to access the application.
- Add recipes by clicking on the "Add Recipe" button and filling out the form.
- Like recipes by clicking the "Like" button on each recipe page.
- Use the timer on each recipe page to keep track of cooking times.
- Add videos to recipes for visual instructions.

## Contributing

Contributions are welcome! Please fork the repository and submit a pull request.

Happy Cooking!
