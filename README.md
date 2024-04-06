# ATS Recruiter API System

## Overview
This project is a Candidate Management System developed using Django, Django REST Framework, and SQLite. It provides APIs for managing candidates, including CRUD operations and search functionalities.

## Features
- **Candidate Management**: Create, Read, Update candidates
- **Search Functionality**: Search for candidates based on various criteria such as name, email, phone number, age, salary, and years of experience.
- **Validation**: Validation of candidate information such as phone number and email address.
- **Default Status**: Default status ('Applied') is assigned to candidates if not provided during creation.
- **Optimized Name Search**: API for searching candidates by name with relevance-based sorting.

## Setup
To set up the project locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/prihit/ats_recruiter_api.git
    ```

2. Install dependencies:
    ```bash
    pip install -r requirements.txt
    ```

3. Apply database migrations:
    ```bash
    python manage.py migrate
    ```

4. Run the development server:
    ```bash
    python manage.py runserver
    ```

## API Endpoints
- **Create Candidate**: `/api/create` (POST)
  - Description: API endpoint for creating a candidate. Data needs to be passed as request body payload.
  
- **Get Candidate Data**: `/api/candidate/<int:candidate_id>` (GET)
  - Description: API endpoint for retrieving candidate data by candidate ID. Used for testing candidate data.
  
- **Update Candidate Status**: `/api/candidate/<int:candidate_id>/update-status` (PATCH)
  - Description: API endpoint for updating the status of a candidate for the given candidate ID.
  
- **Candidate Search**: `/api/candidate_search/` (GET)
  - Description: API endpoint for searching/filtering candidates based on different fields. Fields and values need to be sent as query parameters.
  
- **Name Search**: `/api/candidate_namesearch/` (GET)
  - Description: API endpoint for searching candidates by name and returning data in order of relevance. Name is required to be passed as query parameter

## Technologies Used
- Python
- Django
- Django REST Framework
- SQLite

