from django.shortcuts import render, redirect
from .models import Course


# Create your views here.
def index(request):
    context = {
        'courses': Course.objects.all()
        #SELECT * FROM Course
    }
    return render(request, 'courses/index.html', context)

def courses(request):
    Course.objects.create(course=request.POST['course'], description=request.POST['description'])
    course = Course.objects.all()
    print (course)
    return redirect('/')

def remove(request, id):
    delete = Course.objects.get(id=id)
    Course.objects.filter(id=id).delete()
    course = Course.objects.all()
    print (course)
    return redirect('/')
