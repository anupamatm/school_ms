from django.shortcuts import render, redirect
#from teacher.models import Student

# Create your views here.


def s_login(request):
    if request.method == 'POST':
        s_uid = request.POST['uname']
        s_pwd = request.POST['pwd']

        try:
            s_login1 = Student.objects.get(student_email=s_uid, student_password=s_pwd)
            
            return redirect("student:sview_profile")
        except:
            msg = "invalid user name and password"
            return render(request, "s_login.html", {"error_msg": msg})
    return render(request, "s_login.html")


def s_profile(request):
    return render(request, "sviewproile.html")
