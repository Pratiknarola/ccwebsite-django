from django.forms import ModelForm
# from django.contrib.auth.models import User
# from django.contrib import admin
# from ckeditor.widgets import CKEditorWidget
from post.models import Post, Tags
# from ckeditor_uploader.widgets import CKEditorUploadingWidget
# from multiselectfield import MultiSelectField


class PostForm(ModelForm):

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']
