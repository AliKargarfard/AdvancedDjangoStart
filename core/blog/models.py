from django.db import models

# Create your models here.
class Post (models.Model):
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    image = models.ImageField(null=True, blank=True)
    category = models.ForeignKey('Category', on_delete=models.SET_NULL,null=True)
    status = models.BooleanField()
    content = models.TextField()

    created_date = models.DateTimeField(auto_now_add=True)
    updated_date = models.DateTimeField(auto_now=True)
    published_date = models.DateTimeField()

    def __str__(self):
        return self.title
    
class category(models.Model):
    name  = models.CharField(max_length=250)    

    def __str__(self):
        return self.name


