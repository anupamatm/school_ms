from django.shortcuts import render, redirect

def auth_teacher(func):
    def wrap(request, *args, **kwargs):
        if 'teacher_id' in request.session:
            return func(request, *args, **kwargs)
        else:
            return redirect('teacher:t_login')
    return wrap

