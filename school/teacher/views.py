from django.shortcuts import render,redirect
from  school_admin.models import Teacher

# Create your views here.
def t_login(request):
    if request.method == 'POST':
        t_uid = request.POST['uname']
        t_pwd = request.POST['pwd']

        try:
            #a_login = StudentLogin.objects.get(student_uid=s_uid,student_pwd=s_pwd)
            t_login =Teacher.objects.get(teacher_email=t_uid,teacher_password=t_pwd)
            return redirect("teacher:t_home")
        except:
            msg = "invalid user name and password"
            return render(request,"t_login.html",{"error_message":msg})

    return render(request,"t_login.html")

def t_home(request):
    return render(request,"t_home.html")
def tview_profile(request):
    return render(request,"tview_profile.html")
def tview_student(request):
    return render(request,"tview_student.html")
def add_student(request):
    return render(request,"add_student.html")
def tchange_pwd(request):
    return render(request,"tchange_password.html")