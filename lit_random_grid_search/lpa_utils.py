import os
import sh
import lit_random_grid_search.lpa_utils as lput

def removeprefix(x:str, prefix:str) -> str:
  if x.startswith(prefix):
    return(x[len(prefix):])
  else:  
    return(x)

def removesuffix(x:str, suffix:str) -> str:
  if x.endswith(suffix):
    return(x[:-len(suffix)])
  else:
    return(x)

def output_with_video_prediction(lines) -> dict:
  """outputs/2022-07-04/17-28-54/test_vid_heatmap.csv"""
  outputs = {}
  for l in lines:
    l_split = l.strip().split("/")
    value = l_split[-1]
    key = "/".join(l_split[-3:-1])
    outputs[key] = value
  return(outputs)  

def separate_help(conf:dict, suffix=".help") -> list:
  """ move keys that have .help into separate dict"""
  new_cfg = {}
  help_cfg = {}
  for k,v in conf.items():
    if k.endswith(suffix):
      help_cfg[lput.removesuffix(k,suffix)] = v
    else:
      new_cfg[k] = v  
  # missing help, add None
  for k,v in new_cfg.items():
    if not(k in help_cfg ):
      help_cfg[k] = None
  return(new_cfg, help_cfg)

def get_dir_of_dir(root_dir=".", sub_dir=".", include="tb_logs"):
  """return dirs that has tb_logs and maintain relative dir"""
  dir=os.path.join(os.path.expanduser(root_dir),sub_dir)
  options=[]
  try:
    # x.strip() removes \n at then end
    # os.path.dirname removes dir_name at the end
    # os.path.relpath removes root_dir, sub_dir in the beginning
    options = [os.path.relpath(os.path.dirname(x.strip()),dir) for x in sh.find(dir,"-type","d", "-name", include,)]
    options.sort(reverse=True)
  except:
    pass  
  return(options)

def get_dir_of_files(root_dir=".", sub_dir=".", include="predictions.csv"):
  """return dirs that has predictions.csv and maintain relative dir"""
  dir=os.path.join(os.path.expanduser(root_dir),sub_dir)
  options=[]
  try:
    # x.strip() removes \n at then end
    # os.path.dirname removes dir_name at the end
    # os.path.relpath removes root_dir, sub_dir in the beginning
    options = [os.path.relpath(os.path.dirname(x.strip()),dir) for x in sh.find(dir,"-type","f", "-name", include,)]
    options.sort(reverse=True)
  except:
    pass  
  return(options)

def splitall(path):
  allparts = []
  while 1:
    parts = os.path.split(path)
    if parts[0] == path:  # sentinel for absolute paths
      allparts.insert(0, parts[0])
      break
    elif parts[1] == path: # sentinel for relative paths
      allparts.insert(0, parts[1])
      break
    else:
      path = parts[0]
      allparts.insert(0, parts[1])
  return allparts