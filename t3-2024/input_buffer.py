# Patching `input()` for notebook
input_buffer = []


def set_input_buffer(input_string):
  global input_buffer
  input_buffer = input_string.strip().split('\n')


def input():
  if input_buffer:
    return input_buffer.pop(0)
  else:
    raise Exception("input buffer is empty")
