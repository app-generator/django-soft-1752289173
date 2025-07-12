# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class Property(models.Model):

    #__Property_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)

    #__Property_FIELDS__END

    class Meta:
        verbose_name        = _("Property")
        verbose_name_plural = _("Property")


class Unit(models.Model):

    #__Unit_FIELDS__
    property = models.ForeignKey(Property, on_delete=models.CASCADE)

    #__Unit_FIELDS__END

    class Meta:
        verbose_name        = _("Unit")
        verbose_name_plural = _("Unit")


class Tenant(models.Model):

    #__Tenant_FIELDS__
    user = models.CharField(max_length=255, null=True, blank=True)

    #__Tenant_FIELDS__END

    class Meta:
        verbose_name        = _("Tenant")
        verbose_name_plural = _("Tenant")



#__MODELS__END
