# Python code to illustrate 
# Decorators with parameters in Python 

def decorator(*args, **kwargs): 
	print("Inside decorator") 
	
	def inner(func): 
		
		# code functionality here 
		print("Inside inner function") 
		print("I like", kwargs['like']) 
		
		func() 
		
	# reurning inner function	 
	return inner 

@decorator(like = "decorators") 
def my_func(): 
	print("Inside actual function") 
