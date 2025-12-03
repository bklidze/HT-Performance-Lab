import sys
import math

def parse_ellipse_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    center_line = lines[0].strip()
    radius_line = lines[1].strip()
    
    cx, cy = map(float, center_line.split())
    rx, ry = map(float, radius_line.split())
    
    return cx, cy, rx, ry

def parse_points_file(filename):
    with open(filename, 'r') as f:
        lines = f.readlines()
    
    points = []
    for line in lines:
        if line.strip():
            x, y = map(float, line.split())
            points.append((x, y))
    
    return points

def point_position(cx, cy, rx, ry, px, py):
    value = ((px - cx) / rx) ** 2 + ((py - cy) / ry) ** 2
    
    epsilon = 1e-10
    
    if abs(value - 1.0) < epsilon:
        return 0
    elif value < 1.0:
        return 1
    else:
        return 2

def main():
    if len(sys.argv) != 3:
        print("Использование: python task2.py <файл_эллипса> <файл_точек>")
        sys.exit(1)
    
    ellipse_file = sys.argv[1]
    points_file = sys.argv[2]
    
    try:
        cx, cy, rx, ry = parse_ellipse_file(ellipse_file)
        points = parse_points_file(points_file)
        
        for px, py in points:
            position = point_position(cx, cy, rx, ry, px, py)
            print(position)
            
    except FileNotFoundError as e:
        print(f"Ошибка: файл не найден - {e.filename}")
        sys.exit(1)
    except ValueError as e:
        print(f"Ошибка в формате данных файла")
        sys.exit(1)
    except Exception as e:
        print(f"Ошибка: {e}")
        sys.exit(1)

if __name__ == "__main__":
    main()