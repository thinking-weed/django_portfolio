from django.db import models

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
    

