# STANDARD IMPORTS
import requests

# GET RATINGS
ratings = requests.get('http://localhost:8000/api/v2/rartings')

# ----- Accessing the status code HTTP
# data_status_code = ratings.status_code

# ----- Passing the data to jsonable
# json_data = ratings.json()

# ----- quantity of registers
# register_quantity = ratings.json()['count']

# ----- next page of registers
# next_page = ratings.json()['next']

# ----- page results
# page_results = ratings.json()['results']

# ----- first element of the results list
# page_results = ratings.json()['results'][0]

# ----- last element of the results list
# page_results = ratings.json()['results'][-1]

# ----- last element of the results list by the person who made it
# page_results = ratings.json()['results']['name']

# GET RATING
rating = requests.get('http://localhost:8000/api/v2/rartings/7')

json_data = ratings.json()

# GET COURSES

headers = {'Authorization': 'Token 1836754829273634bjasghdg7346456564'}

courses = requests.get('http://localhost:8000/api/v2/courses', headers=headers)
courses_statuscode = courses.status_code
courses_json = courses.json()
