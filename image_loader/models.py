from django.core.exceptions import ValidationError
from django.db import models


def validate_image(fieldfile_obj):
    filesize = fieldfile_obj.size
    megabyte_limit = 0.2
    if filesize > megabyte_limit*1024*1024:
        raise ValidationError("Размер фотографии больше %sMB" % str(megabyte_limit))


class Image(models.Model):
    title = models.CharField(max_length=50, verbose_name='Название', unique=True)
    image = models.ImageField(
        upload_to='image',
        verbose_name='Изображение',
        validators=(validate_image,),
        help_text='Maximum file size allowed is 0.2Mb'
    )
    created = models.DateTimeField(auto_now=True, verbose_name='Дата и время создания')

    class Meta:
        verbose_name = 'Изображение'
        verbose_name_plural = 'Изображения'

    def __str__(self):
        return self.title
