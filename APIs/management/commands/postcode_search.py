from django.core.management.base import BaseCommand
import requests
import json

class Command(BaseCommand):
    help = "指定した郵便番号の住所を検索"

    def add_arguments(self, parser):
        parser.add_argument("zipcode", type=str, help="検索する郵便番号")

    def handle(self, *args, **options):
        zip_code = options["zipcode"]

        # 郵便番号APIのURL
        url = "https://zipcloud.ibsnet.co.jp/api/search"
        params = {"zipcode": zip_code}

        res = requests.get(url, params)
        data = res.json()

        if data.get("results"):
            address_info = data["results"][0]
            address = f"{address_info['address1']} {address_info['address2']} {address_info['address3']}"
            self.stdout.write(self.style.SUCCESS(f"郵便番号: {zip_code}\n住所: {address}"))
        else:
            self.stdout.write(self.style.ERROR("住所情報が見つかりませんでした。"))
