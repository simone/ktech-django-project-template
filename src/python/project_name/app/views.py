# Create your viewshere.
from django.http import HttpResponse

def home(request):
    return HttpResponse("""
        <img src="static/k-tech.jpg" />
""")
