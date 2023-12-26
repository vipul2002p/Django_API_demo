# views.py
from django.http import HttpResponse,JsonResponse
from django.shortcuts import render
from django.http import JsonResponse
from django.middleware.csrf import get_token
def home_page(request):
    print("home page requested")
    friends = ['ankit', 'ravi', 'uttam']
    return JsonResponse(friends, safe=False)

def userForm(request):
    return render(request, "index.html")

def fetchdata(request):
    if request.method == 'POST':
        # Process the form data
        username = request.POST.get('username')
        password = request.POST.get('password')

        # Perform any processing with the data, for example, pass it to the data.html template
        context = {
            'username': username,
            'password': password,
        }

        return render(request, "data.html", context)

    return HttpResponse("Invalid request")

def get_csrf_token(request):
    csrf_token = get_token(request)
    return JsonResponse({'csrf_token': csrf_token})