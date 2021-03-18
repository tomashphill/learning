# permute.js

Returns a permutation of the specified source object (or array) using the specified iterable of keys. The returned array contains the corresponding property of the source object for each key in keys, in order.

```js
// (Object Any Any, [Hashable Any]) -> [Any]
// ([a], [int]) -> [a]
export default function(source, keys) {
    return Array.from(keys, key => source[key]);
}
```