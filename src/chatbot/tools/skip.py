from langchain.tools import tool

@tool("skip")
def skip(t):
  """Use when you want to skip this step"""
  return t