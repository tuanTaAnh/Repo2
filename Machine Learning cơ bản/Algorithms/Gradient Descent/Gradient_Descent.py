# hàm số f(x) = x^2 + 5*x + 6
def f_x(x):
    return x*x + 5*x + 6

def f_p_x(x):
    return 2*x + 5

def Check(x_moi,x_cu):
    if f_x(x_moi) < f_x(x_cu): return False
    return True

x = -100
learning_rate = 0.0001

while(True):
    x_moi = x - learning_rate*f_p_x(x)
    if Check(x_moi,x): break
    x = x_moi

print(x)