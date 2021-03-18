# descending.js

Like ascending, but returns -1 if `b` is less than `a`, and 1 if `b` is greater than `a`.

```js
export default function(a, b) {
    return b < a ? -1 : b > a ? 1 : b >= a ? 0 : NaN;
}
```