i = 1
s = "s"
u = u"あいうえお"
b = True
l = [10, 20]
d = {"name": "apple"}


def func(p1, p2, p3, p4, p5, p6):
    p5.append(30)
    p6["name"] = "kiwi"


func(i, s, u, b, l, d)

print(i, "#1")
print(s, "#2")
print(u, "#3")
print(b, "#4")
print(l, "#5")
print(d, "#6")


def something_func(user_result, permission_result):

    if user_result == STATUS_SUCCESS:
        if permission_result == STATUS_SUCCESS:
            reply.write_errors("error reading permissions")
            reply.done()
            return

        reply.writ_errors("")
    else:
        reply.writ_errors(user_result)

    reply.done()


def something_func(user_result, permission_result):

    if user_result != STATUS_SUCCESS:
        reply.write_errors(user_result)
        reply.done()
        return

    if permission_result != STATUS_SUCCESS:
        reply.write_errors("error reading permissions")
        reply.done()
        return

    reply.write_errors("")
    reply.done()
