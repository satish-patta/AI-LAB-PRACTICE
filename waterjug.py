def isSolvable(a, b, target):
    # Check if the target is reachable by comparing it with the greatest common divisor of a and b
    return target % gcd(a, b) == 0

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def Solution(a, b, target):
    if not isSolvable(a, b, target):
        print("Solution not possible")
        return

    q = []
    visited = set()

    q.append([a, 0])
    visited.add((a, 0))

    while q:
        x, y = q.pop(0)

        if x == target:
            print("Path from initial state to solution state ::")
            print((x, y))
            break

        # Fill Jug2
        if x < a:
            if (a, y) not in visited:
                q.append([a, y])
                visited.add((a, y))

        # Fill Jug1
        if y < b:
            if (x, b) not in visited:
                q.append([x, b])
                visited.add((x, b))

        # Pour water from Jug2 to Jug1
        if x + y >= a:
            if (a, x + y - a) not in visited:
                q.append([a, x + y - a])
                visited.add((a, x + y - a))
        else:
            if (x + y, 0) not in visited:
                q.append([x + y, 0])
                visited.add((x + y, 0))

        # Pour water from Jug1 to Jug2
        if x + y >= b:
            if (x + y - b, b) not in visited:
                q.append([x + y - b, b])
                visited.add((x + y - b, b))
        else:
            if (0, x + y) not in visited:
                q.append([0, x + y])
                visited.add((0, x + y))

# Corrected code starts here
if __name__ == '__main':
    Jug1 = int(input("Enter the capacity of Jug1: "))
    Jug2 = int(input("Enter the capacity of Jug2: "))
    target = int(input("Enter the target: "))
    
    Solution(Jug1, Jug2, target)