from django.shortcuts import render,redirect
from django.http import HttpResponse
from .forms import PostForm
from django.contrib.auth.decorators import login_required
from .filters import PostFilter
# Create your views here.
from .models import Post
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.core.mail import EmailMessage
from django.conf import settings
from django.template.loader import render_to_string
from django.core.mail import send_mail
from django.shortcuts import render, get_object_or_404


def home(request):
    posts = Post.objects.filter(active=True, featured=True)[0:3]
    return render(request, 'base/index.html', {'posts': posts})

def posts(request):
    post_list = Post.objects.filter(active=True)

    # ✅ Apply filtering
    myFilter = PostFilter(request.GET, queryset=post_list)
    post_list = myFilter.qs  # ✅ Apply filtered queryset

    # ✅ Pagination (3 posts per page)
    page = request.GET.get('page', 1)  # ✅ Default to page 1 if `page` is None
    paginator = Paginator(post_list, 3)

    try:
        posts = paginator.page(page)
    except PageNotAnInteger:
        posts = paginator.page(1)  # ✅ If page is not an integer, load first page
    except EmptyPage:
        posts = paginator.page(paginator.num_pages)  # ✅ If page is out of range, load last page

    context = {
        'posts': posts,
        'myFilter': myFilter,
    }
    return render(request, 'base/posts.html', context)  # ✅ Return the response

def post(request, slug):
    if not slug:  # ✅ Handle missing slug gracefully
        return render(request, 'base/404.html', status=404)  

    post = get_object_or_404(Post, slug=slug)  # ✅ Better error handling

    return render(request, 'base/post.html', {'post': post})

def profile(request): 
    return render(request, 'base/profile.html')

# CRUD VIEWS
@login_required(login_url="home")
def createPost(request):
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('posts')  # ✅ Redirect only after successful submission
    else:
        form = PostForm()  # ✅ Show empty form for GET requests

    return render(request, 'base/post_form.html', {'form': form}) 

@login_required(login_url="home")
def updatePost(request, slug):  # ✅ Use slug in URL
    post = Post.objects.get(slug=slug)
    form = PostForm(instance=post)
    
    if request.method == "POST":
        form = PostForm(request.POST, request.FILES, instance=post)
        if form.is_valid():
            form.save()
            return redirect('posts')  # ✅ Redirect after successful update

    print("Rendering form")
    return render(request, 'base/post_form.html', {'form': form})

@login_required(login_url="home")
def deletePost(request, slug):  # ✅ Use slug in URL
    post = Post.objects.get(slug=slug)
    if request.method == 'POST':
        post.delete()
        return redirect('posts')
    return render(request, 'base/delete_form.html', {'item': post})


# def home(request):
#     posts = Post.objects.filter(active=True, featured =True)[0:3]
#     return render(request, 'base/index.html', {'posts': posts})



# def posts(request):
#     post_list = Post.objects.filter(active=True)

#     # ✅ Apply filtering
#     myFilter = PostFilter(request.GET, queryset=post_list)
#     post_list = myFilter.qs  # ✅ Apply filtered queryset

#     # ✅ Pagination (3 posts per page)
#     page = request.GET.get('page', 1)  # ✅ Default to page 1 if `page` is None
#     paginator = Paginator(post_list, 3)

#     try:
#         posts = paginator.page(page)
#     except PageNotAnInteger:
#         posts = paginator.page(1)  # ✅ If page is not an integer, load first page
#     except EmptyPage:
#         posts = paginator.page(paginator.num_pages)  # ✅ If page is out of range, load last page

#     context = {
#         'posts': posts,
#         'myFilter': myFilter,
#     }
#     return render(request, 'base/posts.html', context)# ✅ Return the response


# def post(request, slug):
#     post = Post.objects.get(slug=slug)
#     return render(request, 'base/post.html', {'post': post})


# def profile(request): 
#     return render(request, 'base/profile.html')







# #CRUD VIEWS
# @login_required(login_url="home")
# def createPost(request):
#     if request.method == "POST":
#         form = PostForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return redirect('posts')  # ✅ Redirect only after successful submission
#     else:
#         form = PostForm()  # ✅ Show empty form for GET requests

#     return render(request, 'base/post_form.html', {'form': form}) 

 

# @login_required(login_url="home")
# def updatePost(request, slug):
#     post = Post.objects.get(slug=slug)
#     form = PostForm(instance=post)
#     if request.method =="POST":
#         form =PostForm(request.POST, request.FILES, instance=post)
#         if form.is_valid():

#             form.save()
#         return redirect(
#         'posts'
#     )
#     print("Rendering form")
#     return render(request, 'base/post_form.html', {'form':form})



# @login_required(login_url="home")

# def deletePost(request, slug):
#     post = Post.objects.get(slug=slug)
#     if request.method == 'POST':
#         post.delete()
#         return redirect('posts')
#     return render(request, 'base/delete_form.html', {'item':post})






# def sendEmail(request):
#     if request.method == "POST":
#         template = render_to_string('base/email_template.html', {
#         'name': request.POST['name'],
#         'email': request.POST['email'],
#         'message': request.POST['message']
#     })
#         email = EmailMessage(request.POST['subject'], template, settings.EMAIL_HOST_USER, ['musefiuamos2@gmail.com']) # this is the receiver

#         email.fail_silently = False
#         email.send()
     
#     return HttpResponse('Email was sent')



def sendEmail(request):
    if request.method == "POST":
        subject = request.POST.get('subject', 'No Subject')  # ✅ Prevents KeyError
        name = request.POST.get('name', 'Unknown User')
        email = request.POST.get('email', 'No Email Provided')
        message = request.POST.get('message', '')

        # ✅ Render email template
        template = render_to_string('base/email_template.html', {
            'name': name,
            'email': email,
            'message': message
        })

        try:
            email_message = EmailMessage(
                subject,
                template,
                settings.EMAIL_HOST_USER,
                ['musefiuamos2@gmail.com']
            )  # this is the receiver
            email_message.fail_silently = False
            email_message.send()

            return render(request, 'base/email_sent.html')  # ✅ Correct return placement

        except Exception as e:
            return HttpResponse(f"Error sending email: {e}")

    return HttpResponse("Invalid request method.")  # ✅ Handles non-POST requests properly


















  
    
