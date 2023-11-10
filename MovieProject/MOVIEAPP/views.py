from django.shortcuts import render,redirect
# from django.http import HttpResponse
from . models import Movie
from . forms import movie_form

# Create your views here.
def Index(request):
    movie=Movie.objects.all()
    context={
        'movie_list':movie
    }
    return render(request,'Indexs.html',context)
#function to fetch databse contents
def detail(request,movie_id):
    MOVIE=Movie.objects.get(id=movie_id)
    return render(request,"detail.html",{'MOVIE':MOVIE})
def add_movie(request):
    if request.method=="POST":
        Name=request.POST.get('Name')
        Desc=request.POST.get('Desc')
        Year=request.POST.get('Year')
        Img=request.FILES['Img']
        movie=Movie(Name=Name,Desc=Desc,Year=Year,Img=Img) #database field name=user input name
        movie.save()
        return redirect('/')
    return render(request,'addmovie.html')
def update(request,id):
    movie=Movie.objects.get(id=id)
    form=movie_form(request.POST or None,request.FILES,instance=movie)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'edit.html',{'form':form,'movie':movie})
#DELETE function
def delete(request,id):
    if request.method=="POST":
          movie=Movie.objects.get(id=id)
          movie.delete()
          return redirect('/')

    return render(request,'delete.html')

