from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpRequest, Http404, HttpResponseBadRequest

# Create your views here.
def home(request: HttpRequest):
    name = "Noel"
    data = request.GET.get('q', '')
    return HttpResponse(f'<h1>Hello World {data}</h1>')
    # raise Http404("Bad Request")
    # print(request.method, 'Request Method')
    # data = ['Noel', 'Steph', 'Jordan']
    # response = HttpResponse(data, { 
    #     'Content-Type': 'text/plain',
    #  })
    # return response

def page(request, id):
    return HttpResponse(f'Counter#{id}')

def page_render(request, id):
    return render(request, "dashboard/counter_page.html", {
        'data': id
    })