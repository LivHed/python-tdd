from byotest import *

def get_change(amount):
    if amount == 0:  #make an if statement to make sure our first test does not break when doing the next test
        return []
                    
    return [amount]  
        
 #remember to put our tests in here before the print("All tests pass!") and after our function
 #write tests for out every coin denominations:
test_are_equal(get_change(0), []) #we expect when we get zero change we get an empty list back
test_are_equal(get_change(1), [1]) #we expect when we get one change that ge get 1 to be returned 
test_are_equal(get_change(2), [2])
test_are_equal(get_change(5), [5])
test_are_equal(get_change(10), [10])
test_are_equal(get_change(20), [20])
test_are_equal(get_change(50), [50])
test_are_equal(get_change(100), [100])

print("All tests pass!")