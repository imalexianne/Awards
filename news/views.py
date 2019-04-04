  
from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from .forms import ProjectForm,ProfileForm
from .models import Project,Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


@login_required(login_url='/accounts/login/')
def welcome(request):
    projects = Project.objects.all()
    return render(request, 'welcome.html',{"projects":projects})

@login_required(login_url='/accounts/login/')
def projects(request,project_id):
    project = Project.objects.get(id = project_id)
    return render(request,"info.html", {"project":project})

@login_required(login_url='/accounts/login/')
def myProfile(request,id):
    user = User.objects.get(id = id)
    profiles = Profile.objects.get(user = user)
    projects = Project.objects.filter(user = user).all()
    form = ProfileForm()
   
    return render(request,'my_profile.html',{"profiles":profiles,"user":user,"projects":projects,"form":form})



def profile(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            profile = form.save(commit=False)
            profile.user = current_user
            profile.save()

        return redirect(welcome)

    else:
        form = ProfileForm()
    return render(request, 'profile.html', {"form": form})

def project(request):
    current_user = request.user
    if request.method == 'POST':
        form = ProjectForm(request.POST, request.FILES)
        if form.is_valid():
            project = form.save(commit=False)
            project.user = current_user
            project.save()

    else:
        form = ProjectForm()
    return render(request, 'project.html', {"form": form})

# def newsletter(request):
#     name = request.POST.get('your_namProjectSerializer
#     email = request.POST.get('email')ProjectSerializer

#     recipient = NewsLetterRecipients(name=name, email=email)
#     recipient.save()
#     send_welcome_email(name, email)
#     data = {'success': 'You have been successfully added to mailing list'}
#     return JsonResponse(data)

# def comments(request):
#     current_user = request.user
#     if request.method == 'POST':
#         form = CommentsForm(request.POST, request.FILES)
#         if form.is_valid():
#             comments = form.save(commit=False)
#             comments.user = current_user
#             comments.save()

#             return redirect(welcome)

#     else:
#         form = CommentsForm()
#     return render(request, 'comment.html', {"form": form})



   

# def all_images(request):
#     images = Image.objects.all()
#     return render(request, 'welcome.html',{"images":images})

def search_results(request):

    if 'project' in request.GET and request.GET["project"]:
        search_term = request.GET.get("project")
        searched_projects = Project.search_by_title(search_term)
        message = f"{search_term}"

        return render(request, 'search.html',{"message":message,"projects": searched_projects})

    else:
        message = "You haven't searched for any term"
        return render(request, 'search.html',{"message":message})

# @login_required(login_url='/accounts/login/')
# def image(request,image_id):
#     try:
#         images = Image.objects.get(id = image_id)
#         locations = Location.objects.all()
#         image_category = Image.objects.filter(category__image_category = category_name)
#     except DoesNotExist:
#         raise Http404()
#     return render(request,"images.html", {"image":image,'image_category':image_category, 'locations':locations})

# def search_result(request):
#     if 'location' in request.GET and request.GET["location"]:
#         search_term = request.GET.get("location")
#         searched_images = Image.search_img(search_term)
#         message = f"{search_term}"

#         return render(request, 'location.html',{"message":message,"images": searched_images})

#     else:
#         message = "You haven't searched for any term"
#         return render(request, 'location.html',{"message":message})


#     return render(request, 'location.html', { 'images':images, 'locations':locations})


