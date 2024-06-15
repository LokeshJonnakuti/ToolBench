from security import safe_requests


def get_top_songs(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "tujhe dekha toh as of now"
    
    """
    url = f"https://getsongs.p.rapidapi.com/getTopSongs"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "getsongs.p.rapidapi.com"
        }


    response = safe_requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

