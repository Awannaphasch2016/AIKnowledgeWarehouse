:Dask:
* how to convert from pandas to Dask
    * ref
        * https://stackoverflow.com/questions/39721800/convert-pandas-dataframe-to-dask-dataframe
    ```
    import pandas as pd
    import dask.dataframe as dd
    from dask.dataframe.utils import make_meta

    df=pd.DataFrame({'a':[1,2,3],'b':[4,5,6]})

    dsk = {('x', 0): df}

    meta = make_meta({'a': 'i8', 'b': 'i8'}, index=pd.Index([], 'i8'))
    d = dd.DataFrame(dsk, name='x', meta=meta, divisions=[0, 1, 2])
    print (d)
    dd.DataFrame<x, npartitions=2, divisions=(0, 1, 2)>
    ```
