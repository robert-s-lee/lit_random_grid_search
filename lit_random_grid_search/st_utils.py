import copy
import lit_random_grid_search.lpa_utils as lput
import streamlit as st

def print_session_state(config:str, inst:str, names:list):
  for n in names:
    print(f"{config}.{inst}.{n} {st.session_state[config][inst][n]}")

def copy_session_state(config:str, source:str, target:str, names:list):
  for n in names:
    st.session_state[config][target][n] = st.session_state[config][source][n]

def disable_element(name:str, target:str, config:str) -> bool:
  """if .submit is present, then disable this while being processed"""
  key = name.split(".",maxsplit=1)[0] + ".submit"
  try:
    return(st.session_state[config][target][key])
  except:
    return(False)

def text_input(name:str, target:str="target", config="config", container=st, empty_is_invalid=True, value=None) -> str:
  if value is None:
    value = st.session_state[config]['current'][name]
  else:
    value = value
  x = container.text_input(name, 
    value=value, 
    placeholder=st.session_state[config]['default'][name],
    disabled=disable_element(name, target, config),
    help=st.session_state[config]['help'][name])
  x = x.strip()
  if x=="" and empty_is_invalid:
    container.error(f"{name} cannot be empty")
  else:  
    st.session_state[config][target][name] = x
  return(x)

def text_area(name:str, target:str="target", config="config", container=st, empty_is_invalid=True, value=None) -> str:
  if value is None:
    value = st.session_state[config]['current'][name]
  else:
    value = value
  x = container.text_area(name, 
    value=value, 
    placeholder=st.session_state[config]['default'][name],
    disabled=disable_element(name, target, config),
    help=st.session_state[config]['help'][name])
  x = x.strip()
  if x=="" and empty_is_invalid:
    container.error(f"{name} cannot be empty")
  else:  
    st.session_state[config][target][name] = x
  return(x)

def selectbox(name:str, options, index, target:str="target", config="config",**kwargs) -> str:
  options = st.session_state[config]['current'][name+".options"]
  index = options.index(st.session_state[config]['current'][name])
  x = st.selectbox(name,
    options = options, 
    index=index, 
    disabled=disable_element(name, target, config),
    help=st.session_state[config]['help'][name],
    **kwargs)
  st.session_state[config][target][name] = x
  return(x)

def radio(name:str, target:str="target", config="config", **kwargs) -> str:
  options = st.session_state[config]['current'][name+".options"]
  index = options.index(st.session_state[config]['current'][name])
  x = st.radio(name,
    options = options, 
    index=index, 
    disabled=disable_element(name, target, config),
    help=st.session_state[config]['help'][name],
    **kwargs)
  st.session_state[config][target][name] = x
  return(x)

def button(name:str, target:str="target", config="config", **kwargs) -> str:
  print("button disabled", st.session_state[config][target][name])
  x = st.button(name,
    disabled=disable_element(name, target, config),
    help=st.session_state[config]['help'][name],
    **kwargs)
  if x:
    st.session_state[config][target][name] = x
  return(x)

def copy_file_to_session_state(config, cfg_flat:dict):
  cfg, help = lput.separate_help(cfg_flat)
  st.session_state[config]['default'] = copy.deepcopy(cfg)
  st.session_state[config]['current'] = copy.deepcopy(cfg)
  st.session_state[config]['target']  = copy.deepcopy(cfg)
  st.session_state[config]['help']    = copy.deepcopy(help)   

def get_stss(config:str, name:str, state:str='current'):
  return(st.session_state[config][state][name])

def copy_lpa_to_session_state(state, config):
  if state:
    st.session_state[config]['default'] = copy.deepcopy(state.session_state[config]['default'])
    st.session_state[config]['current'] = copy.deepcopy(state.session_state[config]['current'])
    st.session_state[config]['target']  = copy.deepcopy(state.session_state[config]['target'])
    st.session_state[config]['help']    = copy.deepcopy(state.session_state[config]['help'])

def copy_session_state_to_lpa(state, config):
  if state:
    state.session_state[config]['default'] = st.session_state[config]['default']
    state.session_state[config]['current'] = st.session_state[config]['current']
    state.session_state[config]['target']  = st.session_state[config]['target']
    state.session_state[config]['help']    = st.session_state[config]['help'] 

def init_session_state(values:dict, config="config", state=None):
  if config not in st.session_state:
    st.session_state[config] = {}
    if state:
      copy_lpa_to_session_state(state, config)
    else:  
      copy_file_to_session_state(config, values)