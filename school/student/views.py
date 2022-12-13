from django.shortcuts import render, redirect

from teacher.models import Student
#from teacher.models import Student

# Create your views here.


def s_login(request):
    if request.method == 'POST':
        s_uid = request.POST['uname']
        s_pwd = request.POST['pwd']

        try:
            s_login1 = Student.objects.get(student_email=s_uid, student_password=s_pwd)
            request.session['student_id'] = s_login1.id
            return redirect("student:s_home")
        except:
            msg = "invalid user name and password"
            return render(request, "s_login.html", {"error_msg": msg})
    return render(request, "s_login.html")


def s_profile(request):
    return render(request, "sviewproile.html")

def student_home(request):
    return render(request, "student_home.html")

def schange_password(request):
    msg=""
    if request.method=='POST':
        s_old_pwd = request.POST['old_pwd']
        s_new_pwd = request.POST['new_pwd']
        s_con_pwd = request.POST['con_pwd']

        students = Student.objects.get(id=request.session['student_id'])
      
        if students.student_password == s_old_pwd:
            if s_new_pwd == s_con_pwd :
                students.student_password = s_new_pwd
                students.save()
                msg = "password changeed successfully"
                
            else:
                msg= "password does not match"
        else:
            msg="incorrect password"
            #return render(request, "tchange_password.html",{'status': msg})

    return render(request, "schange_password.html",{'status': msg})
