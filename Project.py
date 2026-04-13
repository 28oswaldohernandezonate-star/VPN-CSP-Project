











import math
import random
modulo = 1001 #must be odd 

def is_prime(num):
  if num % 2 == 0:
    return False
  i = 3
  while i < math.sqrt(num):
    if (num % i == 0):
      return False
    i += 2
  return True

def get_rand_prime():
  prime_list = []
  for num in range(1, modulo): 
    if is_prime(num):
      prime_list.append(num)
  return prime_list


def find_public(private):
  for num in range(1, modulo):
    if (private * num) % modulo == 1:
      return num
  return False


class Person:
  def __init__(self, private, secret):
    if private != None:
      self.privateKey = private
      self.publicKey = find_public(private)
    self.secretNum = secret
 
  def calculate_public_num(self, other_public_num):
    self.publicNum = other_public_num * self.secretNum % modulo

def crackingMod():
 for i in range(len(Plist)):
   if (Plist[i] * person1.publicKey) % modulo == 1: 
     return i 
   return False 

def crackingAll():
 for i in range(len(allList)):
   if (allList[i] * person1.publicKey) % modulo == person2.publicNum: 
     return i 
   return False 
 
modulo = int(input("What is the public modulo?(must be odd): "))

Plist = get_rand_prime() 

allList= list(range(0,1002))

#person1
print("\x1B[1J\x1B[1;1H")
print("Enter the information for person1: ")
private_key = int(input("What is the persons private key?. You can also enter 1 for a random prime number: "))
if private_key == 1:
  private_key = get_rand_prime()
else:
  while find_public(private_key) == False:
    private_key = int(input("Not a valid number, enter a new private key: "))


print("\x1B[1J\x1B[1;1H")
person1 = Person(private_key, None)


#person2
print("\x1B[1J\x1B[1;1H")
print("Enter the information for person2: ")
secret_num = int(input("What is the persons secret number (0 to the public modulus)? You can also enter -1 for a random prime number: "))
if secret_num == -1:
  secret_num = random.randrange(0, modulo)
else:
  while secret_num < modulo & secret_num >= 0:
    secret_num = int(input("Not a valid number, enter a new private key: "))
   
print("\x1B[1J\x1B[1;1H")
person2 = Person(None, secret_num)
person2.calculate_public_num(person1.publicKey)


print("Person1's public number is: ", person1.publicKey, ". The public modulus is: ", modulo)
print("Person2, try to guess the private key for person1:")
while (int(input("Guess an integer: ")) * person1.publicKey) % modulo != 1:
  continue


print("\nYou got it! Now guess Person2's secret number and you'll cracked the code.")
print("Person2's public number is: ", person2.publicNum, ". The public modulus is: ", modulo)
while (int(input("Guess an integer: ")) * person1.publicKey) % modulo != person2.publicNum:
  continue


print("\n\nYou cracked the code!")
print("The public modulus was: ", modulo)
print("Person1's private key was: ", person1.privateKey)
print("Person2's secret number was: ", person2.secretNum)












  
 
  
     

