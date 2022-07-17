import streamlit as st
import random
import numpy as np
from deepdiff import DeepDiff, Delta
from pprint import pprint

import lit_random_grid_search.allpatterns as allpatterns
import lit_random_grid_search.lpa_utils as lput
import lit_random_grid_search.st_utils as stut
import lit_random_grid_search.settings as settings

cfgname="config"

def search_show(open_delim="<<", close_delim=">>"):

  text=stut.text_area("search.run")

  col1, col2 = st.columns(2)
  with col1:
    search_option = stut.radio("search.strategy", horizontal=True)
  with col2:
    if search_option == "Random":
      random_search = stut.text_input("search.random.count")  

  if search_option == "None":
    st.session_state[cfgname]["target"]["search.details"]=text
  else:
    col1, col2 = st.columns(2)
    with col1:
      new_open_delim = stut.text_input("search.delim.open")
    with col2:
      new_close_delim = stut.text_input("search.delim.close")

    if text != "" and new_open_delim != "" and new_close_delim != "":
      gridsearch = allpatterns.find_text_inside_delim(text,new_open_delim, new_close_delim)
      gridsearch_len = len(gridsearch)
      col1, col2 = st.columns(2)
      with col1:
        stut.text_input("search.count", value=len(gridsearch))
      with col2:
        if search_option == "Random":
          grid_sample = random.sample(range(0, gridsearch_len), int(random_search))
          print(grid_sample)
          gridsearch=np.array(gridsearch)[grid_sample]
      stut.text_area("search.details", value="\n".join(gridsearch))

  # submit
  stut.button("search.submit")
  # make sure to have some other st. after this so that disable action will trigger

def search_submit(state):
    # process button press
  if st.session_state[cfgname]['target']['search.submit']:
    st.info(st.session_state[cfgname]['target'])
    if state:
      # start to process
      if state.session_state_changed is None:
        # Lightning does not detect change in the dict.  
        state.session_state['target'] = st.session_state[cfgname]['target']
        # Lightning detect change to simple datatype.  
        state.session_state_changed = True
      # wait until processed
      elif state.session_state_changed == True: 
        pass
      # processed.  let the UI unlock
      else:
        # unlock the screen
        st.session_state[cfgname]['target']['search.submit']=False
        # unlock the process change
        state.session_state_changed = None
    else:
      st.session_state[cfgname]['target']['search.submit']=False
      
def run(state):
  if state:
    for config in state.session_state_configs:
      stut.init_session_state(state.session_state[config])
  else:
      stut.init_session_state(settings.config)

  # search form show 
  search_show()
  # search submit 
  search_submit(state=state)

if __name__ == "__main__":
  run(state=None)
  