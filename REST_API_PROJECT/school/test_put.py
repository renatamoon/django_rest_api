# STANDARD IMPORTS
import requests

headers = {'Authorization': 'Token 099cd66b13f62cb698873b7c7442c4ab821a2823'}

url_base_courses = 'http://localhost:8000/api/v2/cursos/'
url_base_ratings = 'http://localhost:8000/api/v2/avaliacoes/'


new_course = {
    "title": "Scrum Projects 3",
    "url": "http://www.geekuniversity.com.br/scrum2"
}

result = requests.put(url=url_base_courses, headers=headers, data=new_course)

# Testing status code 200
assert result.status_code == 200

# Testing if the title of the course if is returned
assert result.json()['title'] == new_course['title']
