from django.db import models

# 用户类


class UserInfo(models.Model):
    # 用户ID
    id = models.CharField(max_length=32, primary_key=True, blank=False)
    # 用户名称
    displayName = models.CharField(max_length=200, blank=True)
    # 用户密码
    password = models.CharField(max_length=32, blank=True)
    # 账号
    account = models.CharField(max_length=64, blank=True)

    def __str__(self):
        return "{}".format(self.displayName)
