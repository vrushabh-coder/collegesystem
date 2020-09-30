
from django.db import models



# Create your models here.
class collage(models.Model):
    collagename = models.CharField(max_length=10,default='')

    class Meta:
        db_table = 'collage'


class TeacherDetail(models.Model):
    teach_collage = models.ForeignKey(collage, related_name='Collage_id', on_delete=models.CASCADE)
    teachername=models.CharField(max_length=20)
    teacherphone=models.IntegerField()
    tearcher_email= models.CharField(max_length=100)
    teacher_image = models.ImageField(upload_to='media', default='')

    class Meta:
        db_table = 'Teacher'


class StudentDetail(models.Model):
    student_collage = models.ForeignKey(collage, related_name='collage_id', on_delete=models.CASCADE)
    student_name=models.CharField(max_length=30)
    student_email=models.CharField(max_length=100)
    student_marks=models.CharField(max_length=10)
    student_image=models.ImageField(upload_to='media',default='')


    class Meta:
         db_table = 'student'



class Registraion(models.Model):
    firstname = models.CharField(max_length=30)
    lastname = models.CharField(max_length=30)
    username = models.CharField(unique=True,max_length=30)
    password = models.CharField(max_length=12)

    class Meta:
        db_table = "register"