from django.shortcuts import render
from django.http import HttpResponse

from course_app.models import Year, Course

def index(request):
    return render(request, 'course_app/index.html')

def courses(request):
    page_data = {
        "years": Year.objects.all(),
        "courses": Course.objects.all(),
    }
    return render(request, 'course_app/courses.html', context=page_data)
