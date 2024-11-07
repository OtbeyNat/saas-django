import pathlib
from django.http import HttpResponse
from django.shortcuts import render

from visits.models import PageVisit

this_dir = pathlib.Path(__file__).resolve().parent

def home_page_view(request, *args, **kwargs):
    qs = PageVisit.objects.all()
    pageqs = PageVisit.objects.filter(path=request.path)
    my_title = "My Page"
    html_template = "home.html"
    my_context = {
        "title": my_title,
        "page_visit_count": pageqs.count(),
        "percent": (pageqs.count() * 100.0) / qs.count(),
        "total_visit_count": qs.count(),
    }
    PageVisit.objects.create(path=request.path)
    return render(request, html_template, my_context)

def about_page_view(request, *args, **kwargs):
    my_title = "My Page"
    my_context = {
        "title": my_title,
    }
    html_template = "about.html"
    return render(request, html_template, my_context)