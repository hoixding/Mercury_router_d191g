"""
@source:https://github.com/zixing131/Router
"""

Pwd = "12345678"
def securityEncode(a, b, c):
    d, f, h, m = "", len(a), len(b), len(c)
    e = max(f, h)
    for g in range(0, e):
        l = k = 187
        if (g >= f):
            l = ord(b[g])
        else:
            if (g >= h):
                k = ord(a[g])
            else:
                k = ord(a[g])
                l = ord(b[g])
        d += c[(k ^ l) % m]
    return d


s= securityEncode(Pwd == "" and Pwd or Pwd, "RDpbLfCPsJZ7fiv",
               "yLwVl0zKqws7LgKPRQ84Mdt708T1qQ3Ha7xv3H7NyU84p21BriUWBU4"+
               "3odz3iP4rBL3cD02KZciXTysVXiV8ngg6vL48rPJyAUw0HurW20xqxv9a"+
               "Yb4M9wK1Ae0wlro510qXeU07kV57fQMc8L6aLgMLwygtc0F10a0Dg70TOoo"+
               "uyFhdysuRMO51yY5ZlOZZLEal1h0t9YQW0Ko7oBwmCAHoic4HYbUyVeU3sfQ"+
               "1xtXcPcf1aT303wAQhv66qzW")
print(s)
