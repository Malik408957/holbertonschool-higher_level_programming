#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    """Siyahıdan təhlükəsiz şəkildə elementləri çap edir."""
    count = 0
    try:
        for i in range(x):
            print(my_list[i], end="")
            count += 1
    except IndexError:
        pass
    finally:
        print()
    return count
