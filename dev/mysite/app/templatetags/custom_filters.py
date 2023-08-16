from django import template
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta

register = template.Library()

@register.filter(name='maintenance_warning')
def maintenance_warning(last_inspection_date, part_name):
    if not last_inspection_date:
        return False

    today = datetime.now().date()

    if part_name == 'FLAME':
        maintenance_period = timedelta(days=10)  # フレームのメンテナンスサイクルは1週間
    elif part_name == 'FRONTBRAKE':
        maintenance_period = relativedelta(months=6)  # フロントブレーキのメンテナンスサイクルは6か月
    elif part_name == 'REARBRAKE':
        maintenance_period = relativedelta(months=6)  # リアブレーキのメンテナンスサイクルは6か月
    elif part_name == 'CHAIN':
        maintenance_period = relativedelta(months=1)  # チェーンのメンテナンスサイクルは1か月
    elif part_name == 'FRONTTIRE':
        maintenance_period = timedelta(weeks=1)  # フロントタイヤのメンテナンスサイクルは1週間
    elif part_name == 'REARTIRE':
        maintenance_period = timedelta(weeks=1)  # リアタイヤのメンテナンスサイクルは1週間
    elif part_name == 'STEM':
        maintenance_period = relativedelta(years=1)  # ステムのメンテナンスサイクルは1年間
    elif part_name == 'SADDLE':
        maintenance_period = relativedelta(years=5)  # サドルのメンテナンスサイクルは5年間
    elif part_name == 'SEATPOST':
        maintenance_period = relativedelta(years=1)  # シートポストのメンテナンスサイクルは1年間
    elif part_name == 'SEATCLAMP':
        maintenance_period = timedelta(weeks=1)  # シートクランプのメンテナンスサイクルは1週間
    elif part_name == 'PEDAL':
        maintenance_period = relativedelta(months=3)  # ペダルのメンテナンスサイクルは3か月
    elif part_name == 'FLONTLIGHT':
        maintenance_period = relativedelta(months=1)  # フロントライトのメンテナンスサイクルは1か月
    elif part_name == 'TAILLIGHT':
        maintenance_period = relativedelta(months=1)  # テールライトのメンテナンスサイクルは1か月
    else:
        maintenance_period = None

    if maintenance_period is None:
        return False

    return last_inspection_date + maintenance_period <= today

@register.filter(name='get_partname')
def get_partname(partname_dict, partname):
    return partname_dict.get(partname, partname)  # 辞書から取得できない場合はそのまま表示