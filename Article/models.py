from django.db import models

class Article(models.Model):
    author = models.ForeignKey('auth.User',max_length=100,on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

class Point(models.Model):
    point = models.CharField(max_length=10)
    def __str__(self):
        return self.point


class Rating(models.Model):
    title = models.CharField(max_length=100)
    point = models.ForeignKey(Point,on_delete=models.CASCADE)
    exp = models.TextField(blank=True,null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.point



