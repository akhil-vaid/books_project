# books/forms.py

from django import forms
from .models import Book
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from django import forms
from .models import Book


class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = [
            "title",
            "author",
            "published_date",
            "isbn_number",
            "pages",
            "cover",
            "language",
            "genre",
        ]


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class BookSearchForm(forms.Form):
    title = forms.CharField(required=False, label="Title")
    author = forms.CharField(required=False, label="Author")
    isbn_number = forms.CharField(required=False, label="ISBN")
    published_date = forms.DateField(
        required=False,
        label="Published Date",
        widget=forms.DateInput(attrs={"type": "date"}),
    )


from django import forms


class BookSearchForm(forms.Form):
    search_query = forms.CharField(
        required=False,
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Search by Title, Author, ISBN, Published Year, or Genre"
            }
        ),
    )
