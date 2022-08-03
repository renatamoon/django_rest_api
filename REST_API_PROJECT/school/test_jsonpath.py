# STANDARD IMPORTS
import requests
import jsonpath

# doing request to the router
ratings = requests.get('http://localhost::8000/apí/v2/ratings/')

# getting all results
results = jsonpath.jsonpath(ratings.json(), 'results')

# getting the first element
first_result = jsonpath.jsonpath(ratings.json(), 'results[0]')

# getting the name of the first element
first_name_result = jsonpath.jsonpath(ratings.json(), 'results[0].name')

# getting the email of the first element
email_result = jsonpath.jsonpath(ratings.json(), 'results[0].email')

# getting the ratings of the first element
registered_rating = jsonpath.jsonpath(ratings.json(), 'results[0].ratings')

# course id
course = jsonpath.jsonpath(ratings.json(), 'results[0].course')

# all names of the registered ratings related
names = jsonpath.jsonpath(ratings.json(), 'results[*].name')

# all names of the registered ratings related
registered_ratings = jsonpath.jsonpath(ratings.json(), 'results[*].rating')
