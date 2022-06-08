from django.db import models

# Create your models here.


class QuestionPackage(models.Model):
    title = models.CharField(max_length=150)
    content = models.TextField(blank=True)
    question_quantity = models.IntegerField()
    
    def __str__(self) -> str:
        return self.title



class Questions(models.Model):
    pack_id = models.ForeignKey(QuestionPackage, on_delete=models.CASCADE)
    pack_name = models.TextField()
    question_id = models.TextField(primary_key=True)
    question_text = models.TextField()
    is_image = models.BooleanField()
    photo = models.ImageField(upload_to='photos/%Y/%M/%D/', blank=True)
    answer = models.TextField() 

    def __str__(self):
        return self.question_text[:50]
    
    #class Meta:
    #   managed = False
    #   db_table = 'Questions'
    #   verbose_name = "Question"
    #   verbose_name_plural = "Questions"
    #   ordering = ['pack_name']
