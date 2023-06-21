from django.http import HttpResponse
from django.shortcuts import render
from .forms import usersform


def homepage(request):
    data={
        'title':'Home new',
        'bdata':'welcome to wscubetech1',
        'clist':['PHP','JAVA','DJANGO'],
        'numbers':[10,20,30,40,50,60],
        'student_details':[
            {'name':'durgesh','phone':9897970080},
            {'name':'testing','phone':9866777888}         
          ]
        
    }
    return render(request,"index.html",data)

def aboutUs(request):
    return HttpResponse("welcome to wscubetech")

def coursedetails(request,courseid):
    return HttpResponse(courseid)



def userform(request):
    finalans = 0
    fn=userform()
    
    data={'form':fn}
    if request.method == 'GET':
        try:
            n1 = int(request.GET.get('num1'))
            n2 = int(request.GET.get('num2'))
            finalans = n1 + n2
            data={
                'form':fn,
                'output':finalans
            }
        except:
            pass
    return render(request, "userform.html", {'output': finalans})
