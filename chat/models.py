from django.db import models

# Create your models here.

class User(models.Model):
    # id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    content = models.TextField()
    # upload_to参数，用来指定上传上来的文件保存到哪里
    file = models.FileField(upload_to="media/%Y%m%d/")   # verbose_name='文件'

    create_time = models.DateTimeField(auto_now_add=True, verbose_name='Create time')   # 后台 admin 不会显示
    update_time = models.DateTimeField(auto_now=True, verbose_name='Update time')
    delete_time = models.DateTimeField(null=True, blank=True,  verbose_name='Delete time')

    parent_folder = models.ForeignKey(Folder, null=True, blank=True, on_delete=models.CASCADE, verbose_name = '父文件夹')
    parent_id = models.IntegerField(default=None, null=True, blank=True, verbose_name='父文件夹ID')