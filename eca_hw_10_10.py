# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
#%%
import pylab as py


#%%

def sequential(f, x_init, x_interval, epsilon, x_final):
    # result 의 초기값
    # Initial value for sqrt_10
    result = 'Not Found'

    # 일련의 x_i 값을 미리 준비한다
    # Prepare a series of x_i values in advance
    x_array = py.arange(x_init, x_final+x_interval*0.5, x_interval)

    # 몇번 반복했는지 측정해 보자
    # Let's count the number of iterations
    counter = 0

    # x_i 에 관한 반복문
    # x_i loop
    for x_i in x_array:
        # Evaluate the function
        y_i = f(x_i)
        
        counter += 1
        # Check if absolute value is smaller than epsilon
        if abs(y_i) < epsilon:
            result = x_i
            # found
            break

    # 반복 횟수
    # Number of iterations
    print('counter =', counter)

    return result


#%% [markdown]
# 도전 과제 1: 다음 매개 변수값을 하나씩 바꾸어 보고 그 영향에 대한 의견을 적으시오.
# Try this 1: Change one parameter value at a time and write down your opinion on its influence.
#
# epsilon
#
#
# x_init
#
#
# x_interval
#
#


#%% [markdown]
# 도전 과제 2: $sin^2(\theta)=0.5$ 인 $\theta$(도)를 구해 보시오.
# Try this 2: Find $\theta$(degree) satisfying $sin^2(\theta)=0.5$.
# 
# 
#%%


#%% [markdown]
# 도전 과제 3: 관심 있는 $f(x)=0$ 문제를 정하여 근을 구해 보시오.<br>Try this 3: Find a root of a $f(x)=0$ problem of your choice.
# 
# 
#%%

