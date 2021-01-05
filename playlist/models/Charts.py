from django.db import models

class Charts(models.Model):
    charts_genre = models.AutoField(primary_key=True)
    charts_name = models.CharField(max_length=100)

    class meta:
        app_label = 'playlist'

    def __str__(self):
        return f'{self.chartsradio_name}'