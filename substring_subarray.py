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
'''
LOGIC-
1-if i becomes equal to length of array, return
2-till j is less than or equal to len(arr),means for the current value of i, if j is valid, append arr[i:j] to the finalResult.
3-else move the i to i+1 and move our j to the next position of current position of i, means if i is at index 2 , j should be at idex 3, so increase i = i+1 and j =i+2.
'''

def subarrays(arr, finalResult, i=0, j=1):
    if i == len(arr):
        return

    if j <= len(arr):
        finalResult.append(arr[i:j])
        subarrays(arr, finalResult, i, j + 1)
    else:
        subarrays(arr, finalResult, i + 1, i + 2)

arr = [1, 2, 3]
finalResult = []
subarrays(arr, finalResult)
print(finalResult)

'''
what is the logic behind the 2nd recursive call?
We are just simply moving our i to +1 position and also moving our j to +2 position.
Because if i=0 initially
now i = 1 and j =2
So python slice will give you one element in the result as python slice excludes the last j index element.
If array = [1,2,3]
arr[1:2] will give you 2 in result.
'''
