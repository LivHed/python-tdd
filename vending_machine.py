from byotest import *

def get_change(amount):
    if amount == 0:  #make an if statement to make sure our first test does not break when doing the next test
        return []
        
    if amount in [100, 50, 20, 10, 5, 2, 1]:
        return [amount]    
     
    change = [] 
    for coin in [100, 50, 20, 10, 5, 2, 1]:
        if coin <= amount:
            amount -= coin
            change.append(coin)
            
    return change
      
        
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
test_are_equal(get_change(3), [2, 1]) #we pass in the value of 3 and we expect 2 and 1 coming back as a change. 
test_are_equal(get_change(7), [5, 2]) 

print("All tests pass!")