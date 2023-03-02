from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def say_hello(request):
    return HttpResponse("Hello World")


def homepage(request):
    return HttpResponse("Welcome to Little Lemon restaurant!")


from datetime import datetime
def display_date(request):
    date_joined = datetime.today().year
    return HttpResponse(date_joined)


def menu(request):
    text = """<h1 style="color: #F4CE14;"> This is Little Lemon again!</h1>"""
    return HttpResponse(text)


# Week 2-1: Creating Requests and Responses
def home(request):
    '''
    path = request.path
    response = HttpResponse("This works!")
    return response
    '''
    # return HttpResponse(path, content_type='text/html', charset='utf-8')
    path = request.path
    scheme = request.path
    method = request.method
    address = request.META['REMOTE_ADDR']
    user_agent = request.META['HTTP_USER_AGENT']
    path_info = request.path_info

    # to update the header information
    response = HttpResponse()
    response.headers['Age'] = 20

    msg = f"""
            <br>Path: {path}
            <br>Address: {address}
            <br>Scheme: {scheme}
            <br>Method: {method}
            <br>User agent: {user_agent}
            <br>Path info: {path_info}
            <br> Response header: {response.headers} # update header part
            """
    # response = HttpResponse("This works!")
    # return response
    
    # return response # run it, see the text displayed in the browser
    return HttpResponse(msg, content_type='text/html', charset='utf-8')


# Week 2-3 Mapping URLs with Params
def menuitems(request, dish): # I need to pass additional argument after request, this argument will be passed inside the url.py file (app level?)
    items = {
        "pasta": "Pasta is a type of noddle made from combination of...",
        "falafel": "Flafel are deep fried patties or balls made from...",
        "cheesecake": "Cheesecake is a type of dessert made with..."
    }
    description = items[dish]
    return HttpResponse(f"<h2> {dish} </h2>" + description) # -> return HttpResponse("<h1> %s </h1>", "%query")


# Week 2: Exercise: Mapping URLs with Params
def drinks(request, drink_name):
    drinks = {
        "mocha": "type of coffee",
        "tea": "type of beverage",
        "lemonade": "type of refreshment"
    }
    choice_of_drink = drinks[drink_name]
    return HttpResponse(f"<h2> {drink_name} </h2>" + choice_of_drink)


# Week 2: Exercise: Creating URLs and Mapping to Views
def home(request):
    return HttpResponse("Welcome to Little Lemon!")

def about(request):
    return HttpResponse("About us")

def menu(request):
    return HttpResponse("Menu")

def book(request):
    return HttpResponse("Make a booking")