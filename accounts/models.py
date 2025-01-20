from django.db import models
from django.contrib.auth.models import AbstractUser

class Created_PDF(models.Model):
    #migrationsのinitial.pyを見ると分かるように、Djangoでは、明示的にAutoFieldを指定しなくても、
    #モデルにプライマリキーが設定されていない場合、自動的にidフィールドがAutoFieldとして作成される
    file_name = models.CharField(max_length=100,help_text="作成したPDF名")
    description = models.TextField(null=True,blank=True,help_text="作成したPDFを説明する文章（任意）")
    file_path = models.FileField(upload_to='pdfs/') #アップロード先のディレクトリを指定。この場合、MEDIA_ROOT/pdfs/にファイルが保存される
    created_at = models.DateTimeField(auto_now_add=True,help_text="作成日時")
    updated_at = models.DateTimeField(auto_now=True,null=True,help_text="更新日時")
    delete_flag = models.BooleanField(null=True,help_text="論理削除用フラッグ")

    def __str__(self):
        return f'<CreatedPdf:id={self.id}, {self.file_name}: {self.description}>'

class User(AbstractUser):
    # 必要に応じて追加フィールドを定義
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    address = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    groups = models.ManyToManyField(
        'auth.Group',
        related_name='acrobat_paro_user_set',  # 変更
        blank=True,
        help_text='The groups this user belongs to.',
        verbose_name='groups',
    )
    user_permissions = models.ManyToManyField(
        'auth.Permission',
        related_name='acrobat_paro_user_permissions_set',  # 変更
        blank=True,
        help_text='Specific permissions for this user.',
        verbose_name='user permissions',
    )
    def __str__(self):
        return self.username
    
class Partner_Company(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField(max_length=200)
    address = models.TextField(blank=True, null=True)    
    phone_number = models.CharField(max_length=15, blank=True, null=True)

    def __str__(self):
        return '<Partner_Company:id=' + str(self.id) + ', ' + self.name +\
            '(' + str(self.mail) + ', ' + str(self.phone_number) + ')>'
    # 管理ツールで登録したレコードを表示するときにどのように表示されるか

