import sys

def build_path(n, m):
    path = []
    current = 1
    
    while True:
        path.append(current)
        next_pos = (current + m - 1) % n
        if next_pos == 0:
            next_pos = n
        if next_pos == 1:
            break
        current = next_pos
    
    return path

def main():
    if len(sys.argv) != 5:
        print("Использование: python task1.py n1 m1 n2 m2")
        sys.exit(1)
    
    try:
        n1, m1, n2, m2 = map(int, sys.argv[1:5])
    except ValueError:
        print("Все параметры должны быть целыми числами")
        sys.exit(1)
    
    path1 = build_path(n1, m1)
    path2 = build_path(n2, m2)
    
    result = path1 + path2
    
    print(''.join(map(str, result)))

if __name__ == "__main__":
    main()