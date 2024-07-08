'''
Library for interacting with the PasteBin API
https://pastebin.com/doc_api
'''
import requests

PASTEBIN_API_POST_URL = 'https://pastebin.com/doc_api'
API_DEV_KEY = 'HNxK4FPDkHZgU93mrTqNkKpPOGrCf6Vm'

def post_new_paste(title, body_text, expiration='N', public=True):
    """Posts a new paste to PasteBin

    Args:
        title (str): Paste title
        body_text (str): Paste body text
        expiration (str): Expiration date of paste (N = never, 10M = minutes, 1H, 1D, 1W, 2W, 1M, 6M, 1Y)
        listed (bool): Whether paste is publicly listed (True) or not (False) 
    
    Returns:
        str: URL of new paste, if successful. Otherwise None.
    """    
    # TODO: Function body
    # Note: This function will be written as a group 

    params = {
        'api_dev_key': API_DEV_KEY,
        'api_option': 'paste',
        'api_paste_code': body_text,
        'api_paste_name': title,
        'api_paste_expire_date': expiration,
        'api_paste_private': 0 if public else 1,
    }

    print('Creating new API on PasteBin.')
    
    # Send the POST request
    response = requests.post(PASTEBIN_API_POST_URL, data=params)
    
    if response.status_code == 200:
        print('Paste created successfully.')
        return response.text
    else:
        print(f'Failed to create paste. Response code: {response.status_code}')
        return None