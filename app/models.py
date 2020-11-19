from django.db import models

from users.models import User


class Item(models.Model):


    #タイトル
    title = models.CharField(
        verbose_name='タイトル',
        max_length=20,
        blank=True,
        null=True,
    )

    #メモ
    memo = models.TextField(
        verbose_name='メモ',
        blank=True,
        null=True,
    )

    #日付
    date = models.DateField(
        verbose_name='日付',
        blank=True,
        null=True,
    )


    #作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )



    def __str__(self):

        return self.title

    class Meta:
     
        verbose_name = 'メモ'
        verbose_name_plural = 'メモ'
