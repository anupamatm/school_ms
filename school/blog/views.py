from django.shortcuts import get_object_or_404, redirect, render
from django.contrib.auth import authenticate, login,logout
from django.contrib.auth.models import User
from  .models import Like, Post

# Create your views here.
def post_detail(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    return render(request, 'blog/post_detail.html', {'post': post})



def like_post(request, post_id):
    post = get_object_or_404(Post, pk=post_id)
    # Check if the user has already liked the post
    if Like.objects.filter(post=post, user=request.user).exists():
        return redirect('blog:post_detail', post_id=post_id)  # Redirect back to the post detail page

    # Create a new Like object and associate it with the post and current user
    like = Like(post=post, user=request.user)
    like.save()
    return redirect('blog:post_detail', post_id=post_id)  # Redirect back to the post detail page


def add_post(request):
    if request.method == 'POST':
        title = request.POST['title']
        content = request.POST['content']
        post = Post(title=title, content=content)
        post.save()
        return redirect('blog:post_detail', post.id)  # Redirect to the post list page after successful submission

    return render(request, 'blog/add_post.html')

def add_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        user = User.objects.create_user(username=username, password=password, email=email)
        return redirect('blog:login')  # Redirect to the login page after successful user creation

    return render(request, 'blog/add_user.html')

def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('blog:blog_list')  # Redirect to home page or any other page after successful login
        else:
            return render(request, 'blog/login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'blog.login.html')
    

def blog_list(request):
    posts = Post.objects.all()
    print(posts)
    return render(request, 'blog/blog_list.html', {'posts': posts})

def logout_user(request):
    logout(request)
    return redirect('blog:login')  # Redirect to home page or any other page after logout