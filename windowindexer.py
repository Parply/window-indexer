def windowindexer(iterable,take,skip,start=0,end=None,take_first=True):
    
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
