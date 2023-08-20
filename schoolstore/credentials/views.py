from django.contrib.auth.models import User
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib import auth
from django import forms

# Create your views here.


def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('new_page')
        else:
            messages.error(request, "Invalid credentials")
            return redirect('login')

    return render(request, "login.html")



def new_page(request):
    return render(request, 'regbtn.html')




class RegistrationForm(forms.Form):
    name = forms.CharField(max_length=100)
    dob = forms.DateField()
    age = forms.IntegerField()
    gender = forms.ChoiceField(choices=[('male', 'Male'), ('female', 'Female'), ('other', 'Other')])
    phone = forms.CharField(max_length=20)
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    department = forms.ChoiceField(
        choices=[('Computer_science', 'Computer Science'), ('Commerce', 'Commerce'), ('Bio_Science', 'Bio Science'),
                 ('Home_Science', 'Home Science'), ('Humanities', 'Humanities')])
    course = forms.ChoiceField(choices=['get_courses'], required=False)  # We'll populate this dynamically
    purpose = forms.ChoiceField(choices=[('enquiry', 'Enquiry'), ('order', 'Place Order'), ('return', 'Return')])
    materials_provided = forms.MultipleChoiceField(choices=[
        ('notebook', 'Notebook'), ('pen', 'Pen'), ('papers', 'Exam Papers')
    ], widget=forms.CheckboxSelectMultiple)

def registration_form(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            # Process form data here (e.g., save to database)
            message = "Registration Successful"
        else:
            message = "Form contains errors. Please correct them and try again."
    else:
        form = RegistrationForm()

    return render(request, "regform.html", {'form': form})



def get_courses(request):
    department = request.GET.get('department')
    courses = []
    if department == 'Computer_science':
        courses = [('bsc', 'BSc'), ('honers', 'Honers')]
    elif department == 'Commerce':
        courses = [('bba', 'BBA'), ('b.com', 'B.Com')]
    elif department == 'Bio_Science':
        courses = [('bsc', 'BSc'), ('honers', 'Honers')]
    elif department == 'Home_Science':
        courses = [('bsc', 'BSc'), ('honers', 'Honers')]
    elif department == 'Humanities':
        courses = [('history', 'History'), ('geography', 'Geography')]

    return render(request, 'course_dropdown_options.html', {'courses': courses})


def register(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password1 = request.POST['password1']
        if password == password1:
            if User.objects.filter(username=username).exists():
                messages.info(request, "Username Taken")
                return redirect('register')
            else:
                user = User.objects.create_user(username=username, password=password,)
                user.save();
                return redirect('login')

        else:
            messages.info(request, "password is not matching")
            return redirect('register')
        return redirect('/')
    return render(request, "register.html")


def logout(request):
    auth.logout(request)
    return redirect('/')


from django.shortcuts import render

# Create your views here.
