from media.forms import profile_form
from django.shortcuts import render, redirect
from django.contrib import messages
from accounts.models import profile
import json
from django.http import JsonResponse
from .models import post, comment, like, follower

from django.apps import apps
from django.db.models.deletion import ProtectedError


# Create your views here.
def feed(request):
    try:
        if request.method == 'POST':
            # Creating a new post.
            user_profile = request.user.profile
            content = request.POST.get('content')

            # To know if the post is an empty string.
            if content.isspace():
                messages.error(request, 'The post is empty!')
            else:
                new_post = post.objects.create(id_profile=user_profile, content=content)
                new_post.save()
                messages.success(request, 'Post created!')

        # To change the color if the user liked and also, send all the post.
        user = request.user.profile
        get_post = post.objects.all().order_by('date_added')
        results = []

        # For adding the like_value method for each post
        for posts in get_post:
            is_like_value = posts.like_value(user)
            results.append((posts, is_like_value))

        # For know if a profile follow a other.
        all_profile = profile.objects.all()[:4]
        profile_value = []
        for profiles in all_profile:
            is_follow_value = profiles.follow_value(user)
            profile_value.append((profiles, is_follow_value))

        all_comment = comment.objects.all()

        context = {'all_comments': all_comment, 'all_profile': profile_value, 'results': results}
        return render(request, 'feed.html', context)
    except Exception as e:
        print(f"There's an error: {e}")


def settings(request):
    # To edit the profile information
    if request.method == 'POST':
        form = profile_form(request.POST, request.FILES ,instance=request.user.profile)

        if form.is_valid():
            form.save()
            print(form['image'].value)
            return redirect('feed')
    else:
        form = profile_form(instance=request.user.profile)

    context = {'form': form}
    return render(request, 'settings.html', context)


def profile_view(request, id):
    user_profile = profile.objects.get(id=id)
    all_post = post.objects.filter(id_profile=user_profile).order_by('date_added')
    results = []

    # For pass true or false is user liked the post.
    for posts in all_post:
        is_like_value = posts.like_value(user_profile)
        results.append((posts, is_like_value))

    all_followers = follower.objects.filter(id_following=id).count()
    all_following = follower.objects.filter(id_follower=id).count()

    all_comment = comment.objects.all()

    context = {'user_profile': user_profile, 'posts': all_post, 'all_comments':all_comment ,
               'results': results, 'followers':all_followers, 'following': all_following}
    return render(request, 'profile.html', context)


def post_action(request):
    data = json.loads(request.body)
    action = data['action']
    post_id = data['post']
    user = data['user']

    # Delete a post.
    if action == 'delete':
        get_post = post.objects.get(id=post_id)
        profile_user = profile.objects.get(id=user)

        if get_post.id_profile == profile_user:
            print(f'Post deleted: {post.objects.get(id=post_id)}')
            post.objects.get(id=post_id).delete()
            return redirect('feed')
        else:
            print("This not your post.")

    return JsonResponse('Succesful', safe=False)


def add_comment_to_post(request, id):
    try:
        get_post = post.objects.get(pk=id)
        get_user = request.user.profile
        comment_content = request.POST.get('comment')

        if request.method == 'POST':

            # To know if the post is an empty string.
            if comment_content.isspace():
                print(comment_content)
            else:
                new_comment = comment.objects.create(id_profile=get_user, id_post=get_post, content=comment_content)
                new_comment.save()
                print(f'Comment: {comment_content}.')
    except Exception as e:
        print(f"There's an error: {e}")

    return redirect('feed')


def comment_action(request):
    data = json.loads(request.body)
    comment_id = data['commentID']
    user_id = data['userID']
    action = data['action']

    user_profile = profile.objects.get(id=user_id)
    comment_user = comment.objects.get(id=comment_id)

    if action == 'delete':
        if comment_user.id_profile == user_profile:
            comment_user.delete()
        else:
            print("You can't delete this comment")

    return JsonResponse('Data sent...', safe=False)


def like_action(request, id): 
    user_profile = request.user.profile
    post_to_like = post.objects.get(id=id)

    created_like = like.objects.filter(id_profile=user_profile, id_post=post_to_like).count()

    if created_like == 0:
        new_like = like.objects.create(id_profile=user_profile, id_post=post_to_like)
        new_like.save()
    else:
        like.objects.get(id_profile=user_profile, id_post=post_to_like).delete()

    return redirect('feed')


def follow(request, id):
    user_profile = request.user.profile
    user_to_follow = profile.objects.get(id=id)

    check_follow = follower.objects.filter(id_follower=user_profile, id_following=user_to_follow).count() 
    if check_follow == 0:
        follower.objects.create(id_follower=user_profile, id_following=user_to_follow)
        print('Follow created.')
    else:
        follower.objects.get(id_follower=user_profile, id_following=user_to_follow).delete()
        print('Follow deleted.')
    return redirect('feed')
    