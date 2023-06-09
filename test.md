# Тестирование

Проверять "работоспособность" нашей машины будем вручную. Написание отдельной модели для проверки на адекватность слишком трудозатратный процесс требующий много ресурсов.

При обчении модели важно следить за параметром потерь, он же ```loss```. 
<img width="740" alt="Снимок экрана 2023-06-08 в 17 41 56" src="https://github.com/hchgssarwyh/ai_fiction/assets/90518791/456554bb-ce52-46b0-bcc1-2347a67d68a0">

Чем ближе loss к 0 тем более обученной считается модель. Однако нельзя допускать переобчения, ведь тогда модель не будет генерировать новых строк и будет просто цитировать старые. Меняя парметр ```temp = n ``` (0 < n < 1) можем настраивать сулчайность выдаваемого текста. Важно найти баланс между несвязным текстом (что плохо) и полной цитирцемостью (что тоже плохо, так как нам важно генерировать новые строчки)

### Тест_hokku_n=0.1
<img width="395" alt="Снимок экрана 2023-06-08 в 17 16 39" src="https://github.com/hchgssarwyh/ai_fiction/assets/90518791/955c32a0-a2a0-488e-b815-fb35b8da963e">


Пример построчного цитирования, так быть не должно.

### Тест_hokku_n=0.9
<img width="425" alt="Снимок экрана 2023-06-08 в 17 19 37" src="https://github.com/hchgssarwyh/ai_fiction/assets/90518791/5737ecd7-faef-4223-aed9-b839334e768f">

При слишком большом ```temp = 0.9 ``` получаем мало связанный текст.


### Тест_hokku_n=0.4
<img width="438" alt="Снимок экрана 2023-06-08 в 17 29 58" src="https://github.com/hchgssarwyh/ai_fiction/assets/90518791/3353781d-bcb9-4020-b8e3-3ec39e743608">

Получаем приемлимый результат при котором сохраняется целостность текста и не наблюдается построчная цитируемость. Можно считать успехом для данного датасета

___

##  Вывод
Качество полученного текста зависит от:
- введенных параметров
- качестве и размера датасета для обучения
- времени обучения
