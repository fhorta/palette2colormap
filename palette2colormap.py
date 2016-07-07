import matplotlib
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from mpl_toolkits.mplot3d import Axes3D

def custom_cmap(_sample, _reverse=False):
    midpoint  = .5
    from scipy.ndimage import imread
    im = imread(_sample, mode='RGBA')
    im = im[10:-10,20:-20,:]
    im = im/im.max()
    if _reverse:
        im = np.rot90(im,2)
    nx,ny,nz = im.shape
    my_index = np.linspace(0,ny,257, endpoint=False)
    cdict = {
        'red': [],
        'green': [],
        'blue': [],
        'alpha': []
    }
    shift_index = np.hstack([
        np.linspace(0.0, midpoint, 128, endpoint=False),
        np.linspace(midpoint, 1.0, 129, endpoint=True)
    ])
    for i, si in zip(my_index, shift_index):
        i = int(i)
        r,g,b,a = (im[0,i,0],
                   im[0,i,1],
                   im[0,i,2],
                   im[0,i,3])
        cdict['red'].append((si, r, r))
        cdict['green'].append((si, g, g))
        cdict['blue'].append((si, b, b))
        cdict['alpha'].append((si, a, a))
    mycmap = matplotlib.colors.LinearSegmentedColormap('custom', cdict)
    plt.register_cmap(cmap=mycmap)
    return mycmap

def shift_cmap(cmap, start=0, midpoint=0.5, stop=1.0, name='shiftedcmap'):
    # regular index to compute the colors
    reg_index = np.linspace(start, stop, 257)
    cdict = {
        'red': [],
        'green': [],
        'blue': [],
        'alpha': []
    }
    # shifted index to match the data
    shift_index = np.hstack([
        np.linspace(0.0, midpoint, 128, endpoint=False),
        np.linspace(midpoint, 1.0, 129, endpoint=True)
    ])
    for ri, si in zip(reg_index, shift_index):
        r, g, b, a = cmap(ri)
        cdict['red'].append((si, r, r))
        cdict['green'].append((si, g, g))
        cdict['blue'].append((si, b, b))
        cdict['alpha'].append((si, a, a))
    newcmap = matplotlib.colors.LinearSegmentedColormap(name, cdict)
    plt.register_cmap(cmap=newcmap)
    return newcmap

def _main(argv):
    pl = argv[0]
    rev = argv[1]
    rev = True if int(rev)==1 else False
    print('Pallete file:', pl)
    print('Reverse: ', rev)
    newcmap = custom_cmap(pl, rev)
    #newcmap = shift_cmap(newcmap, midpoint=.3)
    _run_sample(newcmap)

def _run_sample(cmap):
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    X = np.arange(-5, 5, 0.25)
    Y = np.arange(-5, 5, 0.25)
    X, Y = np.meshgrid(X, Y)
    R = np.sqrt(X**2 + Y**2)
    Z = np.sin(R)
    surf = ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cmap,
                        linewidth=0, antialiased=False)
    ax.set_zlim(-1.01, 1.01)
    ax.zaxis.set_major_locator(LinearLocator(10))
    ax.zaxis.set_major_formatter(FormatStrFormatter('%.02f'))
    fig.colorbar(surf, shrink=0.5, aspect=5)
    plt.show()


if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    def help():
        print('\nHelp>> python3 pallete2colormap <png file> <reverse 1|0>\n')
    try:
        _main(argv)
    except IndexError:
        help()
        exit()
    except:
        raise
