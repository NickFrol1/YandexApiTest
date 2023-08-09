import configuration
import data
import requests


def create_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER,
                         json=data.create_test_order_body)


def get_order_by_track(track):
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_BY_TRACK + str(track))
