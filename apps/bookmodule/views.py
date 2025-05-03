from django.shortcuts import render
from django.http import HttpResponse
from .models import Book
from django.db.models import Q
from django.db.models import Count, Sum, Avg, Max, Min
from .models import Student
#from .models import Student, Address


def task1(request):
    mybooks = Book.objects.filter(Q(price__lte=80))
    return render(request, 'bookmodule/lab8_task1.html', {'books': mybooks})

def task2(request):
    mybooks = Book.objects.filter(
        Q(edition__gt=3) &
        (Q(title__icontains='co') | Q(author__icontains='co'))
    )
    return render(request, 'bookmodule/lab8_task2.html', {'books': mybooks})

def task3(request):
    mybooks = Book.objects.filter(
        ~Q(edition__gt=3) &
        ~(
            Q(title__icontains='co') |
            Q(author__icontains='co')
        )
    )
    return render(request, 'bookmodule/lab8_task3.html', {'books': mybooks})

def task4(request):
    mybooks = Book.objects.all().order_by('title')
    return render(request, 'bookmodule/lab8_task4.html', {'books': mybooks})

def task5(request):
    stats = Book.objects.aggregate(
        total_books=Count('id'),
        total_price=Sum('price'),
        average_price=Avg('price'),
        max_price=Max('price'),
        min_price=Min('price'),
    )
    return render(request, 'bookmodule/lab8_task5.html', {'stats': stats})

def task7(request):
    city_counts = Student.objects.values('address__city').annotate(total=Count('id')).order_by('address__city')
    return render(request, 'bookmodule/lab8_task7.html', {'city_counts': city_counts})




def simple_query(request):
    mybooks = Book.objects.filter(title__icontains='and') # <- multiple objects
    #mybooks = Book.objects.filter(author__icontains='and')
    return render(request, 'bookmodule/bookList.html', {'books': mybooks})



def complex_query(request):
    mybooks = Book.objects.filter(author__isnull=
False).filter(title__icontains='and').filter(edition__gte=2).exclude(price__lte=100)[:10]  
    
    
    if len(mybooks)>=1:
        return render(request, 'bookmodule/bookList.html', {'books':mybooks})
    else:
        return render(request, 'bookmodule/index.html')


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



def __getBooksList():
    book1 = {'id':12344321, 'title':'Continuous Delivery', 'author':'J.Humble and D. Farley'}
    book2 = {'id':56788765,'title':'Reversing: Secrets of Reverse Engineering', 'author':'E. Eilam'}
    book3 = {'id':43211234, 'title':'The Hundred-Page Machine Learning Book', 'author':'Andriy Burkov'}
    return [book1, book2, book3]


def index(request):
    return render(request, "bookmodule/index.html")

def list_books(request):
    return render(request, 'bookmodule/list_books.html')

def viewbook(request, bookId):
    return render(request, 'bookmodule/one_book.html')

def aboutus(request):
    return render(request, 'bookmodule/aboutus.html')

def links(request):
    return render(request, 'bookmodule/links.html')

def formatting(request):
    return render(request, 'bookmodule/formatting.html')

def listing(request):
    return render(request, 'bookmodule/listing.html')

def tables(request):
    return render(request, 'bookmodule/tables.html')



def search_books(request):
    if request.method == "POST":
        string = request.POST.get('keyword', '').lower()
        isTitle = request.POST.get('option1')
        isAuthor = request.POST.get('option2')

        books = __getBooksList()
        newBooks = []

        for item in books:
            contained = False
            if isTitle and string in item['title'].lower():
                contained = True
            if not contained and isAuthor and string in item['author'].lower():
                contained = True
            if contained:
                newBooks.append(item)

        return render(request, 'bookmodule/bookList.html', {'books': newBooks})

    return render(request, 'bookmodule/search.html')





###def search_books(request):
    context = {}
    if request.method == "POST":
        keyword = request.POST.get("keyword", "")
        title_checked = request.POST.get("option1")
        author_checked = request.POST.get("option2")

        result = f"Searching for: <strong>{keyword}</strong><br>"

        if title_checked:
            result += "✔️ In Title<br>"
        if author_checked:
            result += "✔️ In Author<br>"

        if not title_checked and not author_checked:
            result += "<em>No search options selected.</em>"

        context["result"] = result

    return render(request, 'bookmodule/search.html', context)



 
