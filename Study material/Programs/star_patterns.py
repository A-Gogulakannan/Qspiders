"""
Star Pattern Programs
Various star pattern implementations in Python
"""

def right_triangle_pattern(rows):
    """Print a right triangle star pattern"""
    print("Right Triangle Pattern:")
    for i in range(1, rows + 1):
        print('*' * i)
    print()

def left_triangle_pattern(rows):
    """Print a left triangle star pattern"""
    print("Left Triangle Pattern:")
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        stars = '*' * i
        print(spaces + stars)
    print()

def pyramid_pattern(rows):
    """Print a pyramid star pattern"""
    print("Pyramid Pattern:")
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)
    print()

def inverted_pyramid_pattern(rows):
    """Print an inverted pyramid star pattern"""
    print("Inverted Pyramid Pattern:")
    for i in range(rows, 0, -1):
        spaces = ' ' * (rows - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)
    print()

def diamond_pattern(rows):
    """Print a diamond star pattern"""
    print("Diamond Pattern:")
    # Upper half (including middle)
    for i in range(1, rows + 1):
        spaces = ' ' * (rows - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)
    
    # Lower half
    for i in range(rows - 1, 0, -1):
        spaces = ' ' * (rows - i)
        stars = '*' * (2 * i - 1)
        print(spaces + stars)
    print()

def hollow_square_pattern(size):
    """Print a hollow square star pattern"""
    print("Hollow Square Pattern:")
    for i in range(size):
        if i == 0 or i == size - 1:
            # First and last row - all stars
            print('*' * size)
        else:
            # Middle rows - stars only at edges
            print('*' + ' ' * (size - 2) + '*')
    print()

def main():
    """Main function to demonstrate all patterns"""
    rows = int(input("Enter the number of rows: "))
    
    print(f"\nGenerating star patterns with {rows} rows:\n")
    
    right_triangle_pattern(rows)
    left_triangle_pattern(rows)
    pyramid_pattern(rows)
    inverted_pyramid_pattern(rows)
    diamond_pattern(rows)
    
    if rows >= 3:  # Hollow square needs at least 3 rows to be meaningful
        hollow_square_pattern(rows)

if __name__ == "__main__":
    main()