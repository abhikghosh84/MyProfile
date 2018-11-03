from django.shortcuts import render, redirect

def profilemain(request):
    context = {
        'title': 'Profile Home Page',
    }
    return render(request, template_name='profilepage/profilemain.html', context=context)