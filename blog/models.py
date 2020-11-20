from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super(PublishedManager,
                     self).get_queryset()\
                        .filter(status='published')

class Post(models.Model):
    def get_absolute_url(self):
        return reverse('blog:post_detail', args=[
            self.publish.year,
            self.publish.month,
            self.publish.day,
            self.slug
        ])
    STATUS_CHOICES =   (
        ('default', 'Default'),
        ('published' ,'published')
    )
    body = models.TextField()
    title = models.CharField(max_length=250)
    author = models.ForeignKey(User, on_delete=models.CASCADE,)
    slug = models.SlugField(max_length=250,unique_for_date='publish')
    status = models.CharField(max_length=10, choices=STATUS_CHOICES,default='draft')
    publish = models.DateField(default=timezone.now)
    objects = models.Manager()  
    published = PublishedManager() 


    
    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title

#class Post(models.Model):
    

# Create your models here.
