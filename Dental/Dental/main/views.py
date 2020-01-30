from django.shortcuts import render


def home(request):
    return render(request, 'main/home.html')


def about(request):
    return render(request, 'main/about.html')


def blog(request):
    return render(request, 'main/blog.html')


def blogdetails(request):
    return render(request, 'main/blog-details.html')


def contactus(request):
    return render(request, 'main/contact.html')


def pricing(request):
    return render(request, 'main/pricing.html')


def service(request):
    return render(request, 'main/service.html')