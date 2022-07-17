cfg_name = "config"

config = {
  "search.run": "python scripts/train_hydra.py --config-path scripts/configs --config-name config hydra.dir.out=outputs",
  "search.run.help": "Run program script argument",

  "search.strategy": "None",
  "search.strategy.options": ['None', 'Grid', 'Random'],
  "search.strategy.help": "None: no eval of script arguments.  \nGrid: Product of all value combinations.  \nRandom: only take Search Count.  \nInclude: From the product, only run selected args.  \nExclude: From the product, run all except the excluded args",

  "search.delim.open": "<<",
  "search.delim.open.help": "Script Arg where the expression enclosed in <<expression>> areevaluated" ,

  "search.delim.close": ">>",
  "search.delim.close.help": "Script Arg where the expression enclosed in <<expression>> areevaluated" ,

  "search.random.count": "1",
  "search.random.count.help": "Numbers of Grid Search in the random sample",

  "search.count": "1",
  "search.count.help": "Final Number of searchs to execute",

  "search.details": "",
  "search.details.help": "Final runs to be executed",

  "search.submit": False,
}

