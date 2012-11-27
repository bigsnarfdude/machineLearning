'''
corey and vishal monster creation
loading kdd99 cup data into pandas dataframe
'''

import pandas, re, numpy as np


def load_file(filename, num_cols, dtypes, delimiter='\t'):
    data = None
    try:
        data = np.fromfile(filename + '.npy', dtype=dtypes)
    except:
        splitter = re.compile(delimiter)

        def items(infile):
            for line in infile:
                for item in splitter.split(line):
                    yield item

        with open(filename, 'r') as infile:
            data = np.fromiter(items(infile), dtypes, -1)
            data = data.reshape((-1, num_cols))
            np.save(filename, data)

    return pandas.DataFrame(data)


if __name__ == "__main__":

    df = pd.read_csv('downsample.csv')
    types = []
    for i in df.columns:
        try:
            i = float(i)
            types.append(type(i))
        except ValueError:
            types.append(type(i))  
    
    dtypes = np.dtype([('feature_'+str(i),types[i]) for i in range(len(types))])
    
    load_file('kddcup.data',42, dtypes, delimiter=',')
