import requests

class AccessTokenNotFoundError(Exception):
    pass


def generate_access_token(client_id, client_secret, redirect_uri, code, accounts_url='https://accounts.zoho.eu'):
    url = f'{accounts_url}/oauth/v2/token'
    data = {
        'grant_type': 'authorization_code',
        'client_id': client_id,
        'client_secret': client_secret,
        'redirect_uri': redirect_uri,
        'code': code
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(url, data=data, headers=headers)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to generate access token: {err}")

    result = response.json()

    if 'access_token' not in result:
        raise AccessTokenNotFoundError("Access token not found in response. Please generate a new code and try again.")

    return result



def refresh_access_token(refresh_token, client_id, client_secret, accounts_url='https://accounts.zoho.eu'):
    url = f'{accounts_url}/oauth/v2/token'
    data = {
        'refresh_token': refresh_token,
        'client_id': client_id,
        'client_secret': client_secret,
        'grant_type': 'refresh_token'
    }
    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    response = requests.post(url, data=data, headers=headers)

    try:
        response.raise_for_status()
    except requests.exceptions.HTTPError as err:
        raise Exception(f"Failed to refresh access token: {err}")

    result = response.json()
    access_token = result.get('access_token')

    if access_token is None:
        raise AccessTokenNotFoundError("Access token not found in response. Please generate a new code and try again.")

    return access_token

