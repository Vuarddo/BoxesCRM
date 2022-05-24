from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .models import boxes
from .forms import PostForm, NewUserForm
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm #add this

# Create your views here.
def post_list(request):
    posts = boxes.objects.all()
    return render(request, 'box/post_list.html', {'posts':posts})

def post_detail(request, pk):
    post = get_object_or_404(boxes, pk=pk)
    return render(request, 'box/post_detail.html', {'post': post})

def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            boxes = form.save(commit=False)
            boxes.author = request.user
            boxes.published_date = timezone.now()
            boxes.save()
            return redirect('post_detail', pk=boxes.pk)
    else:
        form = PostForm()
    return render(request, 'box/post_edit.html', {'form': form})


def register_request(request):
	if request.method == "POST":
		form = NewUserForm(request.POST)
		if form.is_valid():
			user = form.save()
			login(request, user)
			messages.success(request, "Registration successful." )
			return redirect("http://127.0.0.1:8000/")
		messages.error(request, "Unsuccessful registration. Invalid information.")
	form = NewUserForm()
	return render (request=request, template_name="box/register.html", context={"register_form":form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("http://127.0.0.1:8000/")
			else:
				messages.error(request,"Invalid username or password.")
		else:
			messages.error(request,"Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="box/login.html", context={"login_form":form})

def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("http://127.0.0.1:8000/")


def post_edit(request, pk):
    post = get_object_or_404(boxes, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'box/post_edit.html', {'form': form})
