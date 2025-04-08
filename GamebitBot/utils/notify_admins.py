

def info_pk_user(choosing_place: str) -> str:
    """Получение строки с выбором места, и отправка уточняющей справки"""
    if choosing_place.startswith('st'):
        return f'зал стандарт, ПК № {choosing_place[-1]}'
    elif choosing_place.startswith('vip'):
        return f'зал VIP, ПК № {choosing_place[-1]}'
    else:
        return 'PS-5'





