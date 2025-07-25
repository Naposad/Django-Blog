from django.contrib.auth import get_user_model
from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse

# Create your models here.
User = get_user_model()

class BlogPost(models.Model):
    title = models.CharField(max_length=255, unique=True, verbose_name="Titre")
    slug = models.SlugField(max_length=255, unique=True, blank=True)
    author = models.ForeignKey(User,on_delete=models.SET_NULL, blank=True, null=True)
    last_update = models.DateTimeField(auto_now=True)
    created_on = models.DateField(blank=True, null=True)
    published = models.BooleanField(default=False, verbose_name="Publié")
    content = models.TextField(blank=True, verbose_name="Contenu")
    image = models.ImageField(blank=True, upload_to="blog", default="{% static 'css/gettyimages-1986209604-594x594.jpg' %}")


    class Meta:
        ordering = ['-created_on']
        verbose_name = "Article"

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        if not self.image:
            self.image = "{% static 'css/gettyimages-1986209604-594x594.jpg' %}"
        super().save(*args, **kwargs)

    def author_or_default(self):
        return self.author if self.author else "auteur inconnu"

    def get_absolute_url (self):
        return reverse('posts:home')
