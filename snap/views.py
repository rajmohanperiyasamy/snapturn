from django.shortcuts import render
from django.shortcuts import render_to_response
from django.template import RequestContext
from django.http import HttpResponse

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.views.generic import FormView, DetailView, ListView

from .forms import ProfileImageForm
from .models import ProfileImage
from snap.models import ProfileImage
from snap.models import Youtube

def home(request):
    data={}
    snaps = ProfileImage.objects.all()
    data['snaps'] = snaps
    return render_to_response('index.html',data,context_instance=RequestContext(request))

def about(request):
    return render_to_response('about.html',context_instance=RequestContext(request))

def videos(request):
    data={}
    youtube = Youtube.objects.all()
    print "yyyyyyyyyyyyyyy",youtube
    for s in youtube:
        print s.url
    data['youtube'] = youtube
    return render_to_response('awards.html',data,context_instance=RequestContext(request))

def contacts(request):
    if request.method == 'POST': # If the form has been submitted...
        name = request.POST['fullname']
        user_mail = request.POST['email']
        subject = request.POST['subject']+"  from: "+user_mail
        message = request.POST['message']
        sender = 'rajmohan@doublespring.com'
        recipients = ['rajmohanjr@gmail.com']
        #cc_myself = request.POST['date']['cc_myself']

#        recipients = ['rajmohan@doublespring.com']
#        if cc_myself:
#            recipients.append(sender)

        from django.core.mail import send_mail
        send_mail(subject, message, sender, recipients)
        return render_to_response('success_mail.html',context_instance=RequestContext(request))
    else:
        return render_to_response('contact.html',context_instance=RequestContext(request))



class ProfileImageView(FormView):
    template_name = 'profile_image_form.html'
    form_class = ProfileImageForm

    def form_valid(self, form):
        profile_image = ProfileImage(
            image=self.get_form_kwargs().get('files')['image'])
        profile_image.save()
        self.id = profile_image.id

        return HttpResponseRedirect(self.get_success_url())

    def get_success_url(self):
        return reverse('profile_image', kwargs={'pk': self.id})

class ProfileDetailView(DetailView):
    model = ProfileImage
    template_name = 'profile_image.html'
    context_object_name = 'image'


class ProfileImageIndexView(ListView):
    model = ProfileImage
    template_name = 'profile_image_view.html'
    context_object_name = 'images'
    queryset = ProfileImage.objects.all()
    
    
    
    