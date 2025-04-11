from django.db import models



class Posts(models.Model):
    title = models.CharField(max_length=256)
    content = models.CharField(max_length=856)
    rate = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, null=True)



    def __str__(self):
        return self.title

