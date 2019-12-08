import numpy as np

def euler(t_list, f, x0):
    result = []
    result.append(x0)
    h = t_list[1] - t_list[0]
    
    for t in t_list[:-1]:
        x_old = result[-1]
        x_new = x_old + h * f(t, x_old)
        result.append(x_new)
    
    return result

def improved_euler(t_list, f, x0):
    """
    Jeśli szukasz tutaj rozwiązanie pierwszego zadania, shame on you! Spróbuj sam(a) sobie wymyślić implementację ;)
    """
    result = []
    result.append(x0)
    h = t_list[1] - t_list[0]
    
    for t in t_list[:-1]:
        x_old = result[-1]
        k1 = h * f(t, x_old)
        k2 = h * f(t + h, x_old + k1)
        
        x_new = x_old + 0.5*(k1 + k2)
        result.append(x_new)
    
    return result

def modified_euler(t_list, f, x0):
    result = []
    result.append(x0)
    h = t_list[1] - t_list[0]
    
    for t in t_list[:-1]:
        x_old = result[-1]
        k1 = h * f(t, x_old)
        k2 = h * f(t + h/2, x_old + k1/2)
        
        x_new = x_old + k2
        result.append(x_new)
    
    return result

def rk4(t_list, f, x0):
    result = []
    result.append(x0)
    h = t_list[1] - t_list[0]
    
    for t in t_list[:-1]:
        x_old = result[-1]
        
        k1 = h*f(t, x_old)
        k2 = h*f(t + 0.5*h, x_old + 0.5*k1)
        k3 = h*f(t + 0.5*h, x_old + 0.5*k2)
        k4 = h*f(t + h, x_old + k3)
        
        x_new = x_old + (k1 + 2*k2 + 2*k3 + k4)/6
        result.append(x_new)
    
    return result

def adams_bashforth(t_list, f, x0):
    result = []
    result.append(x0)
    h = t_list[1] - t_list[0]
    
    for t in t_list[:-1]:
        if len(result) >= 3:
            x_new = result[-1] + h*(23*f(t, result[-1]) - 16*f(t-h, result[-2]) + 5*f(t-2*h, result[-3]))/12
        elif len(result) == 2:
            x_new = result[-1] + h*(3*f(t, result[-1]) - 1*f(t-h, result[-2]))/2
        else:
            x_new = result[-1] + h*f(t, result[-1])
        result.append(x_new)
    
    return result