import pandas as pd
import numpy as np

from scipy.stats import gamma


chat_id = 417796486 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
  
t = 29
n = len(x)
loc = sum(x)/n

z_1 = st.gamma.ppf((1+p)/2, a = n, scale = 1/n)
z_2 = st.gamma.ppf((1-p)/2, a = n, scale = 1/n)

 return 2*loc/(t**2) - 2/(2*t**2) + 2*z_2/(t**2), \
        2*loc/(t**2) - 2/(2*t**2) + 2*z_1/(t**2)
