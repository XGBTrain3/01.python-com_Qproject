The regression line of **y** on **x** is **3x + 4y + 8 = 0**, and the regression line of **x** on **y** is **4x + 3y + 7
= 0**. What is the value of the Pearson correlation coefficient?

___

#### Answer: _-3/4_

---

> **Step 1: Rewrite the 2 lines in proper form**
>
> Rewrite the 2 lines as:
>
> y = -2 + (-3/4) * x
>
> x = -7/4 + (-3/4) * y
>
> so b1 = -3/4 and b2 = -3/4
>
> **Step 2: Apply Pearson's Coefficient formula**
>
> Let p = pearson coefficient
>
> Let x_std = standard deviation of x
>
> Let y_std = standard deviation of y
>
> From [tutorial](https://www.hackerrank.com/challenges/s10-least-square-regression-line/tutorial):
>
> p = b1 (x_std / y_std)
>
> p = b2 (y_std / x_std)
>
> Multiplying these 2 equations together
>
> p^2 = b1 * b2
>
> p^2 = (-3/4) * (-3/4)
>
> p^2 = 9/16
>
> p = 3/4 or -3/4 (depending on correlation of x and y)
>
> **Step 3: Find out if p is positive or negative**
>
> Notice that both of the original line equations have negative slopes, so x and y are negatively correlated by definition. So, **p = -3/4**
>
> --- _by **RodneyShag**_
