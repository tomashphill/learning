# sort.js

```js
import ascending from "./ascending.js";
import permute from "./permute.js";
```

`sort` will either take a comparator, or multiple accessors. If accessors are supplied, array is sorted in ascending order. If accessor is nondeterministic, this algorithm will still work, since the accessor is invoked only once (and we sort with the original's index after mapping the nondeterministic accessor to the array). `sort` will return a new array instead of sorting by reference.

```js
export default function sort(values, ...F) {
    if (typeof values[Symbol.iterator] !== "function") throw new TypeError("values is not iterable");
    values = Array.from(values); // where we copy values
    // if F is an empty array, f is defaulted to ascending
    // else, the first element of F overides f 
    let [f = ascending] = F;
    // if f is an accessor or if multiple accessors are passed in
    if (f.length === 1 || F.length > 1) {
        const index = Uint32Array.from(values, (d, i) => i);
        if (F.length > 1) {
            F = F.map(f => values.map(f));
            index.sort((i, j) => {
                for (const f of F) {
                    const c = ascending(f[i], f[j]);
                    if (c) return c;
                }
            });
        } else {
            f = values.map(f);
            index.sort((i, j) => ascending(f[i], f[j]));
        }
        return permute(values, index);
    }
    // if no accessor and f is comparator,
    // use comparator to sort
    return values.sort(f);
}