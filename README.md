# Obligatorio 2 Teoría de la computación
## Implementación de grafos no dirigidos en python

En esta tarea se realizó una implemetación de grafo no dirigido con las siguientes operaciones

* Búsqueda en profundiad (DFS)
* Búsqueda en amplitud (BFS)
* Componentes conexas (SCC)
* Cantidad de componentes conexas
* ¿Es conexo?
* Camino más corto entre 2 nodos
* Largo del camino más corto entre 2 nodos
* Verificar si un camino es el más corto

<hr/>

### Estructura del proyecto
* Módulo `graphutils` con la implementación del grafo y sus operaciones
* `tests.py`
* `main.py`

<hr/>

### Instrucciones de uso
1. Desde Visual Studio Code, abrir el archivo `main.py` o de lo contrario, abrir una terminal y ubicarse en la raiz de proyecto
2. En Visual Studio Code, seleccionar la opción "run python file". Si está en la terminal entonces corra el siguiente comando `python3 main.py`

Estas instrucciones correran los test con los grafos por defecto (g1, g2 y g3) que estan instanciados en el script de `tests.py`, que son los mismos grafos que se utilizaron como ejemplo en la letra del obligatorio.

Si desea correr los tests con un grafo distinto, puede crearlo en `main.py` y llamar a la función `run_tests(g)` con el grafo que creó. Esto correra tests sobre todas las funcionalidades excepto las últimas 3, las relacionadas con el camino más corto ya que para estas también se requieren nodo de origin y nodo de destino.

Para correr tests sobre las funciones de camino más corto invoque a las siguientes funciones:

* shortest_path_test(g, a, b)
* shortest_path_length_test(g, a, b)
* verify_shortest_path_test(g, a, b, p)

Donde *a* y *b* son etiqueta del nodo de origen y *g* un grafo. Para la última función, el parámetro *p* es un camino representado por un arreglo de enteros -o el tipo de etiqueta que usó para su grafo-. 