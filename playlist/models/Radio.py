from django.db import models

class Radio(models.Model):
    radio_id = models.AutoField(primary_key=True)
    radio_name = models.CharField(max_length=100)
    radio_description = models.TextField(blank=True, null=True)
    
    class meta:
            app_label = 'playlist'

    def __str__(self):
            return f'{self.radio_name}'
