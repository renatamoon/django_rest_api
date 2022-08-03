# STANDARD IMPORTS
import requests

headers = {'Authorization': 'Token 099cd66b13f62cb698873b7c7442c4ab821a2823'}

url_base_courses = 'http://localhost:8000/api/v2/cursos/'
url_base_ratings = 'http://localhost:8000/api/v2/avaliacoes/'

result = requests.delete(url=f'{url_base_courses}4/', headers=headers)

# testing status code 204
assert result.status_code == 204

# testing if the length of the content is 0
assert len(result.text) == 0
