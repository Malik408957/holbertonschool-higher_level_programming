#!/usr/bin/python3
def safe_print_division(a, b):
    """
    İki tam ədədi təhlükəsiz şəkildə bölür və nəticəni çap edir.
    Args:
        a (int): Bölünən ədəd
        b (int): Bölən ədəd
    Returns:
        float or None: Bölmə nəticəsi və ya sıfıra bölmə cəhdi olduqda None
    """
    result = None
    try:
        result = a / b
    except ZeroDivisionError:
        # Sıfıra bölmə xətası baş verərsə, result None olaraq qalır
        pass
    finally:
        # Nəticə həmişə finally blokunda çap edilir
        print("Inside result: {}".format(result))
        return result
