from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import redirect

# Create your views here.


def homepage(request):
    return redirect('/voting/')
    return render(request=request,
                  template_name='main/home.html',
                  context={}
                  )
