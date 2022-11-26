from pathlib import Path

from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render
from library import models


# Create your views here.
def add_book(request):
    if request.method == 'GET':
        return render(request, 'add_new_book.html')

    if request.method == 'POST':
        title = request.POST.get('title')
        author = request.POST.get('author')
        genre = request.POST.get('genre')
        language = request.POST.get('language')
        book = models.Book(
            title=title,
            author=author,
            genre=genre,
            language=language
        )
        book.save()
        return HttpResponse('Add the book to the DB')


def read_book(request, id_book):
    book = models.Book.objects.filter(id=id_book).first()
    genre = models.Genre.objects.filter(id=book.genre).first()
    file_path = models.BookFile.objects.filter(id_book=book.id).first()
    get_home_path = Path(__file__).resolve().parent.parent
    with open(str(get_home_path) + file_path.path_file, encoding='utf-8') as text:
        read_book = text.readlines()

    return HttpResponse(f'Name book - {book.title}, author - {book.author}, genre - {genre.name}, language - {book.language}\n {read_book}')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'GET':
            return render(request, 'login.html')

        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponse('User is login')
            else:
                return HttpResponse('No user')
    else:
        return HttpResponse('<a href="logout"> logout</a>')


def logout_user(request):
    logout(request)
    return HttpResponse('Already')


def user_registration(request):
    if request.method == 'GET':
        return render(request, 'registration.html')
    if request.method == 'POST':
        user = User.objects.create_user(username=request.POST.get('username'),
                                        password=request.POST.get('password'),
                                        email=request.POST.get('email'),
                                        first_name=request.POST.get('first_name'),
                                        last_name=request.POST.get('last_name'))
        user.save()
        return HttpResponse('User is create')




def get_comment(request, id_comment):
    comments_dict = {}
    query = f"""select library_comment.id, library_comment.name, library_comment.comment, library_book.title 
    from library_comment join library_book on library_comment.id_book = library_book.id
     where library_comment.id = {id_comment}"""
    comment = models.Comment.objects.raw(query)
    for element in comment:
        comments_dict[element.name] = {element.title: element.comment}
    return HttpResponse(comments_dict.items())

