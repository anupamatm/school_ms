from django.shortcuts import render, redirect
from school_admin.models import Teacher
from teacher.models import Student
from . decorators import auth_teacher
from django.http import JsonResponse

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

@auth_teacher
def t_home(request):    
    t_session=Teacher.objects.get(id=request.session['teacher_id'])
    return render(request, "t_home.html",{'teacher_data':t_session})
  
       

@auth_teacher
def tview_profile(request):
    return render(request, "tview_profile.html")

def t_logout(request):
    del request.session['teacher_id']
    request.session.flush()
    return redirect("common:home")

@auth_teacher
def tview_student(request):
    students=Student.objects.filter(teacher=request.session['teacher_id']) #select * from table where 

    return render(request, "tview_student.html",{'student_list':students})

@auth_teacher
def add_student(request):
    msg=""
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

        email_exist = Student.objects.filter(student_email=s_email).exists() # result will be boolean
        
            # object created
        if not email_exist: # if email_exist == false
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
            msg="student Added Succesfully"
        else:
            msg="student Already Added"
    return render(request, "add_student.html",{'status':msg})

@auth_teacher
def tchange_pwd(request):
    msg=""
    if request.method=='POST':
        t_old_pwd = request.POST['old_pwd']
        t_new_pwd = request.POST['new_pwd']
        t_con_pwd = request.POST['con_pwd']

        teachers = Teacher.objects.get(id=request.session['teacher_id'])
        print(teachers.teacher_password,'  ',t_old_pwd)
        print(teachers.teacher_password==t_old_pwd)
        print(t_old_pwd, t_new_pwd,t_con_pwd)
        if teachers.teacher_password == t_old_pwd:
            if t_new_pwd == t_con_pwd :
                Teacher.objects.filter(id=request.session['teacher_id']).update(teacher_password = t_new_pwd)
                # teachers.teacher_password = t_new_pwd
                # teachers.save()
                msg = "password changeed successfully"
                print(teachers.teacher_password)
            else:
                msg= "password does not match"
        else:

            msg="incorrect password"
            #return render(request, "tchange_password.html",{'status': msg})

    return render(request, "tchange_password.html",{'status': msg})

def email_exist(request):
    email = request.POST['email']
    e_exists = Student.objects.filter(student_email = email).exists()
    return JsonResponse({'status':e_exists})

   