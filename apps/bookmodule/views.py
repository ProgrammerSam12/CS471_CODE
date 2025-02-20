from django.shortcuts import render
from django.http import HttpResponse

def index(request):
    name = request.GET.get("name", "world!")
    return render(request, "bookmodule/index.html", {"name": name})

def index2(request, val1=0):
    return HttpResponse(f"value1 = {val1}")

def viewbook(request, bookId):
    book1 = {'id': 123, 'title': 'Continuous Delivery', 'author': 'J. Humble and D. Farley'}
    book2 = {'id': 456, 'title': 'Secrets of Reverse Engineering', 'author': 'E. Eilam'}
    
    # Select the correct book based on bookId
    targetBook = book1 if bookId == 123 else book2 if bookId == 456 else None

    return render(request, "bookmodule/show.html", {"book": targetBook})


def index(request):
    return render(request, "bookmodule/index.html")
def list_books(request):
    return render(request, 'bookmodule/list_books.html')
def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')
def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')