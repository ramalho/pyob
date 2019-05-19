from random_queens_and_guard import solve

TRIES = 500

for size in range(8, 21):
    count = 0
    for _ in range(TRIES):
        try:
            solve(size)
        except RecursionError:
            pass
        else:
            count += 1
    
    success = count / TRIES * 100
    print(f'{size:2d}: {success:5.1f}%')
