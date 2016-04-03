from django.shortcuts import render_to_response
from django.contrib.auth import authenticate,login,logout
from models import Internship,InternCategory
from django.db.models import Q
from django.http import HttpResponseRedirect,HttpResponse
from forms import LoginForm,RegistrationForm,InternshipForm
from django.template import RequestContext
from django.contrib import messages


def home(request):
	return render_to_response('base.html',{})


def InternDetail(request):
	internship=Internship.objects.all()
	return render_to_response('intern.html',{'internship':internship})

def SingleDetail(request,intern_id):
	item=Internship.objects.get(id=intern_id)
	return render_to_response('full_intern_detail.html',{'item':item})	


def Login(request):
    if request.method=='POST':
        form = LoginForm(request.POST)
        btn="Login"
        if form.is_valid():
                username = form.cleaned_data['username']
                password = form.cleaned_data['password']
                user = authenticate(username=username, password=password)
                login(request, user)
                return render_to_response("login.html", {'form':form,"submit_btn": btn},context_instance=RequestContext(request)) 
        else:
            return HttpResponse("Invalid details...")
    else:
        form=LoginForm()
        return render_to_response("login.html",{'form':form},context_instance=RequestContext(request))

def Logout(request):
    logout(request)
    return HttpResponseRedirect('/')
        



def Register(request):
    form = RegistrationForm(request.POST or None)
    btn = "Join"
    if form.is_valid():
        new_user = form.save(commit=False)
        # new_user.first_name = "Justin" this is where you can do stuff with the model form
        new_user.save()
        messages.success(request, "Successfully Registered. Please confirm your email now.")
        return HttpResponseRedirect("/")
        # username = form.cleaned_data['username']
        # password = form.cleaned_data['password']
        # user = authenticate(username=username, password=password)
        # login(request, user)

    context = {
             "form": form,
             "submit_btn": btn,
    }
    return render_to_response( "register.html", context,context_instance=RequestContext(request))        



def search(request):
    try:
        q=request.GET.get('q')
    except:
        None
    if q:
        internships=Internship.objects.filter(Q(location__icontains=q) |Q(interncategory__name__icontains=q) |
         Q(interncategory__company_name__icontains=q))
        context={'query':q,'internships':internships}
        return render_to_response('search.html',context,context_instance=RequestContext(request))
    else:
        return HttpResponseRedirect('/')


def InternForm(request):
    if request.method=="POST":
        form=InternshipForm(request.POST)
        if form.is_valid():
            form.save()
        return HttpResponse('your form has been successfully submitted')    

    else:
        form=InternshipForm()
        return render_to_response('intern_form.html',{'form':form},context_instance=RequestContext(request))
        



def intern_location(request,location):
    interncat=Internship.objects.filter(location=location)
    return render_to_response('intern_location.html',{'interncat':interncat},context_instance=RequestContext(request))


def dashboard(request):
    return render_to_response('dashboard.html',{},context_instance=RequestContext(request))
    

















