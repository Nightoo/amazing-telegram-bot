nums1 = [[2,4],[3,6],[5,5]]
nums2 = [[1,3],[4,3]]

ids1 = []
ids2 = []
for el in nums1:
    ids1.append(el[0])
for el in nums2:
    ids2.append(el[0])
print(ids1, ids2)
ans = [[i, 0, 0] for i in range(max(ids1) + max(ids2))]
print(ans)
for el in nums1:
    ans[el[0]][1] += el[1]
    ans[el[0]][2] = 1
    print(el[0], ans)
for el in nums2:
    ans[el[0]][1] += el[1]
    ans[el[0]][2] = 1
ans1 = []
for el in ans:
    if el[2] == 1:
        ans1.append([el[0], el[1]])
print('------', ans1)