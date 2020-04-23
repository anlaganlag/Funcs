def su(r):
    s,n=0,0
    def h(r):
        nonlocal n,s
        if not r:
            return 0
        n = (n<<1)+r.val
        if not r.left and not r.right:
            s += n
        h(r.left)
        h(r.right)
        n = (n-r.val)>>1
#相當於彈出回退..
        return s
    return h(r)

