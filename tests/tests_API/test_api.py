import allure
import requests
import pytest

BASE_URL = "https://jsonplaceholder.typicode.com"


@allure.title('Get API of all users')
def test_get_all_users():
    response = requests.get(f"{BASE_URL}/users")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
    assert len(response.json()) > 0


@pytest.mark.parametrize('user_id', (1, 3, 5))
@allure.title('Get users by id')
def test_get_user_by_id(user_id):
    response = requests.get(f"{BASE_URL}/users/{user_id}")
    assert response.status_code == 200
    user_data = response.json()
    assert user_data['id'] == user_id
    assert 'name' in user_data


@allure.title('Create post')
def test_create_post():
    payload = {
        "title": "Create new user",
        "body": "He is a man",
        "userId": 5
    }
    response = requests.post(f"{BASE_URL}/posts", json=payload)
    assert response.status_code == 201
    post_data = response.json()
    assert 'id' in post_data
    assert post_data['title'] == payload['title']
    assert post_data['body'] == payload['body']


@pytest.mark.parametrize('post_id', (12, 43, 84))
@allure.title('Test delete posts')
def test_delete_post(post_id):
    response = requests.delete(f"{BASE_URL}/posts/{post_id}")
    assert response.status_code == 200
