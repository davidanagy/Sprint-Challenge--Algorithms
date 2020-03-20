#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) `a=0` is O(1), so we can ignore it. The `while` loop is the important part. After the first iteration of the `while` loop, `a` equals n<sup>2</sup>; after the second iteration, it equals n<sup>2</sup> + n<sup>2</sup> or 2n<sup>2</sup>, then 3n<sup>2</sup>, and so on. The loop ends when `a` reaches n<sup>3</sup>--i.e., n * n<sup>2</sup>. This happens after n iterations. Hence, **the runtime complexity is O(n)**.


b) `sum=0` is O(1), so we can ignore it. The `for` loop iterates n times, so that puts us at O(n). `j=1` is O(1), but then we have a `while` loop *inside* the `for` loop. The `while` loop multiplies `j` by 2 each iteration, and lasts until `j` is equal to or bigger than `n`. For example, if `n` is 10, this will require 4 iterations (2*2*2*2 > 10); if `n` is 100, this will require 7 iterations (2*2*2*2*2*2*2 > 100), etc. This is actually the very definition of the `log(n)` function, since a logarithm just says [how many of one number do we multiply to get another number](https://www.mathsisfun.com/algebra/logarithms.html). To put it another way, [time is going up linearly while the n goes up exponentially](https://stackoverflow.com/a/2307330/12685847). Therefore, this `while` loop has a runtime complexity of O(log(n)). Finally, we can ignore the O(1) complexity of `sum += 1`, since that's a constant. Since the `while` is nested within the `for`, we multiply the two complexities together for a **final runtime complexity of O(nlog(n))**.


c)

## Exercise II


