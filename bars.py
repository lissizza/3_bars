import json
import os
from math import sqrt

def get_distance(user_latitude, user_longitude, bar_latitude, bar_longitude):
    return sqrt((user_latitude - float(bar_latitude))**2 + (user_longitude - float(bar_longitude))**2)

def get_coordinates():
    coordinates = input("Введите вашу долготу и широту через пробел: ")
    try:
        longitude, latitude = map(float, coordinates.split())
        return (longitude, latitude)
    except Exception as e:
        return None
    
def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath) as data_file:    
        return json.load(data_file)
    
def get_biggest_bar(data):
    biggest_bar = max(data, key=lambda e: e['SeatsCount'])
    return (biggest_bar['Name'], biggest_bar['SeatsCount'])


def get_smallest_bar(data):
    smallest_bar = min(data, key=lambda e: e['SeatsCount'])
    return (smallest_bar['Name'], smallest_bar['SeatsCount'])

def get_closest_bar(data, longitude, latitude):
    closest_bar = min(data, key=lambda e: get_distance(latitude, longitude, e['geoData']['coordinates'][1], e['geoData']['coordinates'][0]))
    return (closest_bar['Name'], str(closest_bar['geoData']['coordinates']))

if __name__ == '__main__':
    filepath = input('Укажите путь к файлу с данными: ')
    bar_data = load_data(filepath)
    if bar_data is None:
        print('Кажется, с вашим файлом что-то не так, попробуйте еще раз')
        
    else:
        print('Самый вместительный московский бар: %s, %s посадочных мест' % get_biggest_bar(bar_data))
        print('Самый тесный московский бар: %s, %s посадочных мест' % get_smallest_bar(bar_data))
        
        coordinates = get_coordinates()
        if coordinates is None:
            print('Неверно указана широта или долгота, попробуйте еще раз')
        else:
            print('Ваши координаты: [%s, %s]' % coordinates)
            print('Ближайший от вас московский бар: %s, его координаты: %s' % get_closest_bar(bar_data, coordinates[0], coordinates[1]))
