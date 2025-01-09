import random
from django.core.management.base import BaseCommand
from acrobat_paro.models import User
from acrobat_paro.functions import randomname
from django.contrib.auth.hashers import make_password
from faker import Faker

# 日本語ロケールを設定
fake = Faker('ja_JP')

class Command(BaseCommand):
    help = 'Seed the database with dummy users'

    def handle(self, *args, **kwargs):
        self.stdout.write('Seeding Japanese users...')
        
        for _ in range(10):  # ユーザー10人分のダミーデータを作成
            User.objects.create_user(
                username=fake.user_name(),
                email=fake.email(),
                first_name=fake.first_name(),
                last_name=fake.last_name(),
                phone_number=fake.phone_number(),
                address=fake.address(),
                password=make_password(randomname(20)),  # 固定パスワード
                profile_image=None  # 必要なら画像を設定
            )

        self.stdout.write(self.style.SUCCESS('Successfully seeded Japanese users!'))