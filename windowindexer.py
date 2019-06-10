def windowIndexer(iterable,take,skip,start=0,end=None,take_first=True):
    """
    yields windows in an iterable. Will take (yield) then skip or vice versa from
    iterable in range specified by start and end points
    
    iterable = iterable to iterate over such as a list
    take = number of concurrent elements to yield
    skip = number of concurrent elements to skip
    start = start point for taking windows
    end = end point for taking windows if none does to end of iterable
    take_first = if true will yield first then skip if false will skip then yield
    """
    if end == None:
        end=len(iterable)
    else:
        assert end <= len(iterable) , "End longer than iterable"
    assert type(end)==type(take)==type(skip)==type(start)==int , "Take, skip, start, end must be of type int"


    it = iter(iterable)

    for i in range(start):
        next(it)

    count = start
    if take_first==True:
        while count <= end:
            for i in range(take):
                yield next(it)
            for i in range(skip):
                next(it)
            count += take + skip
    elif take_first==False:
        while count <= end:
            for i in range(skip):
                next(it)
            for i in range(take):
                yield next(it)
            count += take + skip
    else:
        print("Take or skip first?")
