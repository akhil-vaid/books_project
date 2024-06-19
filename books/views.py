from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.db import models
from .forms import BookForm, RegisterForm, BookSearchForm
from .models import Book


def book_list(request):
    books = Book.objects.all()
    return render(request, "books/book_list.html", {"books": books})


def book_detail(request, pk):
    book = get_object_or_404(Book, pk=pk)
    return render(request, "books/book_detail.html", {"book": book})


@login_required
def book_create(request):
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm()
    return render(request, "books/book_form.html", {"form": form})


@login_required
def book_update(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        form = BookForm(request.POST, request.FILES, instance=book)
        if form.is_valid():
            form.save()
            return redirect("book_list")
    else:
        form = BookForm(instance=book)
    return render(request, "books/book_form.html", {"form": form})


@login_required
def book_delete(request, pk):
    book = get_object_or_404(Book, pk=pk)
    if request.method == "POST":
        book.delete()
        return redirect("book_list")
    return render(request, "books/book_confirm_delete.html", {"book": book})


def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect("home")
    else:
        form = RegisterForm()
    return render(request, "books/register.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get("username")
            password = form.cleaned_data.get("password")
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect("home")  # Redirect to home page after login
    else:
        form = AuthenticationForm()
    return render(request, "books/login.html", {"form": form})


def logout_view(request):
    logout(request)
    return redirect("home")


def book_search(request):
    form = BookSearchForm(request.GET or None)
    query = Book.objects.all()
    if form.is_valid():
        search_query = form.cleaned_data["search_query"]
        if search_query:
            query = query.filter(
                models.Q(title__icontains=search_query)
                | models.Q(author__icontains=search_query)
                | models.Q(isbn_number__icontains=search_query)
                | models.Q(published_date__year__icontains=search_query)
                | models.Q(genre__icontains=search_query)
            )

    context = {"form": form, "books": query}
    return render(request, "books/book_search.html", context)


def home(request):
    form = BookSearchForm(request.GET or None)
    query = Book.objects.all()
    if form.is_valid():
        search_query = form.cleaned_data.get("search_query")
        if search_query:
            query = query.filter(
                models.Q(title__icontains=search_query)
                | models.Q(author__icontains=search_query)
                | models.Q(isbn_number__icontains=search_query)
                | models.Q(published_date__year__icontains=search_query)
                | models.Q(genre__icontains=search_query)
            )

    context = {"form": form, "books": query}
    return render(request, "books/home.html", context)
