from django.db import models
from django.utils import timezone

# Create your models here.
class Post(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=200, unique=True)
    text = models.TextField()
    is_pub = models.BooleanField('is published?', default=False) # 공개 여부
    first_pub_at = models.DateTimeField('first published time', null=True) # 최초로 공개된 시간
    pub_at = models.DateTimeField('last published time', null=True) # 공개된 시간
    edited_at = models.DateTimeField(null=True) # 업데이트된 시간

    def save(self, *args, **kwargs):
        # 첫 공개는 자동으로 기록을 남긴다.
        if not self.first_pub_at and self.is_pub:
            self.first_pub_at = timezone.now()
        
        return super(Post, self).save(*args, **kwargs)