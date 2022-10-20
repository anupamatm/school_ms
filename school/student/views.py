from django.shortcuts import render, redirect

from student.models import StudentLogin

# Create your views here.


def s_login(request):
    if request.method == 'POST':
        s_uid = request.POST['uname']
        s_pwd = request.POST['pwd']

        try:
            s_login1 = StudentLogin.objects.get(student_uid=s_uid, student_pwd=s_pwd)
            return redirect("sudent:sview_profile")
        except:
            msg = "invalid user name and password"
            return render(request, "s_login.html", {"error_msg": msg})
    return render(request, "s_login.html")


def s_profile(request):
    return render(request, "sviewproile.html")
