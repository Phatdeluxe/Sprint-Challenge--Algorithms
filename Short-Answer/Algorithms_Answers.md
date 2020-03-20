#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) This while loop looks like it has a time complexity of O(n). 
Generally singel loops have linear time complexity because no matter how much n changes, you are keeping the number of actions constant for each loop.


b) Nested loop. This has a time complexity of O(n^2). More loops would result in
a greater exponent. each time you increase the value of n, you increase the number of 
actions required to finish one loop. Longer while loops in a greater number of for loops



c) I believe that this has a linear time complexity O(n). If n == 0 then it runs once and returns 2. if n == 1, then it runs twice and returns 4. if n == 2 then it runs three times. No matter how much you increase n, the ammount that the function runs increases at a linear rate.

## Exercise II

I remember being asked questions like this before I understood the binary sorting method. This is a great use of the binary sorting method. You can start in the middle, if the egg breaks then you know that every floor above, it will also break. If it does not break, then you know that every floor below it will also not break. Normally in a binary search you would test to see if the value you are currently on is your target value, but because we are looking for two values, you must keep your current floor in the possibility. You can continue to do this until you get the final result

Assuming that floor f does exist.

def egg_break(n):
    broken = False
1. get number of floors
    n == number of floors
2. have an index for the highest possible floor that it could not break on (the top floor)
    high = n
3. have an index for the lowest possible floor that it could break on (the bottom floor)
    low = 0
4. divide the sum of the highest and lowest floor by two. This will be your middle floor
    while True:
        middle = (high + low) // 2
5. drop the egg
        broken = drop_egg(middle)
    - if your highest and lowest possible floors are right next to each other
        if (high - 1) == low:
        - you have found the solution
            return high
    - if it breaks
        elif broken == True:
        - move the highest floor to your current floor
            high = middle
        - repeat steps 4 and 5
    - if it does not break
        if broken == False:
        - move the lowest floor to your current floor
            low = middle
        - repeat steps 4 and 5
    
def drop_egg(n):
    """determines if the egg will break from this height"""
    if egg breaks:
        return True
    else:
        return False


This has a time complexity of O(log(n)). This is a classic binary search and regardless of how big n gets, like a logarithmic graph, the time it takes to run approaches a constant value.