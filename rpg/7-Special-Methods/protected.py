# https://teamtreehouse.com/library/objectoriented-python-2/special-methods

class Protected:
  __name = "Security"

  def __method(self):
    return self.__name

prot = Protected()
# print(prot.__name) # Can't access
# print(prot.__method) # Can't access
print(dir(prot))

print("****************************************")
print(f"Protected's class' __name is: {prot._Protected__method()}") # var._Class-Name__Method-Name()


