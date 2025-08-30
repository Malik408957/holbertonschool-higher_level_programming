#!/usr/bin/python3
if __name__ == "__main__":
    import sys

    # Arqumentlərin cəmini hesablayırıq
    total = 0
    for i in range(1, len(sys.argv)):
        total += int(sys.argv[i])
    
    print(total)
