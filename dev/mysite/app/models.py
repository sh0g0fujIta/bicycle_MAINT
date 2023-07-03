from django.db import models
# from .forms import BicycleBrandForm

# Create your models here.
Brand_Choices = (
    ('ALL-CITY', 'オールシティ'),
    ('ANCHOR', 'アンカー'),
    ('ARAYA', 'アラヤ'),
    ('ARGON18', 'アルゴンエイティーン'),
    ('AVEDIO', 'エヴァディオ'),
    ('BASSO', 'バッソ'),
    ('BE-ALL', 'ビーオール'),
    ('BH BIKES', 'ビーエイチ バイクス'),
    ('BIANCHI', 'ビアンキ'),
    ('BLUE', 'ブルー'),
    ('BMC', 'ビーエムシー'),
    ('BOMA', 'ボーマ'),
    ('BOOTLEG', 'ブートレック'),
    ('BOTTECCHIA', 'ボッテキア'),
    ('CALAMITA', 'カラミータ'),
    ('CANNONDALE', 'キャノンデール'),
    ('CARRERA', 'カレラ'),
    ('CASATI', 'カザーティ'),
    ('CENTURION', 'センチュリオン'),
    ('CERVELO', 'サーヴェロ'),
    ('CHERUBIN', 'ケルビム'),
    ('CHINELLI', 'チネリ'),
    ('CIELO', 'シエロ'),
    ('CIPOLLINI', 'チッポーニ'),
    ('COLNAGO', 'コルナゴ'),
    ('CORRATEC', 'コラテック'),
    ('DACCORD', 'ダコルディ'),
    ('DE ROSA', 'デ・ローザ'),
    ('DEDACCIAI STRADA', 'テダテャイ ストラーダ'),
    ('EDDYMERCKX', 'エディメルクス'),
    ('FELT', 'フェルト'),
    ('FOCUS', 'フォーカス'),
    ('FONDRIEST', 'フォンドリエスト'),
    ('FUJI', 'フジ'),
    ('GARNEAU', 'ガノー'),
    ('GIANT', 'ジャイアント'),
    ('GIOS', 'ジオス'),
    ('GT', 'ジーティー'),
    ('GUERCOTTI', 'グエルチョッティ'),
    ('INTERMAX', 'インターマックス'),
    ('JAMIS', 'ジェイミス'),
    ('KESTREL', 'ケストレル'),
    ('KHS', 'ケイ・ヘイチ・エス'),
    ('KOGA', 'コガ'),
    ('KONA', 'コナ'),
    ('KUOTA', 'クォータ'),
    ('LAPIERRE', 'ラピエール'),
    ('LEVEL', 'レベル'),
    ('LITESPEED', 'ライトスピード'),
    ('LOOK', 'ルック'),
    ('LOUISGARNEAU', 'ルイガノ'),
    ('MANHATTAN BIKE', 'マンハッタン バイク'),
    ('MASI', 'マジィ'),
    ('MBK', 'エムビーケー'),
    ('MERIDA', 'メリダ'),
    ('MIYATA JAPON', 'ミヤタ ジャポン'),
    ('MOOTS', 'ムーツ'),
    ('MUSEEUW', 'ムセウ'),
    ('NEILPRYDE', 'ニールプライド'),
    ('NEVI', 'ネービ'),
    ('OPERA', 'オペラ'),
    ('OPUS', 'オーパス'),
    ('ORBEA', 'オルベア'),
    ('PANASONIC', 'パナソニック'),
    ('PARLEE', 'パーリー'),
    ('PENNAROLA', 'ペンナローラ'),
    ('PINARELLO', 'ピナレロ'),
    ('PASSONI', 'パッソーニ'),
    ('RALEIGH', 'ラレー'),
    ('RHIDLEY', 'リドレー'),
    ('RITCHEY', 'リッチー'),
    ('RITEWYA', 'ライトウェイ'),
    ('SCHWINN', 'シュウィン'),
    ('SCOTT', 'スコット'),
    ('SPECIALIZED', 'スペシャライズド'),
    ('STORCK', 'ストーク'),
    ('SURLY', 'サーリー'),
    ('TIME', 'タイム'),
    ('TREK', 'トレック'),
    ('VELLUMCYCLES', 'ヴェラムサイクル'),
    ('WILIER', 'ウィリエール'),
    ('ZULLO', 'ズッロ'),           
)
    
class Toppage(models.Model):
    title = models.CharField('タイトル', max_length=100, null=True, blank=True)
    subtitle = models.CharField('サブタイトル', max_length=100, null=True, blank=True)
    topimage = models.ImageField(upload_to='images/', verbose_name='トップ画像')
    
    def __str__(self):
        return self.title


class Color(models.Model):
    color = models.CharField('色', max_length=100, null=True, blank=True)

    def __str__(self):
        return self.color
    
class Bicycle(models.Model):

    image = models.ImageField(upload_to='images/bycycle/', verbose_name='登録する自転車の画像')
    brand = models.CharField('ブランド', max_length=100, choices=Brand_Choices)
    model = models.CharField('モデル', max_length=100, null=True, blank=True)
    year = models.CharField('年式', max_length=100, null=True, blank=True)
    update_at = models.DateTimeField('更新日時',null=False, blank=False, auto_now=True)
    
    def __str__(self):
        return self.brand + "_" + self.model + "_" + self.year
    
class Part(models.Model):
    name = models.CharField('パーツ名', max_length=100, null=True, blank=True)
    brand = models.CharField('ブランド', max_length=100, null=True, blank=True)
    type = models.CharField('タイプ', max_length=100, null=True, blank=True)
    price = models.CharField('値段', max_length=100, null=True, blank=True)
    last_inspection_date = models.CharField('最後の点検日付（交換日）', max_length=100, null=True, blank=True)
    
    def __str__(self):
        return self.name + self.brand
