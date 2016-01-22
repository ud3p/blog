# coding: utf-8
from django.contrib.auth.models import User
from django.db import models


class Post(models.Model):
    author = models.ForeignKey(to=User, verbose_name=u'Автор')
    name = models.CharField(max_length=255, verbose_name=u'Название')
    game_id = models.CharField(max_length=255, verbose_name=u'GameID')
    link = models.TextField(verbose_name=u'Link')
    #text = models.TextField(verbose_name=u'Текст')
    step_2 = models.TextField(verbose_name=u'Шаг_2', default=u'2. ', blank=True)
    step_3 = models.TextField(verbose_name=u'Шаг_3', default=u'3. ', blank=True)
    step_4 = models.TextField(verbose_name=u'Шаг_4', default=u'4. ', blank=True)

    created_at = models.DateTimeField(auto_now_add=True, verbose_name=u'Дата публикации')
    
    #rating = models.IntegerField(default=0, verbose_name=u'Рейтинг')
    #is_private = models.BooleanField(default=False, verbose_name=u'Приватная статья?')
    #is_delete = models.BooleanField(default=False, verbose_name=u'Удаленная статья?')

    def __unicode__(self):
        return self.name

    class Meta(object):
        db_table = 'habraposts'
        ordering = ['-created_at',]
