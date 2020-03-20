#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) `a=0` is O(1), so we can ignore it. The `while` loop is the important part. After the first iteration of the `while` loop, `a` equals n<sup>2</sup>; after the second iteration, it equals n<sup>2</sup> + n<sup>2</sup> or 2n<sup>2</sup>, then 3n<sup>2</sup>, and so on. The loop ends when `a` reaches n<sup>3</sup>--i.e., n * n<sup>2</sup>. This happens after n iterations. Hence, **the runtime complexity is O(n)**.


b) `sum=0` is O(1), so we can ignore it. The `for` loop iterates n times, so that puts us at O(n). `j=1` is O(1), but then we have a `while` loop *inside* the `for` loop. The `while` loop multiplies `j` by 2 each iteration, and lasts until `j` is equal to or bigger than `n`. For example, if `n` is 10, this will require 4 iterations (2*2*2*2 > 10); if `n` is 100, this will require 7 iterations (2*2*2*2*2*2*2 > 100), etc. This is actually the very definition of the `log(n)` function, since a logarithm just says [how many of one number do we multiply to get another number](https://www.mathsisfun.com/algebra/logarithms.html). To put it another way, [time is going up linearly while the n goes up exponentially](https://stackoverflow.com/a/2307330/12685847). Therefore, this `while` loop has a runtime complexity of O(log(n)). Finally, we can ignore the O(1) complexity of `sum += 1`, since that's a constant. Since the `while` is nested within the `for`, we multiply the two complexities together for a **final runtime complexity of O(nlog(n))**.


c) The `if` statement has a runtime complexity of O(1), since it's just performing a single check. But the recursion statement `2 + bunnyEars(bunnies-1)` keeps running the `if` statement, subtracting 1 each time, until "bunnies" reaches 0. Defining "bunnies" as "n", this means we start at n and run the `if` statement n times, since it takes that many times for n to reach 0. Hence, we end up with a **runtime complexity of O(n)**.

## Exercise II

1. Start by going to the mid-level floor (i.e., floor "`n` divided by 2" rounded down plus one, or `n//2 + 1`), and drop an egg. There are two possibilities: either it breaks, or it doesn't.

2. (a) If the egg breaks, that means `f` must be on a lower floor. So ignore all the floors `n//2 + 1` and above, go to your new middle floor, and drop an egg again. Another way to put this is: define floor `n//2` as your *new* `n`, then return to step 1.

2. (b) If the egg **doesn't** break, that means `f` must be the current floor **or** a higher one (since the egg doesn't break if you drop it from a floor less than f). So ignore all the floors below `n//2 + 1`, go to your new middle floor, and drop an egg again. Another way to put this is: define floor `n//2 + 1` as the *new first floor*, i.e., subtract each floor by `n//2` and ignore all floors that end up 0 or lower. This means that floor `n` is now floor `n - n//2`. Then go back to step 1.

3. By repeating this process over and over again, we cut out around half the floors each time. Thus, if we keep repeating this process, we end up on a single floor, knowing that all the floors above it result in a broken egg and all the floors below it don't. So just drop an egg from this floor. If it breaks, then `f` is the floor below this one; if it doesn't, then this floor is `f`.

Because we're using a "divide and conquer" strategy and halving the input with each step, this algorithm **has a runtime complexity of O(log(n))**.