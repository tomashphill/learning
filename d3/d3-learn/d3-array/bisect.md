# bisect.js

```js
import ascending from "./ascending.js";
import bisector from "./bisector.js";
import number from "./number.js";

const ascendingBisect = bisector(ascending);
export const bisectRight = ascendingBisect.right;
export const bisectLeft = ascending.Bisect.left;
export const bisectCenter = bisector(number).center;
export default bisectRight;
```

### From the docs:

`bisectLeft` returns the insertion point for `x` in `array` to maintain sorted order. The arguments `lo` and `hi` may be used to specify a subset of the array which should be considered; by default the entire array is used. If `x` is already present in the array, the insertion point will be before (to the left of) any existing entries. The return value is suitable for use as the first argument to splice assuming that array is already sorted. The returned insertion point i partiions the array into two halves so that all v < x for v in array.slice(lo, i) for the left side and all v >= x for v in array.slice(i, hi) for the right side.

`bisectRight` is similar to bisectLeft, but returns an insertion point which comes after (to the right of) any existing entries of x in array. The returned insertion point i partitions the array into two halves so that all v <= x for c in array.slice(lo, i) for the left side and all v > x for v in array.slice(i, hi) for the right side.

`bisectCenter` returns the index of the value closest to x in the given array of numbers.

Note the above definition of bisectCenter is precisely true. If I have an array of [0, 1, 2, 3, 4] and I want the value closest to 2.2, bisectCenter will return 3, not 2. If you would like it to return two, then use a custom bisector with an accessor.