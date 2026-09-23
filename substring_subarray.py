def subarrays(arr):
    result = []

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            result.append(arr[i:j+1])

    return result


arr = [1, 2, 3]

print(subarrays(arr))

# Other solution

def subarrays(arr):
    result = []

    for i in range(len(arr)):
        sub = []

        for j in range(i, len(arr)):
            sub.append(arr[j])
            result.append(sub.copy()) #this is very important, without using copy() we will get wrong answer

    return result

'''
why .copy()?

sub = []
sub.append(1)
result.append(sub)
sub.append(2)
result.append(sub)

You might expect:
result = [[1], [1, 2]]

But you actually get:
result = [[1, 2], [1, 2]]

How?
Because Python stores the reference to the list, not a frozen snapshot of it.

sub = []
sub.append(1)
result.append(sub)

At this point:
sub       -> [1]
result[0] -> [1]
Both sub and result[0] point to the same list.

Now:
sub.append(2)
The same list becomes:
sub       -> [1, 2]
result[0] -> [1, 2]
So result[0] is now also [1, 2].

Then:
result.append(sub)
Now both entries point to the same list:
result[0] ──┐
             ↓
           [1, 2]
             ↑
result[1] ──┘

Therefore:
print(result)
gives:
[[1, 2], [1, 2]] , which is wrong

copy() fixes it
result.append(sub.copy())
means:
"Take whatever sub looks like right now, and create a separate list."
So:
sub       → [1, 2]
result[0] → [1]       (old copy)
result[1] → [1, 2]    (new copy)
That's why we use copy() here.
'''


# Recursive code

def subarrays(arr, i=0, j=1):
    if i == len(arr):
        return

    if j <= len(arr):
        print(arr[i:j])
        subarrays(arr, i, j + 1)
    else:
        subarrays(arr, i + 1, i + 2)


arr = [1, 2, 3]

subarrays(arr)
