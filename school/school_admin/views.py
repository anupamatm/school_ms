from django.shortcuts import render,redirect

from teacher.models import Student
from . models import AdminLogin, Teacher

# Create your views here.
def a_login(request):
    if request.method == 'POST':
        a_uid = request.POST['uname']
        a_pwd = request.POST['pwd']

        try:
            a_login = AdminLogin.objects.get(admin_uid=a_uid,admin_pwd=a_pwd)
            return redirect("school_admin:a_home")
        except:
            msg = "invalid user name and password"
            return render(request,"admin_login.html",{"error_message":msg})

    return render(request,"admin_login.html")


def a_home(request):
    return render(request,"admin_home.html")

def add_teacher(request):
    if request.method == 'POST':
        t_name = request.POST['t_name']
        t_email =request.POST['t_email']
        t_address =request.POST['t_address']
        t_qualification =request.POST['t_quali']
        t_phone =request.POST['t_ph_no']
        t_gender =request.POST['t_gender']
        t_password =request.POST['t_password']
        t_photo =request.FILES['t_photo']
        t_exp =request.POST['t_exp']
        t_dob =request.POST['t_dob']
        
        #object created
        teacher = Teacher(
            teacher_name = t_name ,
            teacher_email = t_email ,
            teacher_address = t_address,
            qualifiaction = t_qualification, 
            teacher_phone = t_phone,
            gender= t_gender, 
            exp=t_exp, 
            teacher_password=t_password, 
            teacher_photo = t_photo,
            teacher_dob = t_dob )

        teacher.save()
        
    return render(request,"add_teacher.html")


def view_teacher(request):
    # teachers=Teacher.objects.all()  #select * from table
    teachers=Teacher.objects.values('teacher_name','teacher_email','qualifiaction','teacher_photo')  #select * from table

    return render(request,"view_teacher.html",{'teacher_list':teachers})


def view_student(request):
    students=Student.objects.all()
    return render(request,"view_student.html",{'student_list':students})

def a_profile(request):
    return render(request,"admin_profile.html")

def c_pwd(request):
    return render(request,"change_password.html")