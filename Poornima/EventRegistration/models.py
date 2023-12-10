from django.db import models

# Create your models here.
# class UserRegistration(models.Model):
#     user_id = models.AutoField(primary_key=True)
#     salutaion= models.CharField(max_length=5)
#     fname= models.CharField(max_length=50)
#     lname=models.CharField(max_length=50)
#     designation=models.CharField(max_length=20)
#     corresponding_email=models.EmailField(max_length=250)
#     contact=models.CharField(max_length=15,null=True,default=None)
#     university_college_name=models.CharField(max_length=50)
#     university_college_address=models.CharField(max_length=50)
#     university_college_city=models.CharField(max_length=50)

#     def __str__(self):
#         return self.fname + " "+self.lname
    

# class UserPaper(models.Model):
#     paper_id = models.AutoField(primary_key=True)
#     paper_name = models.CharField(max_length=255)
#     content = models.FileField(upload_to='research/pdfs')
#     category = models.CharField(max_length=255)
#     user_id = models.ForeignKey(UserRegistration, on_delete=models.CASCADE)
#     date = models.DateTimeField()

#     def __str__(self):
#         return self.paper_name +" "+self.category