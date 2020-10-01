from django.contrib.auth import password_validation

from . import forms
from django.shortcuts import render, redirect, HttpResponse
from django.urls.base import reverse
from django.contrib.auth import login,authenticate
from django.core.mail import send_mail
from django.conf import settings
from .forms import SignupForm
from django.contrib.messages.views import SuccessMessageMixin
from .forms import Registrationform
from django.views import View
from .forms import Collageform
from .forms import UserRegisterForms
from django.contrib import messages
from .models import collage, TeacherDetail, StudentDetail, Registraion
from django.db.models import Q
from itertools import chain
from django.contrib.auth.forms import AuthenticationForm

from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template


# def show(request):
# return render(request, "show.html")
def signup_view(request):
    subject = "thank you for registration to our site"
    message = "you have successfully created an account"
    email_form = settings.EMAIL_HOST_USER
    if request.method == 'POST':
        form = SignupForm(request.POST)
        print(form)
        if form.is_valid():
            form.save()
            email = form.changed_data.get('email')
            recipient_list = [email, ]
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.post('password')
            user = authenticate(username=username, password=password)
            send_mail(subject, message, email_form, recipient_list)
            login(request, user)
            return redirect('app:home')
    else:
        form = SignupForm()
    return render(request, 'singup.html',{'form': form})












class College(View):
    def get(self, request):

        return render(request, "collage.html")

    def post(self, request):

        try:
            collageName = collage(collagename=request.POST["collagename"])
            collageName.save()

        except Exception:
            return render(request, "collage.html", {'error': "ValueError"})
        return redirect(reverse('show'))


class collageshow(View):

    def get(self, request):
        collagelist = collage.objects.all()
        return render(request, "show.html", {'collageshow': collagelist})


class collageEdit(View):

    def get(self, request, id):
        collageedite = collage.objects.get(id=id)
        return render(request, 'edit.html', {'collage_edite': collageedite})


class CollegeUpDate(View):

    def post(self, request, id):
        clg = collage.objects.get(id=id)
        clg.collagename = request.POST["collage"]
        clg.save()
        messages.success(request, "Collage detail updated")
        return redirect(reverse('show'))


class CollegeDelete(View):

    def get(self, request, id):
        bank_delete = collage.objects.get(id=id)
        bank_delete.delete()
        messages.success(request, "collage successfully deletd")
        return redirect(reverse('show'))


class Teacher(View):

    def get(self, request, id):
        return render(request, "teacher.html")

    def post(self, request, id):
        try:
            teacher = TeacherDetail(
                teach_collage_id=id,
                teachername=request.POST["name"],
                teacherphone=request.POST["phone"],
                tearcher_email=request.POST["email"],
                teacher_image=request.POST["image"]

            )
            teacher.save()
        except Exception:
            return render(request, "teacher.html", {'error': "ValueError"})
        return redirect(reverse('show'))


class Teachershow(View):
    def get(self, request, id):
        teacherList = TeacherDetail.objects.filter(teach_collage_id=id)

        return render(request, "teachershow.html", {'teacher_detail': teacherList})


class TeacherEdit(View):

    def get(self, request, id):
        teacherdetail = TeacherDetail.objects.get(id=id)
        return render(request, 'TeacherEdit.html', {'teacher_edit': teacherdetail})


class TeacherUpDate(View):
    def post(self, request, id):
        teacher = TeacherDetail.objects.get(id=id)
        collid = teacher.teach_collage_id
        teacher.teachername = request.POST["name"]
        teacher.teacherphone = request.POST["phone"]
        teacher.tearcher_email = request.POST["email"]
        teacher.save()
        messages.success(request, "Teacher deatail updated")
        return redirect(reverse('teacher_show', kwargs={'id': collid}))


class TeacherDelete(View):

    def get(self, request, id):
        teacher_delete = TeacherDetail.objects.get(id=id)
        collid = teacher_delete.teach_collage_id
        teacher_delete.delete()
        messages.success(request, "Teacherdetail successfully deletd")
        return redirect(reverse('teacher_show', kwargs={'id': collid}))


class Student(View):
    def get(self, request, id):
        return render(request, "student.html")

    def post(self, request, id):
        try:
            student = StudentDetail(
                student_collage_id=id,
                student_name=request.POST["name"],
                student_marks=request.POST["mark"],
                student_email=request.POST["email"],
                student_image=request.POST["image"]
            )
            student.save()
        except Exception:
            return render(request, "student.html", {'error': "ValueError"})
        return redirect(reverse('show'))


class StudentShow(View):
    def get(self, request, id):
        student_list = StudentDetail.objects.filter(student_collage_id=id)
        return render(request, "Studentshow.html", {'student_detail': student_list})


class StudentEdit(View):

    def get(self, request, id):
        studentdetail = StudentDetail.objects.get(id=id)
        return render(request, 'StudentEdit.html', {'student_edit': studentdetail})


class StudentUpDate(View):
    def post(self, request, id):
        student = StudentDetail.objects.get(id=id)
        collid = student.student_collage_id
        student.student_name = request.POST["name"]
        student.student_marks = request.POST["mark"]
        student.student_email = request.POST["email"]
        student.save()
        messages.success(request, "Studentdetail successfully update")
        return redirect(reverse('show_student', kwargs={'id': collid}))


class StudentDelete(View):
    def get(self, request, id):
        studentdelete = StudentDetail.objects.get(id=id)
        collid = studentdelete.student_collage_id

        studentdelete.delete()
        messages.success(request, "Studentdetail successfully deletd")
        return redirect(reverse('show_student', kwargs={'id': collid}))


def index(request):
    if request.method == 'POST':
        member = Registraion(username=request.POST['username'], password=request.POST['password'],
                             firstname=request.POST['firsthand'], lastname=request.POST['laminae'])
        member.save()

        messages.success(request, 'successfully Register!')
        return redirect('/')
    else:
        return render(request, 'index.html')


def login(request):
    messages.success(request, "successfully login")
    return render(request, 'login.html')


def home(request):
    if request.method == 'POST':
        if Registraion.objects.filter(username=request.POST['username'], password=request.POST['password']).exists():
            member = Registraion.objects.get(username=request.POST['username'], password=request.POST['password'])
            return render(request, 'home.html', {'member': member})
        else:
            context = {'msg': 'Invalid username or password'}
            return render(request, 'login.html', context)


def search(request):
    query = request.GET['query']

    if query:
        student_show = StudentDetail.objects.filter(student_name=query)

    else:
        messages.error(request, 'no result found')
    return render(request, "search.html", {'student_detail': student_show})


class Password_Reset_View(View):

    def get(self, request):
        return render(request, "password_reset_for.html")

    def post(self, request):

        emailid = request.POST["find"]

        print(emailid)

        if emailid:
            password = Registraion.objects.filter(username=emailid)
            print(password)
            return render(request, "password_reset_con.html", {"email_id": emailid})
        else:
            messages.error(request, 'no result found')


class Password_ResetDone(View):
    def post(self, request):
        email_id = request.POST["email_id"]
        print(email_id)
        password = request.POST["conform_password"]
        print(password)
        password_update = Registraion.objects.get(username=email_id)
        password_update.password=request.POST["conform_password"]
        password_update.save()
        return render(request, "login.html")

def Homepage(request):
    return render(request,'home.html')

def register(request):
    if request.method == 'POST':
        form = UserRegisterForms(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            ######################### mail system ####################################
            htmly = get_template('Email.html')
            d = {'username': username}
            subject, from_email, to = 'welcome', 'your_email@gmail.com', email
            html_content = htmly.render(d)
            msg = EmailMultiAlternatives(subject, html_content, from_email, [to])
            msg.attach_alternative(html_content, "text / html")
            msg.send()
            ##################################################################
            messages.success(request, f'Your account has been created ! You are now able to log in')
            return redirect('login')
    else:
        form = UserRegisterForms()
    return render(request, 'register.html', {'form': form, 'title': 'reqister here'})



