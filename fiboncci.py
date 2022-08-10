# WARNING: this program assumes the
# fibonacci sequence starts at 1
def fib(num):
  """return the number at index num in the fibonacci sequence"""
  if num <= 2:
    return 1
  return fib(num - 1) + fib(num - 2)


print(fib(10)) 