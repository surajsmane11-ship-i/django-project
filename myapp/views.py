from django.http import HttpResponse

def home(request):
    return HttpResponse("🚀 Hello, Jenkins CI/CD is working! POLL SCM AUTO BUILD IN 2 MIN")
