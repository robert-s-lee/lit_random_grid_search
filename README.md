# lit_random_grid_search component

This ⚡ [Lightning component](lightning.ai) ⚡ was generated automatically with:

```bash
lightning init component lit_random_grid_search
```

## To run lit_random_grid_search

First, install lit_random_grid_search (warning: this app has not been officially approved on the lightning gallery):

```bash
lightning install component https://github.com/theUser/lit_random_grid_search
```

Once the app is installed, use it in an app:

```python
from lit_random_grid_search import TemplateComponent
import lightning_app as la


class LitApp(lapp.LightningFlow):
    def __init__(self) -> None:
        super().__init__()
        self.lit_random_grid_search = TemplateComponent()

    def run(self):
        print(
            "this is a simple Lightning app to verify your component is working as expected"
        )
        self.lit_random_grid_search.run()


app = lapp.LightningApp(LitApp())
```
# setup

git clone https://github.com/robert-s-lee/hello