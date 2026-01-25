# Questions on OOPS (Python)

# 1.)Design a class as described below.
# class: User
# instance variable: name(String)
# constructor: parameter: none, task: initialize the instance variable to "Default"

# class User:
#     def __init__(self):
#         self.name = "Default"
    
# user1 = User()
# print(user1.name)        

# 2.)  Develop a class Calculator with methods to add and subtract two numbers.
# class Calculator:
#     def add(self, a, b):
#         return a + b
#     def sub(self, a,b):
#         return a - b
# c = Calculator()
# print(c.add(2,2))
# print(c.sub(4,2))

# 3.)   You receive data from multiple sources:
# • Batch files
# • Streaming systems
# Create:
# • A base class DataSource
# • Child classes BatchSource and StreamingSource
# Each should implement a fetch_data() method.

# class DataSource:
#     def fetch_data(self):
#         raise NotImplementedError("Subclasses must implement this method")

# class BatchFiles(DataSource):
#     def fetch_data(self):
#         return "Fetching batch files"

# class StreamingSystems(DataSource):
#     def fetch_data(self):
#         return "Fetching streaming "            

# batch = BatchFiles()
# stream = StreamingSystems()

# print(batch.fetch_data())
# print(stream.fetch_data()) 
    

# 4.) You are processing banking transactions.
# Create a Transaction class where:
# • amount cannot be accessed directly
# • Amount should never be negative
# • Provide methods to update and fetch the amount safely
# Constraints
# • If someone tries to set a negative amount, raise an error.

# class Transaction:
#     def __init__(self, amount):
#         if amount < 0:
#             raise ValueError("Amout cannot be negative")
#         self.__amount = amount
        
#     #getter
#     def get_amount(self):
#         return self.__amount
    
#     # setter
#     def set_amount(self, amount):
#         self.__amount = amount
        
# txn = Transaction(10000)
# print("get amount: ", txn.get_amount())
# txn.set_amount(5000)
# print("updated amount: ", txn.get_amount())



# 5.) Design a class as described below:
# • Class Name: Addition
# • Method:
# o Function Name: add
# o Parameters: a (int), b (int)
# o Return Type: int
# o Static: Yes (Use the @staticmethod decorator)
# o Task: Returns the sum of the values given as parameters.

# class Addition:
#     @staticmethod
#     def add(a, b):
#         return a+b
# print(Addition.add(3,2))    


# 6.) Create an abstract class DataPipeline with:
# • extract()
# • transform()
# • load()
# Implement a concrete class TransactionPipeline.

"""An abstract class:

Is a blueprint

Cannot be used to create objects

Forces child classes to implement certain methods
"""

from abc import ABC, abstractmethod

class DataPipeline:
    @abstractmethod
    def extract(self):
        pass
    
    @abstractmethod
    def transform(self):
        pass
    
    @abstractmethod
    def load(self):
        pass

# Implement a concrete class TransactionPipeline.
class TransactionPipeline(DataPipeline):
    def extract(self):
        print("Extracting transaction data")
    
    def transform(self):
        print("Transforming transaction data")
    
    def load(self):
        print("Loading transaction data from the database")

pipeline = TransactionPipeline()
pipeline.extract()
pipeline.transform()
pipeline.load()
    
     

