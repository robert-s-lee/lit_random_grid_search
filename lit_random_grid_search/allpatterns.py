from jsonargparse import CLI
from numpy.random import uniform
from datetime import datetime
import re
import itertools
import random

def midstr(text:str,start:int,end:int,repl:str) -> str:
  """replace text[start:end] with repl
  """
  return(text[:start] + repl + text[end:])

def replace_variables(pattern:str, text:str, product:list, length:int):
  """ replace from the end of string to the beginning of the string for each product of values
  """
  gridsearch=[]
  for p in product:
    # replace variables
    t = text
    i = length-1
    for m in reversed(list(re.finditer(pattern,text))):  
      span_start, span_end = m.span()
      t = midstr(t,span_start,span_end,p[i])
      i = i - 1
    gridsearch.append(t)
  return(gridsearch)

def assign_values(keys:list) -> list:
  """assign value to each elememt eg: ["range(1,2,1)","a"] -> [[1,2],"a"]
  """
  ret=[]
  for k in keys:
    try:
      # if expression, then save the result of expression
      ret.append([str(v) for v in eval(k)])
    except:
      # otherwise, constant
      ret.append([k])
  return(ret)    

def find_text_inside_delim(text:str, open_delim="{{", close_delim="}}") -> list:
  """return text withing the delim """
  # use non greedy regex match with the magic "?""  
  pattern = re.compile('%s(.*?)%s' % (open_delim,close_delim))
  # extract variables
  variables = pattern.findall(text)
  # assign value to variables
  values = assign_values(variables)
  # product product of values
  product = list(itertools.product(*values))
  # replace variables with values
  gridsearch = replace_variables(pattern, text, product, len(variables))
  return(gridsearch)

if __name__ == "__main__":
  """
python allpatterns.py midstr "hi there" 1 2 "new"
python allpatterns.py find_text_inside_delim "--abc {{abc}}"
python allpatterns.py find_text_inside_delim "--abc {{[1,2,3]}} def={{uniform(1,10,3)}}"
python allpatterns.py find_text_inside_delim "--abc {{[1,2,3]}} def={{range(1,3,1)}}"
python allpatterns.py find_text_inside_delim "--abc {{['abc','b','c']}} def={{range(1,3,1)}}"
  """
  print(CLI())