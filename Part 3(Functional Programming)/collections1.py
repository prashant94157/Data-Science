import collections
from pprint import pprint
Scientist = collections.namedtuple('Scientist', ['name','field','born','nobel'])
# prashant = Scientist(name="Prashant Maurya", field='ML', born='2000', nobel=False)
# print(prashant.name)

scientists = [
  Scientist(name="Ajitesh", field="Physics", born='2000', nobel=True),
  Scientist(name="Sumit", field="Mathematics", born='2001', nobel=False),
  Scientist(name="Shivesh", field="Chemistry", born='2002', nobel=True),
  Scientist(name="Monil", field="Mathematics", born='2000', nobel=False),
  Scientist(name="Yuvraj", field="Physics", born='2000', nobel=True),
  Scientist(name="Tanmay", field="Chemistry", born='2001', nobel=False),
  Scientist(name="Danish", field="Chemistry", born='1999', nobel=True)
  ]

"""Filter() function"""
# i = filter(lambda x:x.nobel is True, scientists)
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))
# print(next(i))

# tuple_ = tuple(filter(lambda x:x.nobel is True, scientists))
# print(tuple_)

# def nobel_filter(x):
#   return x.nobel

# print(tuple(filter(nobel_filter, scientists)))

'''Map() function '''
# names = tuple(map(lambda x:x.name,scientists))
# print(names)

# objs = [{'name': x.name, 'age': 2024 - int(x.born)} for x in scientists]
# print(objs)

'''Reduce() function'''
from functools import reduce
# total_age = reduce(
#   lambda acc,val: acc + 2024 - int(val.born),
#   scientists,
#   0
# )
# print(total_age)

# fields_arr = {'Physics':[], 'Chemistry':[], 'Mathematics':[]}
# def reducer(acc, val):
#   acc[val.field].append(val.name)
#   return acc
# fields = reduce(reducer,scientists,fields_arr)
# print(fields)

'''Sequential processing'''
# import time
# def transform(x):
#   print(f'Processing record {x.name}')
#   time.sleep(1)
#   result = {'name': x.name, 'age': 2024 - int(x.born)}
#   print(f'Done processing record {x.name}')
#   return result

# start = time.time()
# result = tuple(map(transform, scientists))

# end = time.time()

# print(f'Time to complete: {end-start:.2f}s')
# print(result)

'''Multiprocessing(Process)'''
# import time
# from multiprocessing import Process,Manager

# def print_func(x,y):
#   print(f'Processing record {x.name}')
#   time.sleep(1)
#   result = {'name': x.name, 'age': 2024 - int(x.born)}
#   print(f'Done processing record {x.name}')
#   y[x.name] = result

# if __name__ == "__main__":  # confirms that the code is under main function
#   start = time.time()
#   manager = Manager()
#   names = manager.dict()
#   procs = []
#   for x in scientists:
#     proc = Process(target=print_func, args=(x,names))
#     procs.append(proc)
#     proc.start()

#   # complete the processes
#   for proc in procs:
#     proc.join()

#   end = time.time()

#   print(f'Time to complete: {end-start:.2f}s')
#   print(names)


'''Multiprocessing(Pool)'''
# import time
# from multiprocessing import Pool

# def print_func(x):
#   print(f'Processing record {x.name}')
#   time.sleep(1)
#   result = {'name': x.name, 'age': 2024 - int(x.born)}
#   print(f'Done processing record {x.name}')
#   print(result)

# if __name__ == "__main__":  # confirms that the code is under main function
#   start = time.time()
#   p = Pool(8)
#   p.map(print_func, scientists)
#   end = time.time()

#   print(f'Time to complete: {end-start:.2f}s')

pprint(scientists)