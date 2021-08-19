from django.shortcuts import render, redirect
from .models import Post
from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt


def getPost(request):
    post = list(Post.objects.values())

    return JsonResponse(post, safe=False)


def post_like(request, post_id):
    post = Post.objects.get(id=post_id)
    post.like_count += 1
    post.save()

# def memos(request):
#     if request.method == 'POST':
#         serializer = MemoSerializer(data=request.data)


# def Post(request):
#     all_Post = Post.objects.all()
#     return render(request, '')
@csrf_exempt
def post(request):
    # all_post=Post.objects.all()
    # return render(request,'Post')
    # postpost = postPost.object.all()
    # json_data = {}
    if request.method == 'POST':
        post = Post()
        # post.author = request.POST['author']
        post.title = request.POST['title']
        post.text = request.POST['text']
        # post.pub_date = request.POST['pub_date']
        # post.save()

    #     return redirect('post')
    # else:
    #     post: Post.object.get(id=1)
        # return render(requsest, '')

        # json_data['author'] = post.author
        # json_data['title'] = post.title
        # json_data['text'] = post.text

        # postPost.objects.create(
        #     author=author,
        #     title=title,
        #     text=text
        # )
    return HttpResponse(status=200)
    # return JsonResponse(json_data)
    # return JsonResponse(post, safe=False)
    # return render(request, 'home.html', {"post": post})


# def post(self, request, *args, **kwargs):
#     return self.create(request)

# def createNote(request):
#     CreateNote_list = createNote.objects.all()
#     json_data = {}
#     if request.method == 'POST':
#         text = request.POST.get('text')
#         title = request.POST.get('title')

#         json_data['text'] = text
#         json_data['title'] = title

#         createNote.objects.create(
#             title=title,
#             text=text
#         )

#     return JsonResponse(json_data)


# return render(request, 'CreateNote.html', {"CreateNote_list": CreateNote_list})
