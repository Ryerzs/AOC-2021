---
creation date: 2021-12-07 21:00
modification date: Tuesday 7th December 2021 21:00:15
---
<< [[2021-12-06]] | [[2021-12-08]] >>
# Solution with polynomial
Plotting the the fuel cost for all different positions along
with the fuel cost if we don't calculate the distance
to each point and instead take the difference.

What we end up with if we just take difference is a perfect
second degree polynomial. I've plotted this polynomial
in blue and the actual fuel cost in red.

We can observe that the blue line fits the actual fuel cost
very closely (you can't really see the blue line :P)
[[_plot_star_2.pdf]]

If we let $\bar{x}$ be the reference point we are
trying to measure the fuel to then the actual fuel cost
is calculated as
$$
f(\bar{x}) = \sum_{k = 0}^{N}
\frac
{|\bar{x} - k|\cdot (|\bar{x} - k| + 1 )}{2}
C_{Crabs}(k)
$$
where $C_{Crabs}(k)$ is the number of crabs at the
horizontal position k.

Since the denominator in the expression always has the same
sign, except for the few points when $k \in [\bar{x}, \bar{x} +1]$
(I think that's right).
This leads to
$$
|\bar{x} - k|\cdot (|\bar{x} - k| + 1 )\approx
(\bar{x} - k)(\bar{x} - k +1)
$$
Which is why we get such a close fit with a polynomial.