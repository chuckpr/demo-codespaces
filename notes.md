`pixi init .`

`pixi add jupyterlab xeus-r`

`pixi shell`

`jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --IdentityProvider.token='' --ServerApp.password=''`

`pixi add r-tidyverse r-palmerpenguins`

`curl -fsSL https://claude.ai/install.sh | bash`

[https://github.com/jupyter-ai-contrib/jupyter-server-mcp](https://github.com/jupyter-ai-contrib/jupyter-server-mcp)

`pixi add  jupyter-server-mcp jupyter-ai-tools jupyterlab-commands-toolkit jupyter-collaboration`

`claude mcp add jupyter-mcp -- uvx --from jupyter-server-mcp jupyter-server-mcp-proxy`

Restart `jupyter`

`jupyter lab --ip=0.0.0.0 --port=8888 --no-browser --IdentityProvider.token='' --ServerApp.password='' --config=jupyter_config.py`

Create `CLAUDE.md` 
  - "Use jupyter MCP tools when working with notebooks"
  - "Use pixi to manage Python and R packages"