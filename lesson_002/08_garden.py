#!/usr/bin/env python
# -*- coding: utf-8 -*-

# в саду сорвали цветы
garden = ('ромашка', 'роза', 'одуванчик', 'ромашка', 'гладиолус', 'подсолнух', 'роза', )

# на лугу сорвали цветы
meadow = ('клевер', 'одуванчик', 'ромашка', 'клевер', 'мак', 'одуванчик', 'ромашка', )

# создайте множество цветов, произрастающих в саду и на лугу
garden_set = set(garden)
meadow_set = set(meadow)


# выведите на консоль все виды цветов
sed = garden_set|meadow_set
print(sed)

# выведите на консоль те, которые растут и там и там
sad = garden_set&meadow_set
print(sad)

# выведите на консоль те, которые растут в саду, но не растут на лугу
mad = garden_set-meadow_set
print(mad)

# выведите на консоль те, которые растут на лугу, но не растут в саду
fat = meadow_set-garden_set
print(fat)


