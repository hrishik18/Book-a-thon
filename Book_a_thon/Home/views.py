from django.shortcuts import render, HttpResponse,redirect
from numpy import dtype
import requests

key = "AIzaSyCo0o_fEsJK3XMoNiQe_UTr0S9i2apuLlU"
def index(request):
    return render(request,'main.html')

def collection(request):
    return render(request,'collection.html')


def display(request):
    title = request.GET.get('book_name', False)
    author = request.GET.get('author_name', False)
    submit = author if request.GET.get(
        'book_name', False) == "" else request.GET.get('book_name', False)

    if (title == False and author == False) or (title == "" and author == ""):
        #return redirect('/')
        return render(request, 'display.html')
        
    queries = {'q': submit, 'key': key}
    print(queries)
    r = requests.get(
        'https://www.googleapis.com/books/v1/volumes', params=queries)
    #print(r)
    data = r.json()
    fetched_books = data['items']
    books = []
    for book in fetched_books:
        book_dict = {
            'title': book['volumeInfo']['title'],
            'image': book['volumeInfo']['imageLinks']['thumbnail'] if 'imageLinks' in book['volumeInfo'] else "",
            'authors': ", ".join(book['volumeInfo']['authors']) if 'authors' in book['volumeInfo'] else "",
            'publisher': book['volumeInfo']['publisher'] if 'publisher' in book['volumeInfo'] else "",
            'info': book['volumeInfo']['infoLink'],
            'popularity': book['volumeInfo']['ratingsCount'] if 'ratingsCount' in book['volumeInfo'] else 0
        }
        books.append(book_dict)
    return render(request, 'collection.html', {'books': books})


#python manage.py runserver
