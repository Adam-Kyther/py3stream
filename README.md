# py3stream - manipulate collections

## Table of contents
* [Description](#Description)
* [Installation](#Installation)
* [Usage](#Usage)

## Description
Package contains classes to support operations on collection like set, list, dict or range using chain of generators.
Classes from the package are: *Stream*, *IntStream* and *DictStream*.

```
example_list = ["1", "5", "2", "10", "11"]
sum = Stream(example_list).map_to_int().filter(lambda x: x < 10).sum()
# result: [1, 5, 2] -> 8
```

In the example class *Stream* has been used on the *example_list*. First there is registered generator for changing strings to ints, then registered generator with lambda expression for elements lower than *10* and sum them.

Classes *Stream*, *IntStream* and *DictStream* are not collections but they are iterable. They hold provided collection as an *iterable object* and generators which are related with *filter(s)* and *map(s)* methods for future **lazy** evaluation.

#### Iteration example
Streams can be used with python *for-loop*. 
```
for element in IntStream(1, 9).filter(lambda x: x % 2 == 0):
    print(element)
# result: 2, 4, 6 and 8
```

## Installaton
To use the streams install the package.
```
pip install py3stream
```

## Usage




