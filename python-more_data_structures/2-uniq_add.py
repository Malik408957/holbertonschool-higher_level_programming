#!/usr/bin/python3
def uniq_add(my_list=[]):
    # Unikal ədədləri saxlamaq üçün çoxluq
    seen = set()
    total = 0
    # Listdəki hər bir elementi gəzirik
    for num in my_list:
        # Əgər bu ədədi əvvəl görməmişiksə
        if num not in seen:
            total += num      # Cəmə əlavə et
            seen.add(num)     # "Görülmüş" olaraq qeyd et
    return total
