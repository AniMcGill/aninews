from django.db import models
from django.core.urlresolvers import reverse
import markdown

# Create your models here.

class NewsItem(models.Model):
    title = models.CharField(max_length=256)
    published = models.DateTimeField('Publish at')
    contents = models.TextField()
    contents_saved = models.TextField()
    image = models.ImageField()

    def save(self, *args, **kwargs):
        self.contents_saved = markdown.markdown(self.contents)
        super(NewsItem, self).save(*args, **kwargs)

    def __unicode__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('newsitem-detailed', args=[str(self.pk)])

    class Meta:
        ordering = ['-published']

class EventItem(NewsItem):
    when = models.DateTimeField()
    where = models.TextField()

    class Meta:
        ordering = ['when']
