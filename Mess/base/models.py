from django.db import models
# Create your models here.



from django.contrib.auth.models import User

class Attendance(models.Model):
    student = models.ForeignKey(User, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f'{self.student.username} - {self.date}'
    




class Category(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)

    class Meta:
        verbose_name_plural = "categories"

    def __str__(self):
        return self.name


class meal(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='item_images', blank=True, null= True)
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, null=True, related_name='meals')
    attendance = models.ForeignKey(Attendance, on_delete=models.CASCADE, blank=True, null=True)

    class Meta:
        verbose_name_plural = "meal"

    def __str__(self):
        return self.name
    



class Feedback(models.Model):
    name=models.CharField(max_length=100)
    email=models.EmailField()
    feedback=models.TextField()


class MealTicket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    date = models.DateField()

    def __str__(self):
        return f'{self.user.username} - {self.category.name} - {self.date}'
