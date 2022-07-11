def create_data(n, l, ret_list):
    for j in [1, 2]:
        ll = l + [j]
        if sum(ll) == n:
            ret_list.append(ll)
            return ll
        elif len(ll) > n * 2 or sum(ll) > n:
            break
        else:
            create_data(n, ll, ret_list)


def func(n: int) -> list:
    ret_list = list()
    for i in [1, 2]:
        create_data(n, [i,], ret_list)
    ok_data_list = list()
    for item in ret_list:
        tmp_str = "".join(str(i) for i in item)
        if "22" not in tmp_str:
            ok_data_list.append(tmp_str)
    if n in (1, 2):
        ok_data_list.append(str(n))

    return ok_data_list


bean = input("请输入豆子数量>>: ")
try:
    n = int(bean)
    print("%s 颗豆子的吃法有 %s种" % (n, len(func(n))))
except Exception as e:
    print(f"Input Err! Need Int!!! {str(e)}")
