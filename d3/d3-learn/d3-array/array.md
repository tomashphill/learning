# D3 ARRAY

this file exports the functions map and slice from the Array prototype object. The functions won't work on their own, since they are not bound to an object. Let's see how d3 handles this later.

```js
var array = Array.prototype;

export var slice = array.slice;
export var map = array.map;
```