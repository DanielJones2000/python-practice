from django.db import models

# 用户类


class UserInfo(models.Model):
    # 用户ID
    id = models.CharField(max_length=32, primary_key=True)
    # 用户名称
    name = models.CharField(max_length=200)
