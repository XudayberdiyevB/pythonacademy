from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User

class ProblemModel(models.Model):
    sequence_number = models.CharField(max_length=10)
    name = models.CharField(max_length=1000)
    content = RichTextUploadingField(blank=True, null=True)
    difficulty = models.CharField(max_length=20)
    topic = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True,null=True)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('problem_detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):  # new
        if not self.slug:
            self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

class ProblemAnswerModelUser(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    problem=models.ForeignKey(ProblemModel,on_delete=models.CASCADE)
    answer_code_text=models.TextField()
    answer_send_date=models.DateTimeField(auto_now_add=True)
    is_correct=models.BooleanField(default=False)
    is_waiting=models.BooleanField(default=True)
    answer_error_text=models.TextField(null=True,blank=True)
    send_answer_date=models.DateTimeField(auto_now_add=True)
    


    def __str__(self):
        return f"{self.user}-{self.problem}-{self.is_correct}"


