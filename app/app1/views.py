from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, logout
from .models import Comment
from .forms import CommentForm

# Create your views here.

# registration, using djangos usercreation form
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

# using djangos logout system then return them to login
def logout_view(request):
    logout(request)
    #redirect to chat
    return redirect('login')


# View to hold a seperate page for edditing a comment, 
@login_required
def edit_comment(request, comment_id):
    # get the unique comment
    comment = get_object_or_404(Comment, id=comment_id)
    # iff and only iff the user is the one who made the comment
    if request.user == comment.user:
        if request.method == 'POST':
            # setup the form to reference the old comment
            form = CommentForm(request.POST, instance=comment)
            if form.is_valid():
                form.save()
                return redirect('chat')
        else:
            form = CommentForm(instance=comment)
    else:
        # just redirect back to chat if the user isnt allowed ot edit it
        return redirect('chat')
    form = CommentForm(request.POST)
    # base render for the edit comment page. this is a little funky fut it seems to work, I need to rewrite it
    return render(request, 'edit_comment.html', {'form': form, 'comment': comment})


# primary view for the app, it is where the user can see and make posts
def chat(request):
    # get all the comments
    comments = Comment.objects.all()
    # setup the comment form
    form = CommentForm(request.POST)
    if request.method == "POST":
        comment = form.save(commit=False)
        # add the user to the comment
        comment.user = request.user
        comment.save()
        return redirect('chat')
    return render(request, 'chat.html', {'form':form, 'comments':comments})

# This view should lalow the user to like and unlike comments, 
def like_comment(request, comment_id):
    # get teh comment
    comment = get_object_or_404(Comment, id=comment_id)
    if request.user != comment.user:
        # if the user has already liked it then remove the like, otherwise add them
        if request.user in comment.likes.all():
            comment.likes.remove(request.user)
        else:
            comment.likes.add(request.user)
        
    return redirect('chat')

   