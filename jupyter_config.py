# Jupyter config that turns on the MCP server and exposes the Jupyter tools.
#
# Needs these packages in the same env as Jupyter:
#   jupyter-server-mcp  jupyter-ai-tools  jupyterlab-commands-toolkit
#
# Start Jupyter with:
#   jupyter lab --config=jupyter_config.py
#
# The MCP server then listens on http://localhost:3001/mcp
# Connect a client with the proxy (it finds the running server by itself):
#   uvx --from jupyter-server-mcp jupyter-server-mcp-proxy

c = get_config()  # noqa: F821

c.MCPExtensionApp.mcp_port = 3001

c.MCPExtensionApp.mcp_tools = [
    # --- notebook toolkit (jupyter_ai_tools.toolkits.notebook) ---
    "jupyter_ai_tools.toolkits.notebook:read_notebook",
    "jupyter_ai_tools.toolkits.notebook:read_notebook_cells",
    "jupyter_ai_tools.toolkits.notebook:read_cell",
    "jupyter_ai_tools.toolkits.notebook:add_cell",
    "jupyter_ai_tools.toolkits.notebook:insert_cell",
    "jupyter_ai_tools.toolkits.notebook:delete_cell",
    "jupyter_ai_tools.toolkits.notebook:edit_cell",
    "jupyter_ai_tools.toolkits.notebook:select_cell",
    "jupyter_ai_tools.toolkits.notebook:get_cell_id_from_index",
    "jupyter_ai_tools.toolkits.notebook:get_active_notebook",
    "jupyter_ai_tools.toolkits.notebook:get_active_cell_id",
    "jupyter_ai_tools.toolkits.notebook:create_notebook",
    # --- jupyterlab toolkit (jupyter_ai_tools.toolkits.jupyterlab) ---
    "jupyter_ai_tools.toolkits.jupyterlab:open_file",
    "jupyter_ai_tools.toolkits.jupyterlab:run_cell",
    "jupyter_ai_tools.toolkits.jupyterlab:run_all_cells",
]
