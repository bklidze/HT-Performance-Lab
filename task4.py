import sys

def min_moves_to_equal(nums, max_moves=20):
    nums.sort()
    median = nums[len(nums) // 2]
    
    total_moves = sum(abs(num - median) for num in nums)
    
    if total_moves <= max_moves:
        return total_moves
    else:
        return None

def main():
    if len(sys.argv) != 2:
        print("Использование: python task4.py <файл>")
        sys.exit(1)
    
    filename = sys.argv[1]
    
    try:
        with open(filename, 'r') as f:
            nums = [int(line.strip()) for line in f if line.strip()]
    except FileNotFoundError:
        print(f"Файл {filename} не найден")
        sys.exit(1)
    except ValueError:
        print("Файл содержит некорректные данные")
        sys.exit(1)
    
    if not nums:
        print("Файл пуст")
        sys.exit(1)
    
    result = min_moves_to_equal(nums)
    
    if result is not None:
        print(result)
    else:
        print("20 ходов недостаточно для приведения всех элементов массива к одному числу")

if __name__ == "__main__":
    main()