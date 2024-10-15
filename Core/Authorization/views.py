# views.py
import requests
from django.shortcuts import redirect
from django.conf import Settings, settings
from django.contrib.auth import login
from requests_oauthlib import OAuth2Session
from .models import CustomUser, Profile
from urllib.parse import urlencode
from django.http import JsonResponse
import jwt
def oauth_login(request):
    params = {
        'client_id': OAuth2Session(settings.APOLLO_CLIENT_ID),
        'redirect_uri': settings.APOLLO_REDIRECT_URI,
        'response_type': 'code',  # Change this depending on your requirement
    }
    query_string = urlencode(params)
    url = settings.APOLLO_AUTH_URL
    # Construct the final URL
    full_url = f"{url}?{query_string}"

    
     # Perform the GET request with parameters
     # Redirect with parameters
    return redirect(full_url)
    
   
def oauth_callback(request):
    #code = request.GET.get('code')
    code = 'LvtbyvK5z01hrNViH56Iq3E-RlYiLuGoS8xfRx-zNoY'
    token_url = settings.APOLLO_TOKEN_URL
    
    # Exchange code for access token
    response = requests.post(token_url, data={
        'client_id': settings.APOLLO_CLIENT_ID,
        'client_secret': settings.APOLLO_CLIENT_SECRET,
        'code': code,
        'redirect_uri': settings.APOLLO_REDIRECT_URI,
        'grant_type': 'authorization_code',
    })

    token_data = response.json()
    
    
    if 'access_token' in token_data:
        access_token = token_data['access_token']
        # Decode the token. You might want to specify the algorithms used
        payload = jwt.decode(access_token,Settings.secret_key, algorithms=["HS256"])
        # You can now use the access token to access Apollo.io APIs
        return JsonResponse({'access_token': access_token})
    else:
        #return JsonResponse({'error': token_data.get('error')}, status=400)
        return JsonResponse(data = token_data)