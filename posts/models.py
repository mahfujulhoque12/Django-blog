from django.db import models
from django.utils import timezone
from django_extensions.db.fields import AutoSlugField
from taggit.managers import TaggableManager  
from django.contrib.auth.models import User
from django_quill.fields import QuillField
from django.utils.translation import gettext as _
from django_editorjs_fields import EditorJsTextField


# Create your models here
    


class Post(models.Model):
    class PostType(models.TextChoices):
        RESEARCH = 'RESEARCH', _('Research')
        SERVICES = 'SERVICES', _('Services')
        PRODUCTS = 'PRODUCTS', _('Products')
        NEWS = 'NEWS', _('News')
        DATABASE = 'DATABASE', _('Database')
        CUSTOMERS = 'CUSTOMERS', _('Customers')
        EDA = 'EDA',_('Eda')

    created_at = models.DateTimeField(default=timezone.now, editable=True)
    updated_at = models.DateTimeField(default=timezone.now, editable=True)
    post_type = models.CharField(choices=PostType.choices, max_length=250)
    title = models.CharField(max_length=255, null=True, blank=True)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to='post_thumbnail', null=True, blank=True)
    cover_photo = models.ImageField(upload_to='post_cover_photo', null=True, blank=True)
    slug = AutoSlugField(populate_from='title', editable=True, unique=True)
    keywords = TaggableManager(help_text="comma seperated keywords", blank=True)
    summary = QuillField(null=True, blank=True)
    external_url = models.URLField(blank=True, null=True)
    external_url_endpoint = models.CharField(max_length=250, blank=True, null=True)
    external_url_title = models.CharField(max_length=250, blank=True, null=True)
    headers_content = QuillField(blank=True, null=True)
    content_en = EditorJsTextField(blank=True, null=True)
    content_ja = EditorJsTextField(blank=True, null=True)
    content_de = EditorJsTextField(blank=True, null=True)



   
    
