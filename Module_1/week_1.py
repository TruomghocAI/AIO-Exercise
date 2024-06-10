import math
import random

def exercise_1():
  
  def precision(tp, fp):
      if tp + fp == 0:
          return 0.0
      return tp / (tp + fp)

  def recall(tp, fn):
      if tp + fn == 0:
          return 0.0
      return tp / (tp + fn)

  def f1_score(precision, recall):
      if precision + recall == 0:
          return 0.0
      return 2 * (precision * recall) / (precision + recall)
    
  def question_1(tp, fp, fn):
    if not isinstance(tp, int) or not isinstance(fp, int) or not isinstance(fn, int):
      if not isinstance(tp, int):
        print('tp must be int')
      if not isinstance(fp, int):
        print('fp must be int')
      if not isinstance(fn, int):
        print('fn must be int')
      return
    if tp <= 0 or fp <= 0 or fn <= 0:
      print('tp and fp and fn must be greater than zero')
      return
    
    a = precision(tp, fp)
    b = recall(tp, fn)
    c = f1_score(a, b)
    print(f'Precision: {a}')
    print(f'Recall: {b}')
    print(f'F1-score: {c}')
    
  question_1(tp=2, fp=3, fn=4)
  question_1(tp='a', fp=3, fn=4)
  question_1(tp=-2, fp=3, fn=4)

def exercise_2():
  def is_number(n):
    try:
        float(n)
        return True
    except ValueError:
        return False
  
  def sigmoid(x):
    sigmoid = 1/(1 + math.exp(-x))
    return sigmoid
  
  def relu(x):
    if x > 0:
      return x
    else:
      return 0
    
  def elu(alpha,x):
    if x > 0:
      return x
    else:
      return round(alpha*(math.exp(x)-1),2)
    
  def question_2(x,alpha):
    if not is_number(x):
      print('x must be a number')
      return    
    
    string_function =['sigmoid','relu','elu']
    print("Nhập activation function:\n 1:Sigmoid\n 2:RELU\n 3:ELU")
    op = input().lower()

    if op not in string_function:
      print(f'{op} is not supported')
    else:
      x = float(x)
      if op == 'sigmoid':
        print(f'{op}: f({x}) = {sigmoid(x)}')
      elif op == 'relu':
        print(f'{op}: f({x}) = {relu(x)}')
      elif op == 'elu':
        print(f'{op}: f({x}) = {elu(alpha,x)}')

  question_2(1 , 0.01)
  question_2(-5 , 0.01)
  question_2(0 , 0.01)
  
def exercise_3():
  def list_data(num_sample,data_pre,data_target):
    for i in range(num_sample):
      pred = random.uniform(0,10)
      data_pre.append(pred)

      target = random.uniform(0,10)
      data_target.append(target)

  def MAE(num_sample,data_pre,data_target):
    loss = 0
    for i in range(num_sample):
      loss += abs(data_target[i] - data_pre[i])
      print(f'loss name: MAE , sample: {i}, pred: {data_pre[i]}, target: {data_target[i]}, loss: {loss}')

    print(f'final MAE: {loss/num_sample}')

  def MSE(num_sample,data_pre,data_target):
    loss = 0
    for i in range(num_sample):
      loss += (data_target[i] - data_pre[i])**2
      print(f'loss name: MSE , sample: {i}, pred: {data_pre[i]}, target: {data_target[i]}, loss: {loss}')

    print(f'final MSE: {loss/num_sample}')

  def RMSE(num_sample,data_pre,data_target):
    loss = 0
    for i in range(num_sample):
      loss += (data_target[i] - data_pre[i])**2
      print(f'loss name: RMSE , sample: {i}, pred: {data_pre[i]}, target: {data_target[i]}, loss: {loss}')
    loss = math.sqrt(loss)
    print(f'final RMSE: {math.sqrt(loss/num_sample)}')

  def question_3():
    data_pre = []
    data_target = []
    num_sample = 5
    if type(num_sample) != int:
      print("number of samples must be an integer number")
      return 
    list_data(num_sample,data_pre,data_target)
      
    loss_name = ['MAE','MSE','RMSE']
    print("Nhập Loss function:\n 1:MAE\n 2:MSE\n 3:RMSE")
    loss_name_function = input().upper()

    if loss_name_function not in loss_name:
      print(f'{loss_name_function} is not supported')
    else:
      if loss_name_function == 'MAE':
        MAE(num_sample,data_pre,data_target)
      elif loss_name_function == 'MSE':
        MSE(num_sample,data_pre,data_target)
      elif loss_name_function == 'RMSE':
        RMSE(num_sample,data_pre,data_target)
        
  question_3()
  
def exercise_4():
  def sin(x,n):
    sinx = 0
    for i in range(n):
      a = ((-1) ** i) * (x ** (2 * i + 1))
      b = math.factorial(2 * i + 1)
      sinx +=  (a / b)
      return sinx

  def cos(x,n):
    cosx = 0
    for i in range(n):
      a = ((-1) ** i) * x**(2*i)
      b = math.factorial(2 * i)
      cosx += a/b
      return cosx

  def sinh(x,n):
    sinhx = 0
    for i in range(n):
      a = x**(2*i +1)
      b = math.factorial(2*i +1)
      sinhx += a/b
    return sinhx

  def cosh(x,n):
    coshx = 0
    for i in range(n):
      a = x**(2*i)
      b = math.factorial(2*i)
      coshx += a/b
    return coshx

  def question_4():
    print(sin(3.14,10))
    print(cos(3.14,10))
    print(sinh(3.14,10))
    print(cosh(3.14,10))
  question_4()

def exercise_5():
  def md_nre_single_sample(y,y_hat,n,p):
    y_root = y ** (1/n)
    y_hat_root = y_hat **(1/n)
    dif = y_root - y_hat_root
    loss = dif**p
    return loss
  
  def question_5():
    print(md_nre_single_sample(100,99.5,2,1))
    print(md_nre_single_sample(50,49.5,2,1))
    print(md_nre_single_sample(20,19.5,2,1))
    print(md_nre_single_sample(0.6,0.1,2,1))
  
  question_5()

if __name__ == "__main__":
  
    exercise = int(input("Select the exercise you want to test:\n 1:exercise_1\n 2:exercise_2\n 3:exercise_3\n 4:exercise_4\n 5:exercise_5\n"))
    if exercise == 1:
      exercise_1()
    elif exercise == 2:
      exercise_2()
    elif exercise == 3:
      exercise_3()
    elif exercise == 4:
      exercise_4()
    elif exercise == 5:
      exercise_5()