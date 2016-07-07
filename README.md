# palette2colormap

You may need Python 2.7+ and (pip install) matplotlib, numpy and (maybe) mpl_toolkits.

    python pallete2colormap.py <png file> <reverse 1|0>

You can run a sample (as attached) or import the code and create/shift your colormap.

I highly recommend using Anaconda to get dependencies: 

    #Download https://www.continuum.io/downloads

    conda create --name cmap python=3
    source activate cmap #or whatever name you like
    conda install matplotlib scipy pillow
  
Example

![alt tag](https://github.com/fhorta/palette2colormap/blob/master/example/W5.png)
![alt tag](https://github.com/fhorta/palette2colormap/blob/master/example/W5-normal.png)
![alt tag](https://github.com/fhorta/palette2colormap/blob/master/example/W5-reverse.png)
