#!/usr/bin/python3
def best_score(a_dictionary):
    # Əgər dictionary boşdursa və ya None-dursa
    if not a_dictionary:
        return None
    # Ən böyük dəyəri tapmaq üçün
    max_value = max(a_dictionary.values())
    # Ən böyük dəyərə uyğun gələn açarı tapmaq üçün
    for key, value in a_dictionary.items():
        if value == max_value:
            return key
