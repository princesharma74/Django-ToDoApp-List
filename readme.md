# Django ToDoApp List

Django ToDoApp is a web application for managing tasks and to-do lists. It allows users to create, update, and delete tasks, as well as categorize them with tags. The application provides a RESTful API for accessing task data.

## Features

- Create, update, and delete tasks
- Categorize tasks with tags
- RESTful API for task management
- Basic authentication for API access
- API endpoints for retrieving task lists and details

## Installation

1. Clone the repository:

    `git clone https://github.com/princesharma74/Django-ToDoApp-List.git`

    `cd todoapp`

2. Create a virtual environment:

    `python -m venv env`

3. Activate the virtual environment:
     **On macOS and Linux:**

      `source env/bin/activate`

     **On Windows:**

     `.\env\Scripts\activate`

5. Install the dependencies:

    `pip install -r requirements.txt`
    
6. Set up the database:

    `python manage.py migrate`

7. Run the development server:

    `python manage.py runserver`



Access the application at http://localhost:8000/ in your web browser.

**API Endpoints**

    GET /api/ - Overview of available API endpoints.
    GET /api/task-list/ - Retrieve a list of all tasks.
    GET /api/task-detail/<str:pk>/ - Retrieve details of a specific task.
    POST /api/task-create/ - Create a new task.
    POST /api/task-update/<str:pk>/ - Update an existing task.
    DELETE /api/task-delete/<str:pk>/ - Delete a task.