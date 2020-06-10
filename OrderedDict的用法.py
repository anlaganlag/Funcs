from collections import OrderedDict
from typing import List
s="aaaabbbbcccc"
def foo(s: str) -> str:
    ss = sorted(s)
    cnt = OrderedDict()
    for ch in ss:
        if ch not in cnt:
            cnt[ch] = 1
        else:
            cnt[ch] += 1
    return cnt
    res = ""
    while len(res) < len(ss):
        for k, v in cnt.items():
            if v > 0:
                res += k
                cnt[k] -= 1

        for k, v in reversed(cnt.items()):
            if v > 0:
                res += k
                cnt[k] -= 1
    return res
foo(s)

