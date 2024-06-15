from security import safe_requests


def kooed_endpoint_copy(kooed: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Kooed Radio Stations end point"
    
    """
    url = f"https://kooed.p.rapidapi.com/"
    querystring = {}
    if kooed:
        querystring['Kooed'] = kooed
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kooed.p.rapidapi.com"
        }


    response = safe_requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def kooed_endpoint(kooed: str=None, toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Kooed Radio Stations end point"
    
    """
    url = f"https://kooed.p.rapidapi.com/"
    querystring = {}
    if kooed:
        querystring['Kooed'] = kooed
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "kooed.p.rapidapi.com"
        }


    response = safe_requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

