from django.db import models

class Entry(models.Model):
    '''An entry in the journal.'''
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True, editable=False)
    date_modified = models.DateTimeField(auto_now=True, editable=False)
    
    def get_preview(self):
        preview = self.text[:60]
        if preview == "" or preview.isspace():
            preview = '[NONE]'
        return unicode(preview)

    def __unicode__(self):
        return self.get_preview()

    class Meta:
        ordering = ('-date_added',)
        verbose_name_plural = "entries"

