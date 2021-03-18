# number.js

This function casts a piece of data into a number, as long as it is not null. If it is null, it turns the null object into NaN. I'm assuming this is primarily used to turn strings to numbers? We'll see... 

**Note:** `+x` does not turn a negative number into a positive one.

```js
// String | Number -> Optional Number
export default function(x) {
    return x === null ? NaN : +x;
}
```

The function `numbers` is an iterator. `values` must be some iterable or "functor" (to be fancy) of numbers or string of numbers. `valueof` is a function that takes in the current iterated value, the current index of iteration, and the iterable `values`... my suspicion is `valueof` is passed in as a function to cast the value into a number. The value is not yielded if it can't be casted into a number.

**Note:** the statement `value = +value` in the if statement sets the variable `value` for the rest of the function's scope.

The `>=` operator is used because if a bad value is casted to a number, becoming `NaN`, then `NaN >= NaN` becomes `false`.

```js
// Iterable -> Optional (Any -> Int -> Iterable -> Number) -> Iterator
export function* numbers(values, valueof) {
    if (valueof === undefined) {
        for (let value of values) {
            if (value != null && (value = +value) >= value) {
                yield value;
            }
        }
    } else {
        let index = -1;
        for (let value of values) {
            if ((value = valueof(value, ++index, values)) 
            != null && (value = +value) >= value) {
                yield value
            }
        }
    }
}