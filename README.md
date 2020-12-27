# Hanoi

MO kursach by Zavodnoi Apelsin Team 

Структура:
| File        | Description  |
| ------------- |:-------------:| 
| .github/workflows | скрипты CI/CD для прогона тестов парсера|
|doc| документация и заметки|
|good_test|пройденные тесты парсером|
|new|боевые тесты для решателя|
|solver_out|вывод решателя|
|solver_test|тесты решателя|
|tests_file|тесты парсера|
|CheckOrder.py|проверка решения|
|FrameStewart.py|not used|
|GUI_module.py|интерфейс|
|Hanoi.py|интерфейс|
|InputTXT.py|парсер|
|app.py|запускатор интерфейса (2 потока)|
|hanoi_console.py|wrapper над бэкендом|
|hanoi_graph_mod.py|улучшенная версия hanoi_graph|
|hanoi_graph_order.py|проверка готового пути|
|hanoi_gui.py|wrapper над GUI|
|hanoi_test_order.py|прогон тестов|
|serega_hanoi.py|разбитие над подбашни|
|stopwatch.py|таймер выполнения|
|test_results.txt|вывод автотестов|


## requirements

1. NetworkX (graph)
2. pyQt5 (GUI)
3. matplotlib (graph plots)
