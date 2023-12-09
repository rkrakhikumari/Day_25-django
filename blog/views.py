from django.shortcuts import render, HttpResponse

# Create your views here.
posts =[
    {
        'author':'Rakhi',
        'title':'Blog post 1',
        'content':'first post content',
        'date_posted':'december 9 2023'
    },
    {
        'author':'Rakhi',
        'title':'Blog post 2',
        'content':'first post content',
        'date_posted':'december 9 2023'
    },
] 

def home(request):
    context ={
        'posts': posts
    }
    return render(request,'home.html', context)

def about(request):
    return render(request,'about.html',{'title':'About'})