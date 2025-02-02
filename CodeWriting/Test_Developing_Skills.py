import json
import time
from langchain_community.llms import Ollama

deepseekr1_32b = "deepseek-r1:32b"
deepseekr1_70b = "deepseek-r1:70b"

message = """Привет!
Напиши мне реализацию регулярных выражений на C# с нуля пожалуйста!

Реализация должна работать следующим образом:

Есть класс Regular.

У него есть статичный метод Parse, который принимает строку string с регулярным выражением, парсит его и возвращает инстанс Regular, содержащий внутри себя конечный автомат, описывающий это регулярное выражение.

У инстанса есть два метода:

```cs
Match Match( string str );

Match Find( string str );
```

здесь тип Match - это класс, содержащий флаг успешного поиска (success) и список начальных и конечных индексов найденных подстрок.

Метод Match выполняет проверку что строка str соответствует регулярному выражению. 

Метод Find выполняет поиск всех подстрок, соответствующих регулярному выражению. 

Регулярные выражения должны поддерживать следующие элементы:
. - подстановка любого символа
* - повторение символа 0 или более раз
? - повторение символа 0 или 1 раз
+ - повторение символа 1 или более раз
[ ] - список символов
( ) - группировка
| - выбор одного из авриантов


Пожалуйста, учти следующие условия:
- Не оставляй пустые методы-заглушки с комментариями вида "добавить реализацию".
- При реализации метода Parse метод должен полноценно разбирать входную строку с регулярным выражением и строить на её основе полноценную стейт-машину.
- Методы Match и Find должны полноценно выполнять эту стейт машину (можно сделать общий метод для логики исполнения стейт-машины)
- При реализации не используй готовые библиотеки.

"""


def main(model):
    time_start = time.time()
    print(f"Start loading at {time_start}")
    llm = Ollama(model=model)
    time_end = time.time()
    print(f"End loading at {time_end}")
    loading_time = time_end - time_start
    print(f"Model loading time: {loading_time}")

    print()

    time_start = time.time()
    print(f"Start excution at {time_start}")
    response = llm.invoke(message)
    time_end = time.time()
    print(f"end excution at {time_end}")
    excution_time = time_end - time_start
    print(f"Model answering time: {excution_time}")

    print()
    print("Result:")
    print()

    print(response)

    with open("result-3.txt", "w", encoding="utf8") as f:
        f.writelines([
            f"model loading time: {loading_time}",
            f"model execution time: {excution_time}",
            "", "", "",
            "Question:", "",
            message,
            "", "", "",
            "Result:", "",
            response
        ])


if __name__ == "__main__":
    main(deepseekr1_32b)
