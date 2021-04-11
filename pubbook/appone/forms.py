from django import forms
from appone.models import Publisher, Book

class NewPublisher(forms.ModelForm):
    class Meta:
        model = Publisher
        fields = '__all__'

class NewBook(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'
