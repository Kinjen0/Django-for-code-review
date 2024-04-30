from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from .models import Comment
from .forms import CommentForm

# Create your views here.


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            #login the user
            login(request, user) 
            return redirect('chat')  
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

def logout_view(request):
    logout(request)
    #redirect to chat
    return redirect('login')


@login_required
def edit_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user == comment.user:
        if request.method == 'POST':
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('chat')
        else:
            form = CommentForm(instance=comment)
    else:
        return redirect('chat')
    form = CommentForm(request.POST)
    return render(request, 'edit_comment.html', {'form': form, 'comment': comment})



def chat(request):
    comments = Comment.objects.all()
    form = CommentForm(request.POST)
    if request.method == "POST":
        comment = form.save(commit=False)
        comment.user = request.user
        comment.save()
        return redirect('chat')
    return render(request, 'chat.html', {'form':form, 'comments':comments})

    
def like_comment(request, comment_id):

    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.user:
        
        if request.user in comment.likes.all():
            comment.likes.remove(request.user)
        else:
            comment.likes.add(request.user)
        
    return redirect('chat')

   