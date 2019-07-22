"""
  传递多个参数、python内部是通过一个元祖来接受参数和获取参数
  因为元祖不可更改、所以使用元祖
"""


def cooking(*foods):
    print("the parameter is ", type(foods))
    for food in foods:
        print("food you provide is:", food)


"""
    multiple dict parameter
"""


def build_profile(firstname, lastname, **profile):
    user = {}
    print('type of profile is:', type(profile))
    user['firstname'] = firstname
    user['lastname'] = lastname
    user['pfofile'] = profile
    return user


cooking("beef", "tomato", "onion")
cooking("rice")

print(build_profile('rod', 'zhong'))
print(build_profile('rod', 'zhong', money=100.00, house=100, car=20))
