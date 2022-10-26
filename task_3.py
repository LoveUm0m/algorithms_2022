 1 способ
list_values = sorted(list(companies.values()), reverse=True)[:3]                     # O(n)
for el in list_values:                                                               # O(1)
    for k, v in companies.items():                                                   # O(n)
        if v == el:
            print(k, ':', v)                                                         # O(1)


# O(n)  + O(1) + O(n)  + O(1) = O(n)

# 2 способ
sorted_companies = sorted(companies, key=companies.get, reverse=True)[:3]    # O(n*log n)
for i in sorted_companies:                                                   # O(1)
    print(i, ':', companies.get(i))                                          # O(1)

# O(n*log n) + O(1) + O(1) = O (n *log n)