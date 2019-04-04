  
from django.shortcuts import render,redirect
from django.http  import HttpResponse,HttpResponseRedirect
from .forms import ProjectForm,ProfileForm
from .models import Project,Profile
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import  CoreProject
from .models import  CoreProfile
from .serializer import ProjectSerializer
from .serializer import ProfileSerializer
from rest_framework import status
from .permissions import IsAdminOrReadOnly





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


class ProjectList(APIView):
    def get(self, request, format=None):
        all_project = CoreProject.objects.all()
        serializers = ProjectSerializer(all_project, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProjectSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 
        permission_classes = (IsAdminOrReadOnly,)

class ProjectDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_project(self, pk):
        try:
            return CoreProject.objects.get(pk=pk)
        except CoreProject.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project)
        return Response(serializers.data)
    
    def put(self, request, pk, format=None):
        project = self.get_project(pk)
        serializers = ProjectSerializer(project, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        project = self.get_project(pk)
        project.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

class ProfileList(APIView):
    def get(self, request, format=None):
        all_profile = CoreProfile.objects.all()
        serializers = ProfileSerializer(all_project, many=True)
        return Response(serializers.data)

    def post(self, request, format=None):
        serializers = ProfileSerializer(data=request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data, status=status.HTTP_201_CREATED)
        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST) 
        permission_classes = (IsAdminOrReadOnly,)

class ProfileDescription(APIView):
    permission_classes = (IsAdminOrReadOnly,)
    def get_profile(self, pk):
        try:
            return CoreProfile.objects.get(pk=pk)
        except CoreProfile.DoesNotExist:
            return Http404

    def get(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile)
        return Response(serializers.data)
    
    def put(self, request, pk, format=None):
        profile = self.get_profile(pk)
        serializers = ProfileSerializer(profile, request.data)
        if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        profile = self.get_profile(pk)
        profile.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

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


