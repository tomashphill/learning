# bisector.js

```js
import ascending from "./ascending.js"
```
`ascendingComparator` returns an altered ascending function, applying function `f` to the first argument.
`f` is applied only to the first argument, because the first argument might be an object where `f` is used to access the desired property to be compared. 

```js
// (a -> b) -> (a, b) -> -1 | 1 | NaN
function ascendingComparator(f) {
    return (d, x) => ascending(f(d), x);
}
```

`f` will either be an accessor (function with one parameter), or a comparator (function with two parameters).

**Note:** The length property of a function returns the number of parameters the function takes.

Given a sorted list of `a`, and an item `x`, a bisector will return the index where `x` would be inserted, if it were. Doing it from left or right is just describes how the algorithm handles cases where there are multiples of the same item in a list. It does this with a binary search algorithm.

There's a lot to unpack in the handling of finding the center, depending on what sort of comparator you use as f. If you supply an accessor, it will essentially round your value to the closest other value, and return the other value's index. If "ascending" (I'm looking at the tests here) is supplied as the comparator, it will round up.

```js
export default function(f) {
    // delta used in center method
    let delta = f;
    let compare = f;
 
    if (f.length === 1) {
        delta = (d, x) => f(d) - x;
        compare = ascendingComparator(f);
    }

    function left(a, x, lo, hi) {
        if (lo == null) lo = 0;
        if (hi == null) hi = a.length;
        while (lo < hi) {
            const mid = (lo + hi) >>> 1;
            // if a[mid] is less than x
            if (compare(a[mid], x) < 0) lo = mid + 1;
            else hi = mid;
        }
        return lo;
    }

    function right(a, x, lo, hi) {
        if (lo == null) lo = 0;
        if (hi == null) hi = a.length;
        while (lo < hi) {
            const mid = (lo + hi) >>> 1;
            // if a[mid] is greater than x
            if (compare(a[mid], x) > 0) hi = mid;
            else lo = mid + 1;
        }
        return lo;
    }

    function center(a, x, lo, hi) {
        if (lo == null) lo = 0;
        if (hi == null) hi = a.length;
        const i = left(a, x, lo, hi - 1);
        return i > lo && delta(a[i - 1], x) > -delta(a[i], x) ? i - 1 : i;
    }

    return {left, center, right};
}
```

**Note:** The `>>>` operator in javascript is the "unsigned right shift operator", and will shift the number of specified bits to the right. It's essentially a floor division of 2.