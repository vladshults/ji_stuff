s = "abc bca abb bba bba bba bba abb abc cde abc bca abb"

l = s.split(" ")
d = {}

for idx in range(1, len(l)-1):
    f = " ".join((l[idx - 1], l[idx], l[idx + 1]))
    if f not in d:
        d[f] = 1
    else:
        d[f] += 1

sorted_triplets = sorted(d.items(), key=lambda item: item[1])

print(sorted_triplets[-1][0])

