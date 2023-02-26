import requests


def get_all_leads(access_token):
    headers = {
        'Authorization': 'Zoho-oauthtoken ' + access_token,
    }

    url = 'https://www.zohoapis.eu/crm/v2/Leads'

    leads = []
    page = 1

    while True:
        params = {
            'page': page,
            'per_page': 200
        }

        response = requests.get(url, headers=headers, params=params)

        if response.status_code == 200:
            leads += response.json()['data']
            info = response.json()['info']
            if not info['more_records']:
                break
        else:
            print(f"Error {response.status_code}: {response.json()['message']}")
            return None

        page += 1

    return leads
