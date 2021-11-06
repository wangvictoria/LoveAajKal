'''
Group #1 
Sovann Chang - sovann.d.chang@vanderbilt.edu
Kastur Koul - kastur.koul@vanderbilt.edu
Victoria Wang - victoria.m.wang@vanderbilt.edu
Kristen Wright - kristen.v.wright@vanderbilt.edu
Homework #3
'''

from django.shortcuts import render, redirect
from .forms import ProfileForm, MatchmakerForm, MatchActionForm
from django.views import generic
from .models import Profile
from django.core.mail import send_mail
from django.urls import reverse_lazy
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    """View function for home page of site."""
    context = {}

    return render(request, 'index.html', context)

@login_required
def admin_index(request):
    """View function for home page of site for Reshma."""
    context = {}

    return render(request, 'admin_index.html', context)

# @login_required
# def unmatched_profiles(request):
#     model = Profile
#     context = {'unmatched_list': None, 'first_profiles': None, 
#                 'second_profiles': None, 'third_profiles': None}
#     unmatched_list = Profile.objects.all().filter(matched=False)
#     context['unmatched_list'] = unmatched_list
#     # context['first_profiles'] = unmatched_list[1::2]
#     # context['second_profiles'] = unmatched_list[::2]
#     # context['third_profiles'] = unmatched_list[::3]
#     # model = Profile
#     # context_object_name = 'umatched_list'
#     # template_name = '../profile_detailed_view.html'
#     # queryset = Profile.objects.filter(matched=False)
#     # def get_context_data(self, **kwargs):
#     #     # Call the base implementation first to get the context
#     #     context = super(UnmatchedProfiles, self).get_context_data(**kwargs)
#     #     # Create any data and add it to the context
#     #     context['first_name'] = 'some data'
#     #     return context
#     return render(request, 'unmatched_profiles.html', context)


def about(request):
    context = {}
    return render(request, 'about.html', context)

def contact(request):
    if request.method == 'POST':
        message_name = request.POST['name']
        message_email = request.POST['email']
        message = request.POST['message']

        # send email
        send_mail(
            'message from ' + message_name,  # subject
            message,  # message
            message_email,  # from email
            ['kristen.v.wright@vanderbilt.edu']  # To Email
        )
        return render(request, 'contact.html', {'message_name': message_name})

    else:
        return render(request, 'contact.html', {})

def CreateProfile(request):
    form = ProfileForm(request.POST or None)
    model = Profile
    context = {'form': form}   
    if request.method == 'POST':
        if form.is_valid():
            '''form.save()
            name = form.cleaned_data['first_name']
            print(name)
            form = ProfileForm(request.POST or None)
            '''
            #post = form.save(commit=False)
            ## KASTUR'S EDIT IS BELOW, USED https://www.youtube.com/watch?v=qwE9TFNub84
            form.save()
            # post.user = request.user
            # post.save

            #test = form.cleaned_data['first_name']
            return redirect('create_profile_success')
        else:
            form = ProfileForm(request.POST or None)
    
    return render(request, 'create_profile.html', context)


def create_profile_success(request):
    context = {}
    return render(request, 'create_profile_success.html', context)

def match_action(request):
    model = Profile
    form = MatchActionForm(request.POST or None)
    context = {'available_list': None}
    available_list = Profile.objects.all().filter(matched=False)
    context['available_list'] = available_list
    if request.method == 'POST':
        if form.is_valid():
            profile_instance = Profile.objects.get()
            profile_instance.matched_with = form.cleaned_data.get('matched_with')
            return redirect('match_action_success')
        else:
            form = MatchActionForm(request.POST or None)

    return render(request, 'match_action.html', context)

class UnmatchedProfiles(generic.ListView):
    model = Profile
    context_object_name = 'unmatched_list'
    queryset = Profile.objects.filter(matched=False)
    template_name = 'unmatched_profiles.html'

class MatchedProfiles(generic.ListView):
    model = Profile
    context_object_name = 'matched_list'
    queryset = Profile.objects.filter(matched=True)
    template_name = 'matched_profiles.html'


class ProfileDetailedView(generic.FormView):
    model = Profile
    form_class = MatchmakerForm
    success_url = '../unmatched'
    template_name = 'profile_detailed_view.html'
    
    def form_valid(self, form):
        profile_instance = Profile.objects.get()
        profile_instance.notes = form.cleaned_data.get('notes')
        return super().form_valid(form)


    # context = {'first_name': model.first_name,
    #            'last_name': model.last_name,
    #            'age': model.age,
    #            'gender': model.gender,
    #            'sexuality': model.sexuality,
    #            'country': model.country,
    #            'state_region': model.state_region,
    #            'city': model.city,
    #            'occupation': model.occupation,
    #            'company': model.company,
    #            'education': model.education,
    #            'bio': model.bio,
    #            'religion': model.religion,
    #            'hobbies': model.hobbies,
    #            'dietary_preferences': model.dietary_preferences,
    #            'alcohol': model.alcohol,
    #            'smoking': model.smoking}

    # return render(request, 'profile_detailed_view.html', context)