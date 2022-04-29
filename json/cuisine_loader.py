import json
from datetime import datetime
from time import ctime

with open('raw.json', 'r', encoding='utf-8') as file:
    data = json.load(file)

restaurants = list()
grades = list()
count_grade = 0

for index, content in enumerate(data):
    result = {
        'model': "restaurant_api.Restaurant",
        'pk': index + 1,
        'fields': {
            'name': content['name'] if content['name'] != '' else content['address']['street'] + content['address']['building'],
            'restaurant_uniq_id': int(content['restaurant_id']),
            'building': content['address']['building'],
            'longitude': float(content['address']['coord'][0]) if bool(content['address']['coord']) else 0,
            'latitude': float(content['address']['coord'][1]) if bool(content['address']['coord']) else 0,
            'street': content['address']['street'],
            'zipcode': int(content['address']['zipcode']) if content['address']['zipcode'] != '' else 0,
            'borough': content['borough'],
            'cuisine': content['cuisine'],
        }
    }
    restaurants.append(result)


    if bool(content['grades']):
        for i, grade in enumerate(content['grades']):
            count_grade += 1
            t = datetime.strptime(ctime(grade['date']['$date'] // 1000), "%a %b %d %H:%M:%S %Y")
            result_grade = {
                'model': 'restaurant_api.Grade',
                'pk': count_grade,
                'fields': {
                    'fk_grade': str(index + 1),
                    'date': f'{t.year}-{t.month}-{t.day} {t.hour:02d}:{t.minute:02d}:{t.second:02d}',
                    'grade': grade['grade'],
                    'score': grade['score']
                }
            }
            grades.append(result_grade)


with open('data_restaurants.json', 'w') as file:
    json.dump(restaurants, file, indent=4)
    print('save is done')

with open('data_grades.json', 'w') as file:
    json.dump(grades, file, indent=4)
    print('save is done')
