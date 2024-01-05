from django.db import models



class Category(models.Model):
    name = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200,unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class BlogPost(models.Model):
    category = models.ForeignKey(Category,on_delete=models.PROTECT)
    title = models.CharField(max_length=200)
    content = models.TextField()
    image = models.ImageField(upload_to="blog_images/",null=True,blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return self.title