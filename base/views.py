from email import message
from typing_extensions import Required
from urllib import request, response
from django.shortcuts import render, redirect,HttpResponse
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView, FormView
from django.urls import reverse_lazy

from django.contrib.auth.views import LoginView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login

# Imports for Reordering Feature
from django.views import View
from django.shortcuts import redirect
from django.db import transaction

from .models import Task,FilesUpload,Sts,User,TueForm
from .forms import PositionForm


from .models import Products,News
from django.core.paginator import Paginator

import requests
from django.contrib import messages

from django.contrib.auth.decorators import login_required

# def doctorReg(request):   
#     news_objects1=News.objects.all()
#     return render(request,'base/doctorReg.html',{'news_objects1':news_objects1})

@login_required
def doctorLog(request):
    user_objects=User.objects.all()
    user_name=request.GET.get('user_name')
    if user_name!='' and user_name is not None:
        user_objects=user_objects.filter(username__icontains=user_name)
        # user_objects=user_objects.filter(cateegory__icontains=user_name)
    return render(request,'base/doctorLog.html',{'user_objects':user_objects})


def home(request):
    return render(request,'base/home.html')
    # return render(request,'base/home.html') 
  
def drugs(request):
    product_objects=Products.objects.all()
    # drug_objects=Drug1.objects.all()
    
    # search code
    item_name=request.GET.get('item_name')
    if item_name!='' and item_name is not None:
        product_objects=product_objects.filter(title__icontains=item_name)
        product_objects=product_objects.filter(cateegory__icontains=item_name)
        # product_objects=product_objects.filter(cateegory__icontains=item_name)
    # paginator code
    paginator=Paginator(product_objects,10)
    page=request.GET.get('page')
    product_objects=paginator.get_page(page)
    return render(request,'base/drugs.html',{'product_objects':product_objects})
    # return render(request,'drugs.html')  

def detail(request,id):
    product_object=Products.objects.get(id=id)   
    return render(request,'base/detail.html',{'product_object':product_object})   
    # return render(request,'detail.html')

def aboutus(request):   
    return render(request,'base/aboutus.html')

def resources(request):   
    return render(request,'base/resources.html')

def education(request):  
    response=requests.get('https://api.covid19api.com/countries').json() 
    return render(request,'base/education.html',{'response':response})

def news(request):   
    news_objects=News.objects.all()
    return render(request,'base/news.html',{'news_objects':news_objects})

def tue(request):   
    return render(request,'base/tue.html')

@login_required
def upload(request):  
    # stages=Sts.objects.all()
    user = request.user
    if request.method=="POST":
        file2=request.FILES["file"]
        
        document=FilesUpload.objects.create(user=user,file=file2)
        document.save()
        
        messages.success(request,"File Uploaded Successfully")
        return redirect(reverse_lazy('tasks')) 
    try:
     status2=Sts.objects.get(user_id=user)
    #  status2.save()
    except:
     status2=Sts.objects.create(user_id=user)
     status2.save()

    return render(request,'base/upload.html')  

@login_required
def pre(request):
    user = request.user
    try: 
    #  data=FilesUpload.objects.filter(user=user).count()
     preview=TueForm.objects.get(user=user)
     context={'user':user,'preview':preview}
    except:
     data=0
     context={'user':user,'data':data}
    # context={'user':user,'stages':stages,'data':data}
    return render(request,'base/pre.html',context) 

@login_required
def stage(request):
    user = request.user
    # print(user.id)
    # user=User.objects.get(id=1)
    # stages=Sts.objects.get(user_id=user)
    # print(stages)
    try:
     stages=Sts.objects.get(user_id=user)
    #  status2.save()
    except:
     stages=Sts.objects.create(user_id=user)
     stages.save()
    try: 
     data=FilesUpload.objects.filter(user=user).count()
     preview=TueForm.objects.get(user=user)
     context={'user':user,'stages':stages,'data':data,'preview':preview}
    except:
     data=0
     context={'user':user,'stages':stages,'data':data}
    # context={'user':user,'stages':stages,'data':data}
    return render(request,'base/stage.html',context) 

class CustomLoginView(LoginView):
    template_name = 'base/login.html'
    fields = '__all__'
    redirect_authenticated_user = True

    def get_success_url(self):
        return reverse_lazy('tasks')


class RegisterPage(FormView):
    template_name = 'base/register.html'
    form_class = UserCreationForm
    redirect_authenticated_user = True
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        user = form.save()
        try:
          status2=Sts.objects.get(user_id=user)
    #  status2.save()
        except:
         status2=Sts.objects.create(user_id=user)
         status2.save()
        if user is not None:
            login(self.request, user)
        
        return super(RegisterPage, self).form_valid(form)

    def get(self, *args, **kwargs):
        if self.request.user.is_authenticated:
            return redirect('tasks')
        return super(RegisterPage, self).get(*args, **kwargs)


class TaskList(LoginRequiredMixin, ListView):
    # user=request.user
    # x=FilesUpload.objects.filter(user=user).count()
    model = Task
    context_object_name = 'tasks'
    
    def get_context_data(self, **kwargs):
        
        context = super().get_context_data(**kwargs)
        context['total']=context['tasks'].all()
        context['cnt']=context['tasks'].all().count()
        context['tasks'] = context['tasks'].filter(user=self.request.user)
        context['count'] = context['tasks'].filter(complete=False).count()
        
        search_input = self.request.GET.get('search-area') or ''
        if search_input:
            context['tasks'] = context['tasks'].filter(
                title__contains=search_input)

        context['search_input'] = search_input

        return context
    
class TaskDetail(LoginRequiredMixin, DetailView):
    model = Task
    context_object_name = 'task'
    template_name = 'base/task.html'


class TaskCreate(LoginRequiredMixin, CreateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super(TaskCreate, self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = Task
    fields = ['title', 'description', 'complete']
    success_url = reverse_lazy('tasks')


class DeleteView(LoginRequiredMixin, DeleteView):
    model = Task
    context_object_name = 'task'
    success_url = reverse_lazy('tasks')
    def get_queryset(self):
        owner = self.request.user
        return self.model.objects.filter(user=owner)

class TaskReorder(View):
    def post(self, request):
        form = PositionForm(request.POST)

        if form.is_valid():
            positionList = form.cleaned_data["position"].split(',')

            with transaction.atomic():
                self.request.user.set_task_order(positionList)

        return redirect(reverse_lazy('tasks'))

@login_required
def tue_form(request):
    user = request.user
    if request.method == 'POST':
        # print(request.POST.get('fname'))
        # print(request.POST)
        fname1 = request.POST['fname']
        dob1 = request.POST['dob']
        email1 = request.POST['email']
        phone1 = request.POST['phone']
        gender1 = request.POST['gender']
        sport1 = request.POST['sport']
        id_type1 = request.POST['id_type']
        id_no1 = request.POST['id_no']
        name_on_id1 = request.POST['name_on_id']
        addType1 = request.POST['addType']
        nationality1 = request.POST['nationality']
        state1 = request.POST['state']
        district1 = request.POST['district']
        city1 = request.POST['city']
        postal_code1 = request.POST['postal_code']
        
        select1a = request.POST['select1']
        text1a = request.POST['text1']
        text2a = request.POST['text2']
        text3a = request.POST['text3']
        select2a = request.POST['select2']
        text4a = request.POST['text4']
        select3a = request.POST['select3']

        text5a = request.POST['text5']
        select4a = request.POST['select4']
        select5a = request.POST['select5']
        select6a = request.POST['select6']
        select7a = request.POST['select7']
        select8a = request.POST['select8']
        text5a = request.POST['text5']
        upload1a=request.FILES['upload1']
        text6a = request.POST['text6']
        text7a = request.POST['text7']
        text8a = request.POST['text8']
        text9a = request.POST['text9']
        text10a = request.POST['text10']
        text11a = request.POST['text11']
        text12a = request.POST['text12']
        physicianNamea = request.POST['physicianName']
        text13a = request.POST['text13']
        text14a = request.POST['text14']
        text15a = request.POST['text15']
        text16a = request.POST['text16']
        text17a = request.POST['text17']
        text18a = request.POST['text18']
        text19a = request.POST['text19']
        text20a = request.POST['text20']
        text21a = request.POST['text21']
        text22a = request.POST['text22']
        upload2a=request.FILES["upload2"]
        upload3a=request.FILES["upload3"]
        date3a = request.POST['date3']

        print(dob1)
        TueForm.objects.create(
        user=request.user,
        fname=fname1,
        dob=dob1,
        email=email1,
        phone=phone1,
        gender=gender1,
        sport=sport1,
        id_type=id_type1,
        id_no=id_no1,
        name_on_id=name_on_id1,
        addType=addType1,
        nationality=nationality1,
        state=state1,
        district=district1,
        city=city1,
        postal_code=postal_code1,
        select1=select1a,
        text1=text1a,
        text2=text2a,
        text3=text3a,
        select2=select2a,
        text4=text4a,
        select3=select3a,
        text5=text5a,
        upload1=upload1a,
        text6=text6a,
        text7=text7a,
        text8=text8a,
        text9=text9a,
        text10=text10a,
        text11=text11a,
        text12=text12a,
        physicianName=physicianNamea,
        text13=text13a,
        text14=text14a,
        text15=text15a,
        text16=text16a,
        text17=text17a,
        text18=text18a,
        text19=text19a,
        text20=text20a,
        text21=text21a,
        text22=text22a,
        upload2=upload2a,
        upload3=upload3a,
        date3=date3a,
        )
        messages.success(request,"Form Submitted Successfully")
        return redirect(reverse_lazy('tasks')) 
        
    return render(request,'base/tue_form.html')

@login_required
def info(request):
    return render(request,'base/info.html') 


@login_required
def prescription(request):
    return render(request,'base/prescription.html') 
