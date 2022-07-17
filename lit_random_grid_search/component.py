import lightning_app as la
import time
# utilities 
import lit_random_grid_search.search_ui as ui
import lit_random_grid_search.st_utils as stut
# setting define the behavior 
import lit_random_grid_search.settings as settings

class LitRandomGridSearch(la.LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        # input to UI
        self.session_state_configs = [settings.cfg_name]
        # parameters for the configs
        self.session_state = {
          settings.cfg_name: settings.config,
          'target': None,
          }  
        # None = not waiting
        # True = UI is waiting for 
        self.session_state_changed = None
    def run(self):
        pass

    def configure_layout(self):
        return la.frontend.StreamlitFrontend(render_fn=ui.run)

