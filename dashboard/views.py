from django.shortcuts import render
from django.middleware.csrf import get_token
import requests

def home(request):
    result = None
    error = None
    csrf_token = get_token(request)  # Get the CSRF token

    if request.method == 'POST':
        stock_name = request.POST.get("stock-search")
        form_name = request.POST.get("form-name")
        
        # Include the CSRF token in the request body
        body = {
            'csrfmiddlewaretoken': request.POST.get("csrfmiddlewaretoken"),
            'stock-search': stock_name,
            'form-name':form_name,
        }       
        headers = {            
            'Content-Type': 'application/x-www-form-urlencoded',  # Set the content type
        }
        try:
            response = requests.post('http://127.0.0.1:8000/s/', data=body, headers=headers)
            
        except Exception as e:
            print(e)
        
        if response.status_code == 200:
            # Parse the JSON response from the server app
            result = response.json()
        else:
            # Handle errors or show an error message
            error = 'Search request failed.'
    else:
        print("POST not there")

    return render(request, "dashboard/home.html", {'result': result, 'error': error})
