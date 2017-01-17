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
    return max(data, key=lambda e: e['SeatsCount'])


def get_smallest_bar(data):
    return min(data, key=lambda e: e['SeatsCount'])


def get_closest_bar(data, longitude, latitude):
    return min(data, key=lambda e: get_distance(latitude, longitude, e['geoData']['coordinates'][1], e['geoData']['coordinates'][0]))


if __name__ == '__main__':
    filepath = input('Укажите путь к файлу с данными: ')
    bar_data = load_data(filepath)
    if bar_data is None:
        print('Кажется, с вашим файлом что-то не так, попробуйте еще раз')
        
    else:
        biggest_bar = get_biggest_bar(bar_data)
        print('Самый вместительный московский бар: {}, {} посадочных мест'.format(biggest_bar['Name'], biggest_bar['SeatsCount']))
        
        smallest_bar = get_smallest_bar(bar_data)
        print('Самый тесный московский бар: {}, {} посадочных мест'.format(smallest_bar['Name'], smallest_bar['SeatsCount']))
        
        coordinates = get_coordinates()
        if coordinates is None:
            print('Неверно указана широта или долгота, попробуйте еще раз')
        else:
            closest_bar = get_closest_bar(bar_data, coordinates[0], coordinates[1])
            print('Ваши координаты: [{}, {}]'.format(coordinates[0], coordinates[1]))
            print('Ближайший от вас московский бар: {}, его координаты: {}'.format(closest_bar['Name'], str(closest_bar['geoData']['coordinates'])))
