from stream import Stream, IntStream, DictStream


d = {
    "a": 0,
    "b": 1,
    "c": 2,
    "d": [1,2,3,4],
    "e": 4,
    "f": 5
}




def main():
    #for i in IntStream(0, 10).filter(lambda x: x%2):
    #    print(i)

    #for i in DictStream(d).filter(lambda k,v: isinstance(v, list)).values().fmap(lambda x: Stream(x)):
    #    print(i)

    stream = IntStream(0, 100).lt(50).odd()
    print(stream.all_match(lambda x: x > 5))



if __name__ == '__main__':
    main()

