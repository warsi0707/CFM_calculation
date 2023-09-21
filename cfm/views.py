from django.http import HttpResponse
from django.shortcuts import render

def index(request):
    if request.method == "POST":
        s1 = eval(request.POST.get('length'))
        s2 = eval(request.POST.get('Depth'))
        s3 = eval(request.POST.get('Height'))
    
        s5 = eval(request.POST.get('air'))

        a=s1*s2
        v=s1*s2*s3
        cfm = v / 60
        total = cfm * s5

        data={
            'area':a,
            'volume':v,
            'cfm':cfm,
            'total':total,
        }
        return render(request, "index.html", data)

    return render(request, "index.html")