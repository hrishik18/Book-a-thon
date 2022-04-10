from django.shortcuts import get_object_or_404, render, HttpResponse, redirect
from numpy import dtype
import requests

key = "AIzaSyCo0o_fEsJK3XMoNiQe_UTr0S9i2apuLlU"
save = []


def index(request):
    return render(request, 'main.html')


def collection(request):
    books = []
    for i in save:
        r = requests.get(
            f'https://www.googleapis.com/books/v1/volumes/{i}')
        data = r.json()
        saved_books = data
        book_dict = {
            "id": saved_books['id'],
            'title': saved_books['volumeInfo']['title'],
            'image': saved_books['volumeInfo']['imageLinks']['thumbnail'] if 'imageLinks' in saved_books['volumeInfo'] else "",
            'authors': ", ".join(saved_books['volumeInfo']['authors']) if 'authors' in saved_books['volumeInfo'] else "",
            'publisher': saved_books['volumeInfo']['publisher'] if 'publisher' in saved_books['volumeInfo'] else "",
            'info': saved_books['volumeInfo']['infoLink'],
            'popularity': saved_books['volumeInfo']['ratingsCount'] if 'ratingsCount' in saved_books['volumeInfo'] else 0
        }
        books.append(book_dict)

    return render(request, 'saved.html', {'books': books})


def main(request):
    title = request.GET.get('book_name', False)
    # submit = author if request.GET.get(
    #     'book_name', False) == "" else request.GET.get('book_name', False)

    if (title == False) or (title == ""):
        # return redirect('/')
        return render(request, 'main.html')

    queries = {'q': title, 'key': key}
    r = requests.get(
        'https://www.googleapis.com/books/v1/volumes', params=queries)
    data = r.json()
    fetched_books = data['items']
    books = []
    for book in fetched_books:
        book_dict = {
            "id": book['id'],
            'title': book['volumeInfo']['title'],
            'image': book['volumeInfo']['imageLinks']['thumbnail'] if 'imageLinks' in book['volumeInfo'] else "",
            'authors': ", ".join(book['volumeInfo']['authors']) if 'authors' in book['volumeInfo'] else "",
            'publisher': book['volumeInfo']['publisher'] if 'publisher' in book['volumeInfo'] else "",
            'info': book['volumeInfo']['infoLink'],
            'popularity': book['volumeInfo']['ratingsCount'] if 'ratingsCount' in book['volumeInfo'] else 0
        }
        books.append(book_dict)
    return render(request, 'collection.html', {'books': books})


def addbook(request, slug):
    if request.method == 'POST':
        print(slug)
        save.append(slug)

    books = []
    for i in save:
        r = requests.get(
            f'https://www.googleapis.com/books/v1/volumes/{i}')
        data = r.json()
        saved_books = data
        book_dict = {
            "id": saved_books['id'],
            'title': saved_books['volumeInfo']['title'],
            'image': saved_books['volumeInfo']['imageLinks']['thumbnail'] if 'imageLinks' in saved_books['volumeInfo'] else "",
            'authors': ", ".join(saved_books['volumeInfo']['authors']) if 'authors' in saved_books['volumeInfo'] else "",
            'publisher': saved_books['volumeInfo']['publisher'] if 'publisher' in saved_books['volumeInfo'] else "",
            'info': saved_books['volumeInfo']['infoLink'],
            'popularity': saved_books['volumeInfo']['ratingsCount'] if 'ratingsCount' in saved_books['volumeInfo'] else 0
        }
        books.append(book_dict)
# return redirect to collection page with same query
    return render(request, 'saved.html', {'books': books})


# python manage.py runserver
