# STANDARD IMPORTS
import requests

headers = {'Authorization': 'Token: 18746399dfhhjfcjmdkjklfjedlpçedfd'}

url_base_courses = 'http://localhost:8000/api/v2/courses'
url_base_ratings = 'http://localhost:8000/api/v2/rartings'

courses_result = requests.get(url=url_base_courses, headers=headers)
ratings_result = requests.get(url=url_base_ratings, headers=headers)

result_courses = courses_result.json()
result_ratings = ratings_result.json()

# testing if the endpoint is correct
assert result_courses.status_code == 200
assert result_ratings.status_code == 200

# testing the quantity of registers
assert result_ratings.json()['count'] == 21
assert result_courses.json()['count'] == 2

# testing if the title of the first course is correct
assert result_ratings.json()['result'][0]['title'] == 'Criação de API Rest com Django REST Framework'
