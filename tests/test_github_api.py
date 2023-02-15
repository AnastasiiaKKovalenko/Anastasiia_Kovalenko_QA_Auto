import pytest


@pytest.mark.api
def test_user_exists(github_api):
    user_response = github_api.get_user('defunkt')
    assert user_response['login'] == 'defunkt'


@pytest.mark.api
def test_user_not_exists(github_api):
    user_response = github_api.get_user('butenkosergii')
    assert user_response['message'] == 'Not Found'


@pytest.mark.api
def test_repo_can_be_found(github_api):
    repo_response = github_api.search_repo('become-qa-auto')
    assert repo_response['total_count'] == 31


@pytest.mark.api
def test_repo_cannot_be_found(github_api):
    repo_non_exist = github_api.search_repo('sergiibutenko_repo_non_exist')
    assert repo_non_exist['total_count'] == 0
