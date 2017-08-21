# coding: utf-8
from __future__ import unicode_literals

import datetime
from django.db import models

# Create your models here.
from django.utils.timezone import get_current_timezone


class BaseModel(models.Model):
    create_time = models.DateTimeField(auto_now_add=True)
    modify_time = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class ICOProject(BaseModel):
    """
    ICO 项目
    """
    status_choice = (
        (1, '未开始'),
        (2, '进行中'),
        (3, '已结束')
    )

    name = models.CharField(max_length=128)
    logo = models.CharField(max_length=256, default='')
    url = models.CharField(max_length=256, default='#')
    status = models.IntegerField(default=1, choices=status_choice)
    start_time = models.DateTimeField(default=None, null=True, blank=True)
    end_time = models.DateTimeField(default=None, null=True, blank=True)

    def __unicode__(self):
        return self.name


class Exchange(BaseModel):
    """
    交易所或众筹网站
    """
    name = models.CharField(max_length=64, unique=True)
    url = models.CharField(max_length=256, default='#')
    logo = models.CharField(max_length=256, default='')

    def __unicode__(self):
        return self.name


class Currency(BaseModel):
    """
    货币
    """
    name = models.CharField(max_length=64, unique=True)
    abbr = models.CharField(max_length=10, unique=True)
    logo = models.CharField(default='')

    def __unicode__(self):
        return self.name


class ExchangeICOProject(BaseModel):
    """
    交易所 ICO 项目
    """
    ico = models.ForeignKey(ICOProject, related_name='ico_exchanges')
    exchange = models.ForeignKey(Exchange, related_name='exchange_icos')
    currency = models.ForeignKey(Currency, related_name='currency_icos')
    url = models.CharField(max_length=256, default='')
    total_amount = models.FloatField(default=0.0)
    current_amount = models.FloatField(default=0.0)
    percent = models.FloatField(default=0.0)
    ico_cost = models.FloatField(default=0.0)
    market_value = models.FloatField(default=0.0)

    def __unicode__(self):
        return '{0}-{1}'.format(self.exchange.name, self.ico.name)