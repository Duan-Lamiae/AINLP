# def need(n):
#     res=" "
#     for i in range(1,int(n)+1):
#         for j in range(1,int(n)+1):
#             res+=f"{i},{j}"
#     return res
# print(need(4))


#普通递归
# def recur(n):
#     #终止条件
#     if n==1:
#         return 1
#     #递：递归调用
#     res=recur(n-1)
#     #归：返回结果
#     return n+res
# print(recur(8))

#尾递归
# def tail_recur(n,res):
#     '''尾递归'''
#     #终止条件
#     if n==0:
#         #res类似与求和器，初始值为0
#         return res
#     return tail_recur(n-1,res+n)
# print(tail_recur(9,0))

# def fib(n):
#     '''斐波那契数列：递归'''
#     #终止条件：f(1)=0,f(2)=1
#     if n==1 or n==2:
#         return n-1
#     #递归调用 f(n)=f(n-1)+f(n-2)
#     res=fib(n-1)+fib(n-2)
#     #返回结果 f(n)
#     return res
# print(fib(9))
#
# def for_loop_recur(n):
#     '''使用迭代模拟递归'''
    #使用一个显示的栈来模拟系统调用栈
    # stack=[]
    # res=0
    #递：递归调用
#     for i in range(n,0,-1):
#         #通过"入栈操作"模拟”递“
#         stack.append(i)
#     #归：返回结果
#     while stack:
#         #通过”入栈操作“模拟”归“
#         res+=stack.pop()
#     #res=1+2+3+...+n
#     return res
# print(for_loop_recur(5))
#虽然递归和迭代可以相互转化，但是不一定值得这么做
#两点原因：
#①：转化后的代码可能更加难以理解，可读性更差
#②：对于某些复杂问题，模拟系统调用栈的行为可能非常困难
#选择迭代还是递归取决于特定问题的性质

#时间复杂度
# def algo(n):
#     a=1       #+0
#     a=a+n     #+0
#     for i in range(5*n+1):   #+n
#         print(1)
#     for i in range(2*n):     #+n*n
#         for j in range(n+1):
#             print(0)
# algo(1)
#时间复杂度由T(n)中最高阶的项决定
#常见类型
#o(1)<o(logn)<o(n)<o(blogn)<o(n^2)<o(2^n)<o(n!)
#常数阶< 对数阶 <线性阶<线性对数阶<平方阶<指数阶 <阶乘阶

#常数阶o(1)
#尽管操作数量size数值很大，但由于与其输入的数据n大小无关，因此时间复杂度为o(1)
# def constant(n):
#     count=0
#     size=100000
#     for i in range(size):
#         count+=1
#     return count
# print(constant(1))

#线性阶o(n)
#线性阶的操作数量相对于输入数据大小n以线性级别增长
# def quadratic(n):
#     '''平方阶'''
#     count=0
#     #循环次数与数组长度成平方关系
#     for i in range(int(n)):
#         for j in range(int(n)):
#             count+=1
#
#     return count
# print(quadratic(9))

#冒泡排序例子
# def bubble_sort(num):
#     '''平方阶(冒泡排序)'''
#     count=0
#     for i in range(len(num)-1,0,-1):
#         for j in range(i):
#             if num[j]>num[j+1]:
#                 num[j],num[j+1]=num[j+1],num[j]
#     return count
# lst=[1,6,7,2,3,0,9]
# bubble_sort(lst)
# print(lst)

#指数阶o(2^n)
# def exponential(n):
#     count=0
#     base=1
#     for i in range(n):
#         for j in range(base):
#             count+=1
#         base*=2
#     return count
# print(exponential(6))
#
#指数阶o(2^(n-1))
# def exp_recur(n):
#     if n==1:
#         return 1
#     return exp_recur(n-1)+exp_recur(n-1)+1
# print(exp_recur(6))

#对数阶o(log2^n)
# def logarithmic(n):
#     count=0
#     while n>1:
#         n=n/2
#         count+=1
#     return count
# print(logarithmic(8))

# def log_recur(n):
#     if n<=1:
#         return 0
#     return log_recur(n/2)+1
# print(log_recur(8))

#线性对数阶o(nlogn)
# def liner(n):
#     if n<=1:
#         return 1
#     count=liner(n//2)+liner(n//2)
#     for i in range(n):
#         count+=1
#     return count
# print(liner(6))
# import random
# def random_numbers(n):
#     nums=[i for i in range(1,n+1)]
#     random.shuffle(nums)
#     return nums
# def find_one(nums):
#     for i in range(len(nums)):
#         if nums[i]==1:
#             return i
#     return -1
#
# print(random_numbers(6))
# nus=[11,8,56,32,98]
# print(find_one(nus))

