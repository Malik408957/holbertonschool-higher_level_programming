#!/usr/bin/python3
# Moduldan funksiyanı import et
from add_0 import add

# Əgər bu fayl birbaşa işə salınırsa (import edilmirsə)
if __name__ == "__main__":
    # Dəyişənlərə dəyərlər mənimsət
    a = 1
    b = 2
    # Nəticəni formatla və çap et
    print("{} + {} = {}".format(a, b, add(a, b)))
