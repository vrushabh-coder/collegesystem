from django.contrib import admin
from django.urls import path
from operation import views
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from .import views

from django.urls import path, include
from django.conf import settings
from . import views
from django.conf.urls.static import static


from django.contrib.auth import views as auth_views
from .views import College, collageEdit, collageshow, CollegeUpDate, CollegeDelete, Teacher, TeacherDelete, TeacherEdit,\
    Teachershow, TeacherUpDate, Student, StudentDelete, StudentEdit , StudentShow , StudentUpDate,  \
    Password_Reset_View,Password_ResetDone

app_name = 'app'
urlpatterns = [

    path("collage/", College.as_view(), name='add'),
    path('show/', collageshow.as_view(), name='show'),
    path('edit/<int:id>', collageEdit.as_view(), name='edit'),
    path('update/<int:id>', CollegeUpDate.as_view(), name='update'),
    path('delete/<int:id>', CollegeDelete.as_view(), name='delete'),
    path("teacher/<int:id>", Teacher.as_view(), name='attache'),
    path('TeacherShow/<int:id>', Teachershow.as_view(), name='teacher_show'),
    path('teacheredit/<int:id>', TeacherEdit.as_view(), name='editteacher'),
    path('teacherupdate/<int:id>', TeacherUpDate.as_view(), name='updateteacher'),
    path('teacherdelete/<int:id>', TeacherDelete.as_view(), name='deleteteacher'),
    path("Student/<int:id>", Student.as_view(), name='student'),
    path('showStudent/<int:id>', StudentShow.as_view(), name='show_student'),
    path('editStudent/<int:id>', StudentEdit.as_view(), name='student_edit'),
    path('updateStudent/<int:id>', StudentUpDate.as_view(), name='student_update'),
    path('deleteStudent/<int:id>', StudentDelete.as_view(), name='student_delete'),
    path('', views.index,name='index'),
    path('login/', views.login),
    path('home/', views.home),
    path('search/',views.search,name='search'),
    # path('password_reset/',Password_Reset_View.as_view(),name='password_reset'),
    # path('password_new/',Password_ResetDone.as_view(),name='password_reset_done'),
    path('singup/',views.signup_view,name='signup'),
    path('home1/',views.Homepage,name='home'),

    #path('resets/<uidb64>/<token>/',auth_views.Password_Reset_ConfirmView.as_view(),name='password_reset_confirm'),
    #path('resets_password_complete/',auth_views.Password_Reset_CompleteView.as_view(),name='password_reset_complete'),
    #path('reset_password/',auth_views.PasswordResetView.as_view(),name='reset_password'),
    #path('reset_password_sent/',auth_views.PasswordResetDoneView.as_view(),name='password_reset_done'),
    #path('reset/<uidb64>/<token>/',auth_views.PasswordResetConfirmView.as_view(),name='password_reset_confirm'),
    #path('reset_password_complete/',auth_views.PasswordResetView.as_view(),name='password_reset_complete'),
    # path('password_new/',auth_views.PasswordResetDone.as_view(),name='password_reset_done'),
    # path('resets/<uidb64>/<token>/',auth_views.Password_Reset_ConfirmView.as_view(),name='password_reset_confirm'),
    # path('resets_password_complete/',auth_views.Password_Reset_CompleteView.as_view(),name='password_reset_complete'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)