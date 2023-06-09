#!/opt/homebrew/bin/python3


# problem would be more difficult with arrays and not lists - without insert and pop operations

# consider sizes 0, 1, 2, 3, 4
def merge_sort(a: list[int]) -> None:
    
    if len(a) <= 1:
        return

    if len(a) % 2 == 0:
        split(0, len(a) // 2 - 1, len(a) - 1, a)
    else:
        split(0, len(a) // 2, len(a) - 1, a)

def split(l:int, m:int, r:int, a: list[int]) -> None:

    if (r - l) == 0:
        return
    if (r - l) == 1:
        a[l], a[r] = (a[r], a[l]) if a[l] > a[r] else (a[l], a[r])
        return
    # tuple assignment with ternary operator... unnecessarily complicated?

    split(l, (l + m) // 2, m, a)
    split(m + 1, (m + r + 1) // 2, r, a)
    merge(l, m, m + 1, r, a)

# merge 2 sorted lists inside a list
# r1 > l1, r2 > l2, l1 < l2, r1 < r2 (Need to verify these)
def merge(l1: int, l2: int, r1: int, r2: int, a: list[int]) -> None:
    
    # Using list comprehension and break, may be able to do it faster/cleaner
    while (r1 <= r2):

        if a[r1] >= a[l2]:
        # We're already sorted at this level, return.
        # It's a bit ugly that we're adding this here - ideally we'd add it in the beginning too, for readability. That is even uglier
            return

        l1_temp = l1

        while (l1_temp < l2 & a[r1] > a[l1_temp]):
            l1_temp += 1

        r1_temp_val = a.pop(r1)
        a.insert(l1_temp, r1_temp_val)
        l1 += 1
        r1 += 1



# How to automate the test cases? 
# Can probably just auto-generate lists and throw them at the problem.

a = [4, 3, 2, 1, 5]
b = [1, 2, 3, 4, 5]
c = [1, 2, 3, 4, 5, 2]
d = [2, 1]

merge_sort(a)
merge_sort(b)
merge_sort(c)
merge_sort(d)

print(a)
print(b)
print(c)
print(d)
