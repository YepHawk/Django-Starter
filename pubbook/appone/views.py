from django.shortcuts import render
from appone.models import Book,Publisher
from appone.forms import NewBook,NewPublisher
from django.views import View

# Create your views here.
def index(request):
    return render(request,'index.html')

# def books(request):
#     book = Book.objects.all()
#     context = {'book':book}
#     return render(request,'books.html',context)

def publishers(request):
    publisher = Publisher.objects.all()
    context = {'publisher':publisher}

    if request.method == "POST":
        pchklst = request.POST.getlist("pubdelete")
        print(pchklst)
        for item in pchklst:
            Publisher.objects.filter(publisher_id=item).delete()


    return render(request,'publisher.html',context)

def addbook(request):
    book = NewBook()
    if request.method == "POST":
        book = NewBook(request.POST)
        if book.is_valid():
            book.save(commit=True)
            return render(request,'index.html')
        else:
            print('Error: Invalid')
    return render(request,'addbook.html',{'book':book})

def addpublisher(request):
    pub = NewPublisher()
    if request.method == "POST":
        pub = NewPublisher(request.POST)
        if pub.is_valid():
            pub.save(commit=True)
            return render(request,'index.html')
        else:
            print('Error: Invalid')
    return render(request,'addpub.html',{'pub':pub})


class BookCh(View):
    def get(self,request):
        book = Book.objects.all()
        context = {'book':book}
        return render(request,'books.html',context)

    def post(self,request):
        chklst = request.POST.getlist("bookdelete")
        print(chklst)
        for item in chklst:
            Book.objects.filter(book_id=item).delete()
        return self.get(request)

class PubCh(View):
    def get(self,request):
        publisher = Publisher.objects.all()
        context = {'publisher':publisher}
        return render(request,'publisher.html',context)

    def post(self,request):
        pchklst = request.POST.getlist("pubdelete")
        print(pchklst)
        for item in pchklst:
            Publisher.objects.filter(publisher_id=item).delete()
        return self.get(request)
