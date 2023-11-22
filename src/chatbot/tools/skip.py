from langchain.tools import tool

@tool("skip")
def skip(t):
  """Bypass unnecessary steps."""
  return t