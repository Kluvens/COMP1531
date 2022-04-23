# python strings are immutable
# lists are for mutable ordered structures of the same type
# tuples are fore immutable ordered structures of any mix of types
# An exception is an action that disrupts the normal flow of a program. This action is often representative of an error being thrown. Exceptions are ways that we can elegantly recover from errors

try:
  print(x)
except:
  # if try block cannot run, run except block
  print("An exception occurred")
  
try:
  print(x)
except NameError:
  print("Variable x is not defined")
except:
  print("Something else went wrong")
  
try:
  print(x)
except:
  print("Something went wrong")
finally:
  # no matter which block is run before, we run finally block in the end
  print("The 'try except' is finished")
  
# pytest for checking exception
def test_zero_division():
  with pytest.raises(ZeroDivisionError):
      1 / 0
