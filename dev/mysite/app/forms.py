from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django import forms
from .models import Bicycle


class SignupForm(UserCreationForm):
    def __init__(self, *args, **kwargs):
        super(SignupForm, self).__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'p-1 border border-gray-300 rounded-sm ml-2'})
        self.fields['password1'].widget.attrs.update({'class': 'p-1 border border-gray-300 rounded-sm ml-2'})
        self.fields['password2'].widget.attrs.update({'class': 'p-1 border border-gray-300 rounded-sm ml-2'})

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2']

class LoginForm(AuthenticationForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['username'].widget.attrs.update({'class': 'p-1 ml-2 border border-gray-300 rounded-sm'})
        self.fields['password'].widget.attrs.update({'class': 'p-1 ml-2 border border-gray-300 rounded-sm'})

class BicycleBrandForm(forms.Form):
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
    brand_choicel = forms.ChoiceField(choices= Brand_Choices)

class BicycleForm(forms.ModelForm):
    class Meta:
        model = Bicycle
        fields = ['image', 'brand', 'model', 'year']
