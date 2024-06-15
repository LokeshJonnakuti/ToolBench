from security import safe_requests


def buy_gmail_accounts_old_new_verified_instant_delivery(toolbench_rapidapi_key: str='088440d910mshef857391f2fc461p17ae9ejsnaebc918926ff'):
    """
    "Buy and sell old PVA Gmail accounts in bulk from Storegmail at super low price with 100% money back guarantee. You can buy bulk Gmail accounts or JUST ONE"
    
    """
    url = f"https://buy-gmail-accounts.p.rapidapi.com/"
    querystring = {}
    
    headers = {
            "X-RapidAPI-Key": toolbench_rapidapi_key,
            "X-RapidAPI-Host": "buy-gmail-accounts.p.rapidapi.com"
        }


    response = safe_requests.get(url, headers=headers, params=querystring)
    try:
        observation = response.json()
    except:
        observation = response.text
    return observation

