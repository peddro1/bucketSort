from random import shuffle
from random import randint
import math
import timeit
import matplotlib as mpl
import matplotlib.pyplot as plt
  
  
def desenhaGrafico(x,y, xl = "Entradas", yl = "Saídas"):
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111)
    ax.plot(x,y, label = "Tempo")
    ax.legend(bbox_to_anchor=(1, 1),bbox_transform=plt.gcf().transFigure)
    plt.ylabel(yl)
    plt.xlabel(xl)
    plt.show()


def geraLista(tam):
    
    lista = list(range(1, tam + 1))
    shuffle(lista)
    return lista
    
x2 = [100000,200000,300000,400000,500000,1000000,2000000]
y = []



def insertionSort(array):
	for i in range(1, len(array)):
		tmp = 0
		tmp = array[i]
		position = i
		while position > 0 and array[position - 1] > tmp:
			array[position] = array[position - 1]
			position -= 1
		array[position] = tmp


def hashing(array):
    m = array[0]
    for i in range(1, len(array)):
        if ( m < array[i] ):
            m = array[i]
    result = [m,int(math.sqrt( len(array)))]
    return result
 

def re_hashing(i, code ):
    return int(i/code[0]*(code[1]-1))
 
def bucketSort(array):
    code = hashing(array)
    buckets = [list() for _ in range( code[1] )]
    for i in array:
        x = re_hashing( i, code )
        buck = buckets[x]
        buck.append( i )
    for bucket in buckets:
        insertionSort(bucket)
        ndx = 0
    for b in range( len( buckets ) ):
        for v in buckets[b]:
            array[ndx] = v
            ndx += 1
            
for a in range(len(x2)):
    array = []
    array = geraLista(x2[a])
  
    
    inicio = timeit.default_timer()
    bucketSort(array)
    fim = timeit.default_timer()
    
    
    y.append('%f' %(fim - inicio))
  
 
    print(y)
    

desenhaGrafico(x2,y)
