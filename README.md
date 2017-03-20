# Подсчет количества прадеревьев в графе и построение графа #

### Определение прадерева ###
**Прадеревом с корнем A** называется граф G = (E, Г), если существует единственная вершина А, в которую не заходит ни одна дуга; в каждую другую вершину заходит в точности одна дуга; граф не имеет контуров.

На картинке пример с прадеревом:

![Image alt](https://github.com/samvel63/recount_of_great_trees/raw/master/images/img1.jpg)

***

### Алгоритм вычисления ###

1. Найти матрицу связности.
2. Найти матрицу вхождений.
3. Посчитать разность матрицы вхождений и матрицы связности.
4. У полученной матрицы удалить k-ую строку и столбец, k - это корень прадерева.
5. Посчитать детериминант у обработанной матрицы.
Полученное число будет количеством частичных прадеревьев на графе.

***
### Инструкция по запуску ###

1. Сначала необходимо установить фласк и его виртуальное окружение:

![Image alt](https://github.com/samvel63/recount_of_great_trees/raw/master/images/img2.jpg)

2. Далее файлы с репозитория нужно поместить в папку flask_simple_ajax(название может быть любым).
3. Открыть и запустить файл.
4. В любом браузере заходим по ссылке localhost:5000 и пользуемся программой.

***
### Инструкция по использованию программы ###

<li>Чтобы соединить графы проведите зажатой левой кнопкой мышь от первой вершины до второй.
<li>Чтобы сделать цикл, необходимо выделить вершину левой кнопкой мышь и нажать 'R' - вершина будет выделена черной линией.
<li>Чтобы удалить вершину или дугу, выделите её и нажмите 'Delete'.
<li>Если выделить дугу, то при нажатии кнопки 'R' дуга будет направлена вправо.
<li>Если выделить дугу, то при нажатии кнопки 'L' дуга будет направлена влево.
<li>Если выделить дугу, то при нажатии кнопки 'B' дуга будет направлена в обе стороны.
<li>Если зажать ctrl + левая кнопка мышb, то можно менять место вершин.