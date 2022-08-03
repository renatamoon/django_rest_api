# STANDARD IMPORT
import requests

headers = {'Authorization': 'Token 099cd66b13f62cb698873b7c7442c4ab821a2823'}
url_base_course = 'http://localhost:8000/api/v2/cursos/'


def test_get_cursos(self):
    response = requests.get(url=self.url_base_course, headers=self.headers)

    assert response.status_code == 200


def test_get_curso(self):
    response = requests.get(url=f'{self.url_base_course}12/', headers=self.headers)

    assert response.status_code == 200


def test_post_curso(self):
    new = {
        "titulo": "Curso de Programação com Ruby 345",
        "url": "http://www.geekuniversity.com.br/cpr234"
    }
    response = requests.post(url=self.url_base_course, headers=self.headers, data=new)

    assert response.status_code == 201
    assert response.json()['title'] == new['title']


def test_put_curso(self):
    updated = {
        "title": "Novo Curso de Ruby 34",
        "url": "http://www.geekuniversity.com.br/ncr34"
    }

    response = requests.put(url=f'{self.url_base_course}12/', headers=self.headers, data=updated)

    assert response.status_code == 200


def test_put_titulo_curso(self):
    updated = {
        "title": "Novo Curso de Ruby 225",
        "url": "http://www.geekuniversity.com.br/ncr225"
    }

    response = requests.put(url=f'{self.url_base_cursos}12/', headers=self.headers, data=updated)

    assert response.json()['title'] == updated['title']


def test_delete_curso(self):
    response = requests.delete(url=f'{self.url_base_cursos}12/', headers=self.headers)

    assert response.status_code == 204 and len(response.text) == 0
