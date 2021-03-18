# count.js

```js
// Iterator a -> Optional () ->
export default function count(values, valueof) {
    let count = 0;
    if (valueof === undefined) {
        for (let value of values) {
            if (value != null && (value = +value) >= value) {
                ++count;
            }
        }
    }
}