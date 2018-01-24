def flatten(nested):
    
    try:

        for sublist in nested:  
            print 'sublist',sublist
            # import pdb; pdb.set_trace()
            for element in flatten(sublist):

                yield  element

    except TypeError:           
        print '11111'
        yield nested

for num in flatten(a):
    print(num)

#第一种情况当 a=[1,2,3]时，
# 程序走的是：
#     except
#         print '11111'
#         yield nested
# 因为 for循环对于 int类型是不可迭代的。会跑出异常。

#第一种情况当 a=[1,2,3,'c']时，
# 程序走的是：
# for sublist in nested:  
#     print 'sublist',sublist
#     # import pdb; pdb.set_trace()
#     for element in flatten(sublist):
#         yield  element
# 因为 for循环对于 string类型是可迭代的。
# for sublist in nested这句终是对的，则递归终会执行，
# 但python中递归是有一个最大深度的，则报出maximum recursion depth exceeded...
