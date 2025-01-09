import sys ,random, string 
import img2pdf
import os
from datetime import datetime


def randomname(n):
    return ''.join(random.choices(string.ascii_letters + string.digits, k=n))

def convert_pdf():  # 1つの画像をPDF化するプログラム
    try:
        if len(sys.argv) < 2:
            raise ValueError("No Input File!")
        
        # 入力画像ファイル
        input_image = sys.argv[1]
        if not os.path.exists(input_image):
            raise ValueError("Input file does not exist!")
        
        # 入力画像ファイル名を基に保存名を生成
        base_name = os.path.splitext(os.path.basename(input_image))[0]  # ファイル名（拡張子なし）
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # 現在の日時を追加
        out_pdf_name = f"{base_name}_{timestamp}.pdf"  # 例: inputfile_20250103_123456.pdf

        # PDFレイアウト設定
        a4_layout = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
        layout = img2pdf.get_layout_fun(a4_layout)

        # PDF作成
        with open(out_pdf_name, "wb") as f:
            f.write(img2pdf.convert([input_image], layout_fun=layout))
        
        print(f"Output file: {out_pdf_name}")
    
    except ValueError as e:
        print(e)


def convert_pdfs():  # 複数の画像を1つのPDFに変換するプログラム
    try:
        if len(sys.argv) < 2:
            raise ValueError("No Input Files!")
        
        # 入力画像リスト
        input_images = sys.argv[1:-1] if len(sys.argv) > 2 else sys.argv[1:]
        
        # 入力ファイルが存在するか確認
        for img in input_images:
            if not os.path.exists(img):
                raise ValueError(f"Input file does not exist: {img}")
        
        # 保存名を確認
        if len(sys.argv) > 2 and not sys.argv[-1].lower().endswith(('.jpg', '.jpeg', '.png', '.bmp', '.gif')):
            out_pdf_name = sys.argv[-1]  # ユーザーが指定したPDF名
            if not out_pdf_name.lower().endswith(".pdf"):
                out_pdf_name += ".pdf"  # 拡張子を追加
        else:
            # デフォルトの名前
            timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")  # 現在の日時
            out_pdf_name = f"merged_{timestamp}.pdf"

        # PDFレイアウト設定 (A4)
        a4_layout = (img2pdf.mm_to_pt(210), img2pdf.mm_to_pt(297))
        layout = img2pdf.get_layout_fun(a4_layout)

        # PDF作成
        with open(out_pdf_name, "wb") as f:
            f.write(img2pdf.convert(input_images, layout_fun=layout))
        
        print(f"Output file: {out_pdf_name}")
    
    except ValueError as e:
        print(e)


