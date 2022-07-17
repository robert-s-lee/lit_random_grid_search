import lightning_app as la
from lit_random_grid_search import LitRandomGridSearch
from lit_bashwork import LitBashWork

import time

class LitApp(la.LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        self.ui = LitRandomGridSearch()
        self.work = LitBashWork()
        self.index = 0

    def run(self):
        if self.ui.session_state_changed:
          target = self.ui.session_state['target']
          search_details = target["search.details"].split("\n")
          search_details_len = len(search_details)
          #print(search_details)
          if self.index < search_details_len:
            cmd=search_details[self.index]
            self.work.run(cmd)
            print(cmd)
            print(search_details_len, self.index, search_details[self.index])
            print(target)
            self.index += 1
          else:  
            print(self.index, search_details_len)
            print(target)
            self.index = 0
            self.ui.session_state_changed = False


app = la.LightningApp(LitApp())
