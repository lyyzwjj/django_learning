from django.db import models


class BookInfo(models.Model):
    '''图书模型类'''
    btitle = models.CharField(max_length=20)
    bname = models.CharField(max_length=20)
    bpub_date = models.DateTimeField(max_length=20)
    bsell_date = models.DateField()

    def __str__(self):
        return self.btitle


class HeroInfo(models.Model):
    ''' 英雄人物类 '''
    hname = models.CharField(max_length=20)
    hgender = models.BooleanField(default=False)
    hcomment = models.CharField(max_length=128)
    hbook = models.ForeignKey('BookInfo', on_delete=models.CASCADE)

    def __str__(self):
        return self.hname
