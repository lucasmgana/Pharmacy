from django.views import generic



class Profile(generic.TemplateView):
    template_name= "profile/profile.html"
