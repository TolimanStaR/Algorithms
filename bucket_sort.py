def to_normal_string(x):
    point_pos = 0
    for i in range(len(str(x))):
        if str(x)[i] == '.':
            point_pos = i

    if len(str(x)[point_pos + 1:]) == 1:
        return (str(x) + '0')

    else:
        return (x)


n = int(input())
array = list(map(float, input().split()))

print('Initial array:')
for i in range(n):
    print(to_normal_string(array[i]), end=' ')
if n == 1:
    exit(0)
print()
print()


def insertion_sort(ar):
    for i in range(1, len(ar)):
        k = i
        while ar[k] < ar[k - 1] and k > 0:
            ar[k], ar[k - 1] = ar[k - 1], ar[k]
            k -= 1

    return ar


def bucket_sort(array):
    bucket = [[] for i in range(n * 2)]
    to_print = []

    min_elem = min(array)
    max_elem = max(array)

    for i in range(n):
        if max_elem - min_elem > 0:
            index = int((array[i] - min_elem) * n * 2 / (max_elem - min_elem))
        else:
            index = int(array[i] - min_elem)
        if index == n * 2:
            bucket[n * 2 - 1].append(array[i])
        else:
            bucket[index].append(array[i])

    for i in range(n * 2):
        if len(bucket[i]) > 0:

            print('Bucket:')
            for j in range(len(bucket[i])):
                print(to_normal_string(bucket[i][j]), end=' ')
            print()

            bucket[i] = insertion_sort(bucket[i])

            print('Sorted bucket:')
            for j in range(len(bucket[i])):
                print(to_normal_string(bucket[i][j]), end=' ')
            print()
            print()
            to_print += bucket[i]

    print('Final array:')
    for i in range(n):
        print(to_normal_string(to_print[i]), end=' ')


if __name__ == '__main__':
    bucket_sort(array)
