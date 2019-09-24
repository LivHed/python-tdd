from byotest import *

# A dictionary with denomination of coin and its quantity as key, value.
usd_coins = {100: 20, 50: 20, 25: 20, 10: 20, 5: 20, 1: 20}
eur_coins = {200: 20, 100: 20, 50: 20, 20: 20, 10: 20, 5: 20, 2: 20, 1: 20}


def get_change(amount, coins=eur_coins):
     """
    Takes the payment amount and returns the change
    `amount` the amount of money that we need to provide change for
    `coins` is the set of coins that we need to get change for (i.e. the set
        of available coins)
    Returns a list of coin values
    """
     change = []
    
    # Unlike a list, looping through a dictionary does not keep the order.
    # Therefore we use `sorted()` to sort the order. This will start with the
    # lowest by default, so we use `reverse=True` to start with the highest
    # denomination. The `while` ends when the domination quantity reaches 0.
    # An exception is thrown if there are insufficient coins to give change.
    
     for denomination in sorted(coins.keys(), reverse=True):
        while denomination <= amount and coins[denomination] > 0:
            amount -= denomination
            coins[denomination] -= 1
            change.append(denomination)
    
     if amount != 0:
        raise Exception("Insufficient coins to give change.")

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
#test_exception_was_raised(get_change, (5, {2: 1, 1: 2}), "Insufficient coins to give change.")


print("All tests pass!")