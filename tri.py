from scipy.spatial import Delaunay
import numpy as np

def graph(array, coor):
    points = np.array(array)
    point = np.array(coor)
    tri = Delaunay(points)

    import matplotlib.pyplot as plt
    plt.triplot(points[:,0], points[:,1], tri.simplices)
    plt.plot(points[:,0], points[:,1], 'o')
    plt.plot(point[0], point[1], 'o')

    for j, p in enumerate(points):
        plt.text(p[0]-0.03, p[1]+0.03, j, ha='right') # label the points
    for j, s in enumerate(tri.simplices):
        p = points[s].mean(axis=0)
        plt.text(p[0], p[1], '#%d' % j, ha='center') # label triangles
    plt.xlim(19.3, 19.45); plt.ylim(-99.12, -99.2)
    plt.show()

    coordenadas = points[tri.simplices[0]]
    puntos = tri.simplices[0]
    coordenadas[0]
    


