from django.shortcuts import render
from visits.models import PageVisit

def home_page(request):
    page_title = "Home Page"
    path = request.path
    print(f"Path - {path}")
    PageVisit.objects.create(path = request.path)
    qs = PageVisit.objects.all()
    page_qs = PageVisit.objects.filter(path = request.path)
    context = {
        "page_title": page_title,
        "pagevisit_count": page_qs.count(),
        "total_pagevisit": qs.count()
    }
    return render(request, 'home_page.html', context)