from django.http.response import HttpResponse
from django.views import generic
from django.shortcuts import HttpResponseRedirect, redirect, render
from pharmaProfile.forms import RegisterSalesmanForm, PermitSalesmanForm
from django.urls import reverse, reverse_lazy
from django.contrib.auth.models import User
from pharmaProfile.models import Profile


class ManageUser(generic.TemplateView):
    template_name = 'profile/users.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        users = []

        user = User.objects.all()
        for yuza in user:
            if yuza.is_superuser or yuza.profile.is_boss:
                continue
            users.append(yuza)
        
        context['users'] = users
        return context


class SalesManRegisterView(generic.View):
    template_name= "profile/profile.html"

    def get(self, request):
        return render(request, self.template_name, {'form': RegisterSalesmanForm})
    
    def post(self, request, **kwargs):
        form = RegisterSalesmanForm

        first_name = request.POST.get('first_name')
        middle_name = request.POST.get('middle_name')
        last_name = request.POST.get('last_name')
        gender = request.POST.get('gender')
        nida = request.POST.get('nida')
        kura = request.POST.get('kura')
        licence = request.POST.get('licence')
        mobile_number = request.POST.get('mobile_number')
        username = request.POST.get('username')
        email = request.POST.get('email')
        password_r = "mganaluka"

        if username and password_r:
            user_r = User.objects.create_user(username=username, password=password_r)
            user_r.save()
            
            prof  = Profile.objects.get(owner = user_r)
            prof.email = email
            if middle_name:
                prof.fullname = first_name +" "+middle_name+" "+last_name
            else:
                prof.fullname = first_name +" "+last_name
            prof.mobile = mobile_number
            if nida:
                prof.nida = nida
            if licence:
                prof.licence = licence
            if kura:
                prof.kura = kura
            prof.gender = gender            
            prof.save()
            return redirect('manage_medicine')

        else:
            # print('Please enter valid food informations')
            return  HttpResponseRedirect(reverse('profile'))
    

class PermitSalesman(generic.View):
    template_name= "profile/permit.html"

    def get(self, request, pk):
        user_to_permit = User.objects.get(id = pk)
        return render(request, self.template_name, {'form': PermitSalesmanForm})
    
    def post(self, request, **kwargs):
        form = PermitSalesmanForm

        if True:
            pass

        else:
            # print('Please enter valid food informations')
            return  HttpResponseRedirect(reverse('profile'))
    
