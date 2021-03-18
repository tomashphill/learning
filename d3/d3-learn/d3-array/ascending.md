# ascending.js

This function compares two values to determine whether they are ascending, or descending.

ascending `returns` -1  
descending `returns` 1

if the variables are equal, however, the function returns `NaN`

```js
// a -> a -> 1 | -1 | NaN
export default function(a, b) {
    return a < b ? -1 : a > b ? 1 : a >= b : NaN;
}
```

Default exports are useful to export only a single object, function, variable. During the import, we can use any name to import.

For example, I can import this like:

```js
import x from './ascending'
console.log(x(3, 4) === -1); // true
```
