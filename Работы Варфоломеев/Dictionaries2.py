def enter_comps():
    emp_set = {}
    print("введите список участников")
    s = input()
    while s != '':
        _s = s.split()
        emp_set[_s[0] + ' ' + _s[1]] = int(_s[2])
        s = input()
    return emp_set


count = int(input())
_list_comps = [0]*count
for i in range(count):
    _list_comps[i] = enter_comps()

for ol in _list_comps:
    print(ol)

