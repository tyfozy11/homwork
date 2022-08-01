import time



# # def time_work_def(func):
# #     def wrapper(*args, **kwargs):
# #         start = time.clock()
# #         res = func(*args, **kwargs)
# #         stop = time.clock()
# #         resaut_time = stop-start
# #         print(resaut_time)
# #         return res
# #     return wrapper()
#
#
# def time_of_function(function):
#     def wrapped(*args):
#         start_time = time.perf_counter_ns()
#         res = function(*args)
#         print(time.perf_counter_ns() - start_time)
#         return res
#     return wrapped
#
# @time_of_function
# def foo(arg1, arg2):
#     resa = arg1+arg2
#     return resa
#
# print(foo(9, 12))
#
# if difference

a = 29
s = 92
d = a-s
print(abs(d))