from django.shortcuts import get_object_or_404, render, HttpResponse,redirect
from numpy import dtype
import requests

key = "AIzaSyCo0o_fEsJK3XMoNiQe_UTr0S9i2apuLlU"

def collection(request):
    return render(request,'collection.html')


def main(request):
    title = request.GET.get('book_name', False)
    # submit = author if request.GET.get(
    #     'book_name', False) == "" else request.GET.get('book_name', False)

    if (title == False) or (title == ""):
        #return redirect('/')
        return render(request, 'main.html')
        
    queries = {'q': title, 'key': key}
    print(queries)
    r = requests.get(
        'https://www.googleapis.com/books/v1/volumes', params=queries)
    #print(r)
    data = r.json()
    fetched_books = data['items']
    books = []
    save=[]
    for book in fetched_books:
        book_dict = {
            "id":book['id'],
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
