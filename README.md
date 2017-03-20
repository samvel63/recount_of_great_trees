# Recount of a great trees #

### Definition of great tree: ###
A great tree with root X0 is the graph G = (E, F) if there exists a unique vertex A, into which no arcs come; In each other vertex exactly one arc comes in; The graph has no contours.

Picture with an example of a great tree below.

![Image alt](https://github.com/samvel63/recount_of_great_trees/raw/master/images/img1.jpg)

***

### Tasks algorithm ###

1. Find connectivity matrix.
2. Find the occurrence matrix.
3. Calculate difference of occurrence matrix and сonnection matrix.
4. Remove k-th column and row in matrix(k - position of the root of great tree).
5. Сalculate determinant of resulting matrix.

***
