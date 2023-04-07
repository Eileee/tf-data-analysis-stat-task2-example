import pandas as pd
import numpy as np

from scipy.stats import norm


chat_id = 417796486 # Ваш chat ID, не меняйте название переменной

def solution(p: float, x: np.array) -> tuple:
  
t = 29
loc = sum(x)/len(x)

z_1 = st.gamma.ppf((1+p)/2, a = len(x), scale = 1/len(x))
z_2 = st.gamma.ppf((1-p)/2, a = len(x), scale = 1/len(x))

 return 2*loc/(t**2) - 2/(2*t**2) + 2*z_2/(t**2), \
        2*loc/(t**2) - 2/(2*t**2) + 2*z_1/(t**2)
