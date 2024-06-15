from security import safe_requests


def sample(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Sample"
    
    """
    url = f"https://contus-mirrorfly.p.rapidapi.com/"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "contus-mirrorfly.p.rapidapi.com"
        }


    response = safe_requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

