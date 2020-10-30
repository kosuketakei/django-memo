from django.db import models

from users.models import User


class Item(models.Model):


    # サンプル項目1 文字列
    title = models.CharField(
        verbose_name='タイトル',
        max_length=20,
        blank=True,
        null=True,
    )

    # サンプル項目2 メモ
    memo = models.TextField(
        verbose_name='メモ',
        blank=True,
        null=True,
    )

    # サンプル項目7 日付
    date = models.DateField(
        verbose_name='日付',
        blank=True,
        null=True,
    )



    



    # 以下、管理項目

    # 作成者(ユーザー)
    created_by = models.ForeignKey(
        User,
        verbose_name='作成者',
        blank=True,
        null=True,
        related_name='CreatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 作成時間
    created_at = models.DateTimeField(
        verbose_name='作成時間',
        blank=True,
        null=True,
        editable=False,
    )

    # 更新者(ユーザー)
    updated_by = models.ForeignKey(
        User,
        verbose_name='更新者',
        blank=True,
        null=True,
        related_name='UpdatedBy',
        on_delete=models.SET_NULL,
        editable=False,
    )

    # 更新時間
    updated_at = models.DateTimeField(
        verbose_name='更新時間',
        blank=True,
        null=True,
        editable=False,
    )

    def __str__(self):

        return self.title

    class Meta:
     
        verbose_name = 'メモ'
        verbose_name_plural = 'メモ'
