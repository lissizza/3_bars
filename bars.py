# -*- coding: utf-8 -*-
import json
from math import sqrt

def get_distance(lt, lg, x, y):
    return sqrt((lt - float(x))**2 + (lg - float(y))**2)

def load_data(filepath):
    with open(filepath) as data_file:    
        data = json.load(data_file)
    
    return data


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
    data = load_data('data.json')
    print('Самый вместительный московский бар: %s, %s посадочных мест' % get_biggest_bar(data))
    print('Самый тесный московский бар: %s, %s посадочных мест' % get_smallest_bar(data))
    
    while True:
        longitude = input("Введите вашу долготу: ")
        try:
            longitude = float(longitude)
            break
        except Exception as e:
            print("Ой, что-то не так с вашей долготой, попробуйте еще раз!")
    
    while True:
        latitude = input("Введите вашу широту: ")
        try:
            latitude = float(latitude)
            break
        except Exception as e:
            print("Ой, что-то не так с вашей широтой, попробуйте еще раз!")    
    
    print('Ваши координаты: [%s, %s]' % (longitude, latitude))
    print('Ближайший от вас московский бар: %s, его координаты: %s' % get_closest_bar(data, longitude, latitude))
