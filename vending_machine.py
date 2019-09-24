from byotest import *

usd_coins = [100, 50, 25, 10, 5, 2, 1]
eur_coins = [100, 50, 20, 10, 5, 2, 1]

def get_change(amount, coins=eur_coins):
     
    change = []   #As long as the coin is less than or equal to the amount, it will carry on adding it.And only when it's not will it move on or return the change.
    for coin in coins:
        while coin <= amount:
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
test_are_equal(get_change(9), [5, 2, 2]) # pass in the value of 9, We'd expect to get back change of 5 cents, 2 cents, and 2 cents.
test_are_equal(get_change(35, usd_coins), [25, 10]) #we´re passing in a value of 35 and a second argument(that currently don´t exist, and expect back 25 and 10.


print("All tests pass!")