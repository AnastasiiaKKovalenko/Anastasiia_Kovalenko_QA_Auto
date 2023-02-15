import pytest
import requests


class GitHub:

    def get_user(self, username):
        url = f'https://api.github.com/users/{username}'
        response = requests.get(url)
        body = response.json()

        return body

    def search_repo(self, name):
        response = requests.get(f'https://api.github.com/search/repositories',
                                params={'q': name})
        body = response.json()

        return body
