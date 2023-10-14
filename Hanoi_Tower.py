def t_hanoi(n , starting_tower, auxiliary_tower, destination_tower):
    """solving the Tower of Hanoi Question with recursion function"""
    if n == 1:
        print(starting_tower, '------>', destination_tower)
        return
    t_hanoi(n-1, starting_tower, auxiliary_tower, destination_tower)
    print(starting_tower, '------>', destination_tower)
    t_hanoi(n-1, auxiliary_tower, destination_tower, starting_tower)


n = int(input('pleas enter the number of disk :'))
t_hanoi(n, starting_tower='a', auxiliary_tower='b', destination_tower='c')
