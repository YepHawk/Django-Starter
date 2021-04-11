from django.shortcuts import render
from appone.models import Book,Publisher
from appone.forms import NewBook,NewPublisher

# Create your views here.
def index(request):
    return render(request,'index.html')

def books(request):
    book = Book.objects.all()
    context = {'book':book}
    return render(request,'books.html',context)

def publishers(request):
    publisher = Publisher.objects.all()
    context = {'publisher':publisher}
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

def delete_book(request):

    if request.method == "POST":

        chklst = request.POST.getlist("bookdelete")
        print(chklst)
        for instance in chklst:  #instance is only ID, need to find object
            for item in Book.objects.all():
                if instance == item.book_id:
                    item.delete()
                    chklst.pop(instance)

    return render(request,'books.html',{'book':book})
