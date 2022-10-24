from django.shortcuts import render, redirect
from school_admin.models import Teacher
from teacher.models import Student

#from teacher.models import Student

# Create your views here.


def t_login(request):
    if request.method == 'POST':
        t_uid = request.POST['uname']
        t_pwd = request.POST['pwd']

        try:
            #a_login = StudentLogin.objects.get(student_uid=s_uid,student_pwd=s_pwd)
            t_login = Teacher.objects.get(teacher_email=t_uid, teacher_password=t_pwd)
            request.session['teacher_id'] = t_login.id
            return redirect("teacher:t_home")
        except:
            msg = "invalid user name and password"
            return render(request, "t_login.html", {"error_message": msg})

    return render(request, "t_login.html")


def t_home(request):
    t_session=Teacher.objects.get(id=request.session['teacher_id'])
    return render(request, "t_home.html",{'teacher_data':t_session})


def tview_profile(request):
    return render(request, "tview_profile.html")


def tview_student(request):
    students=Student.objects.filter(teacher=request.session['teacher_id']) #select * from table where 

    return render(request, "tview_student.html",{'student_list':students})


def add_student(request):
    if request.method == 'POST':
        s_name = request.POST['sname']
        s_email = request.POST['s_email']
        s_address = request.POST['s_address']
        s_phone = request.POST['s_phone']
        s_gender = request.POST['s_gender']
        s_password = request.POST['s_pwd']
        s_photo = request.FILES['s_pic']
        sparent_name = request.POST['sp_name']
        s_dob = request.POST['s_dob']

        # object created
        student_add = Student(
            student_name = s_name,
            student_email = s_email,
            student_address = s_address,
            student_phone = s_phone,
            student_gender = s_gender,
            student_parrent_name = sparent_name,
            student_password = s_password,
            student_photo = s_photo,
            student_dob = s_dob,
            teacher_id = request.session['teacher_id'])

        student_add.save()

    return render(request, "add_student.html")


def tchange_pwd(request):
    return render(request, "tchange_password.html")
