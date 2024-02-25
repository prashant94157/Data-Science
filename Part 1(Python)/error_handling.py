# try:
#   # f = open('testfile.txt')
#   v = arr
# except FileNotFoundError:
#   print('file not exists', FileNotFoundError)
# except Exception as e:
#   print(e)

# try:
#   print('try part')
# except FileNotFoundError:
#   print('file not exists', FileNotFoundError)
# except Exception as e:
#   print(e)
# else:
#   print("else part") # will be executed if there is no exception
# finally:
#   print("finally part")

# try:
#   print('try part')
# except FileNotFoundError:
#   print('file not exists', FileNotFoundError)
# except Exception as e:
#   pass # we are sure that we will handle exception but until that time we write pass for correctly running the code 
# else:
#   print("else part") # will be executed if there is no exception
# finally:
#   print("finally part")



try:
  num = 69
  den = 0
  if(den==0):
    raise Exception
  else:
    print("result", num/den)
except Exception:
  print('Dividing by zero is not possible')
