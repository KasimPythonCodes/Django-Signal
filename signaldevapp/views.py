from django.shortcuts import render , HttpResponse
from signaldevapp.models import*
# Create your views here.
import uuid


def reg(request):
    user=request.user
    if request.method == 'POST':
        name = request.POST.get('name')
        password = request.POST.get('password')
        # ids=uuid.uuid4()
        count=Student.objects.all().count()
        code = str(uuid.uuid4()).replace("-", "")[:6]
        print(code)
        print(count)
        user = Student.objects.create(
            name=name,
            password=password,
            # user=request.user,
        )
        user.save()
        return render(request , 'index.html')
    else:    
        count=Student.objects.all().count()
        return render(request , 'index.html' ,{'count':count})
