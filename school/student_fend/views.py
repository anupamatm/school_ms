from django.shortcuts import render
import requests

# Create your views here.
def home(request):
    response = requests.get('http://127.0.0.1:8000/student_api/load_student')
    data = response.json()
    # return render(request, 'home.html', {'data': data})
     
   
   
    return render(request,'student_fend/home.html',{'data': data}) 