# pairs.js

This is self-explanatory... Takes to values (presumably numbers) and makes them a pair.

```js
// Number -> Number -> (Number, Number)
export function pair(a, b) {
    return [a, b];
}
```

This function takes in a list of values and groups them into pairs. Ex. `[1,2,3,4] -> [[1,2],[3,4]]`

```js
// Iterable[a] -> Optional (a -> a -> b) -> [b]
export default function(values, pairof = pair) {
    const pairs = [];
    let previous;
    let first = false; // skip first so we have 
    for (const value of values) {
        if (first) pairs.push(pairof(previous, value));
        previous = value;
        first = true;
    }
    return pairs;
}
```