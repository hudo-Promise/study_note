"""

"""


# def verify_blend(gen_1, gen_2, gen_3):
#     len_3 = len(gen_3)
#     for i in range(0, len_3+1):
#         if gen_3[0: i] == gen_1[0: i]:
#             verify_blend(gen_1, gen_2, gen_3)
#         elif gen_3[0: i] == gen_2[0: i]:
#             pass
#         else:
#             return False
#
#
# verify_blend("AGCT", "TCGA", "AGTCTCGA")


# def length_of_str(s):
#     d = {}
#     start = 0
#     ans = 0
#     for i, c in enumerate(s):
#         print(i, c)
#         print(d)
#         if c in d:
#             start = max(start, d[c] + 1)
#         d[c] = i
#         ans = max(ans, i-start+1)
#     return ans
#
#
# n = length_of_str("abcabcbb")
# print(n)

def consumer():
    cnt = yield
    while True:
        if cnt <= 0:
            cnt = yield cnt
        cnt -= 1
        print("consumer get one")

def producer(cnt):
    gen = consumer()
    next(gen)
    gen.send(cnt)
    while True:
        cnt += 1
        print("producter product 1 cnt = ", cnt)
        cnt = gen.send(cnt)

producer(1)