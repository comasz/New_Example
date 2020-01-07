from django.shortcuts import render
from AppTwo.models import User
from django.http import HttpResponse
from AppTwo.forms import NewUserForm

# Create your views here.

#BASE DIRECTORY IS IN 'templates' FOLDER

def index(request):
    # return HttpResponse ('Welcome To My Site')
    # my_dict = {'insert_me': 'Hello I am views.py |||||| I am comming from AppTwo/index'}
    # return render(request, 'AppTwo/index.html', context=my_dict)
    return render(request, 'AppTwo/index.html')


# def help(request):
#     helpdict = {'help_insert':'HELP PAGE'}
#     return render(request, 'AppTwo/help.html', context=helpdict)
#
# def users(request):
#     user_list = User.objects.order_by('Fname')
#     user_dict = {'users' :   user_list}
#     return render(request, 'AppTwo/users.html', context=user_dict) #dir is always in quotes

def users(request):
    form = NewUserForm()

    if request.method == "POST":
        form = NewUserForm(request.POST)

        # checks if input information was entered in correctly
        if form.is_valid():
            form.save(commit=True)
            # return the index view of the request/ take you back to the homepage
            return index(request)
        else:
            print('ERROR FORM INVALAD')

    return render(request, 'AppTwo/users.html', {'form' : form})
