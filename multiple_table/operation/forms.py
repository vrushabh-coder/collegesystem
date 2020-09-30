from  django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import StudentDetail
from .models import TeacherDetail
from .models import collage,Registraion




class Collageform(forms.ModelForm):
    class Meta:
        model = collage
        fields ='__all__'

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = StudentDetail
        fields ='__all__'

class TeacherRegistration(forms.ModelForm):
    class Meta:
        model =TeacherDetail
        fields = '__all__'


class Registrationform(forms.ModelForm):
    class Meta:
        model= Registraion
        fields ='__all__'

class SignupForm(UserCreationForm):
    username = forms.CharField(max_length=50)
    email = forms.EmailField(max_length=100)

    class Meta:
        model = User
        fields = ('username','email','password1','password2')


from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegisterForms(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email']


