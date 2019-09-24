from byotest import *

def get_change(amount):
    if amount == 0:  #make an if statement to make sure our first test does not break when doing the next test
        return []
                    
    return [1]    #The if statement means that 0 results in no coins, and 1 makes our second test pass.
        
 #remember to put our tests in here before the print("All tests pass!") and after our function
 
test_are_equal(get_change(0),[]) #we expect when we get zero change we get an empty list back
test_are_equal(get_change((1),[1]) #we expect when we get one change that ge get 1 to be returned 

print("All tests pass!")