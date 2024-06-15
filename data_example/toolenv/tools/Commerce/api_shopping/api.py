from security import safe_requests


def get_prices_of_tomatoes(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "This one will get prices from tomatoes"
    
    """
    url = f"https://api-shopping.p.rapidapi.com/shopping?item=tomatoes"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "api-shopping.p.rapidapi.com"
        }


    response = safe_requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

def get_prices_of_bananas(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "On this option, you can get a JSON file with the prices of bananas from TESCO"
    
    """
    url = f"https://api-shopping.p.rapidapi.com/shopping?item=banana"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "api-shopping.p.rapidapi.com"
        }


    response = safe_requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

