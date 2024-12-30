from django.shortcuts import render, redirect

# Create your views here.

user_name = ''

horoscope_spisok = {
    'aries': {
        'sign_name': 'Овен',
        'prediction': 'Начни день с улыбки. Пусть она станет твоим первым шагом к успеху!'
    },
    'taurus': {
        'sign_name': 'Телец',
        'prediction': 'Помни, что каждое утро – это новый шанс. Используй его на полную!'
    },
    'gemini': {
        'sign_name': 'Близнецы',
        'prediction': 'Не бойся ошибок. Они – часть пути к совершенству.'
    },
    'cancer': {
        'sign_name': 'Рак',
        'prediction': 'Сегодня ты можешь стать лучше, чем вчера. Стремись к прогрессу!'
    },
    'leo': {
        'sign_name': 'Лев',
        'prediction': 'Будь открыт новым возможностям. Иногда самые лучшие вещи приходят неожиданно.'
    },
    'virgo': {
        'sign_name': 'Дева',
        'prediction': 'Поставь цель и двигайся к ней шаг за шагом. Маленькие победы ведут к большим достижениям.'
    },
    'libra': {
        'sign_name': 'Весы',
        'prediction': 'Заботься о себе. Здоровье и благополучие – основа успеха.'
    },
    'scorpio': {
        'sign_name': 'Скорпион',
        'prediction': 'Окружай себя позитивом. Хорошее настроение притягивает хорошие события.'
    },
    'sagittarius': {
        'sign_name': 'Стрелец',
        'prediction': 'Не забывай о благодарности. Цени то, что имеешь, и мир ответит тебе взаимностью.'
    },
    'capricorn': {
        'sign_name': 'Козерог',
        'prediction': 'Доверяй своим инстинктам. Ты умнее, чем думаешь.'
    },
    'aquarius': {
        'sign_name': 'Водолей',
        'prediction': 'Проявляй терпение. Все великое требует времени.'
    },
    'pisces': {
        'sign_name': 'Рыбы',
        'prediction': 'Живи настоящим моментом. Наслаждайся каждым мгновением дня!'
    }
}


def flowers(request, color):
    if color == 'pink-bouquet':
        return render(request, 'flowers.html', {'image': '/static/src/image1.png', 'name': user_name})
    elif color == 'violet-bouquet':
        return render(request, 'flowers.html', {'image': '/static/src/image2.png', 'name': user_name})
    elif color == 'blue-bouquet':
        return render(request, 'flowers.html', {'image': '/static/src/image3.png', 'name': user_name})


def horoscope(request, sign):
    sign_detail = horoscope_spisok.get(sign)

    context = {
        'sign': sign_detail.get('sign_name'),
        'prediction': sign_detail.get('prediction'),
        'name': user_name
    }

    return render(request, 'horoscope.html', context)


def main(request, name):
    context = {
        'name': name,
    }

    if request.method == 'POST':
        sign = request.POST.get("select-horoscope")
        color = request.POST.get("select-color")

        if sign:
            return redirect(f'/horoscope/{sign}')
        elif color:
            return redirect(f'/flowers/{color}')

    return render(request, 'main.html', context)


def entry(request):
    if request.method == 'POST':
        global user_name
        user_name = request.POST.get("name")

        return redirect(f'/main/{user_name}')
    return render(request, 'entry.html', {})


def dog(request):
    return render(request, 'dog.html', {'name': user_name})
