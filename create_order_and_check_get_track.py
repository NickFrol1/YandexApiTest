# Никита Фролов, EARTH, 7 поток — Финальный проект. Инженер по тестированию плюс

import sender_stand_request


def test_create_order_and_check_get_track():
    response_create = sender_stand_request.create_order()
    track = response_create.json()["track"]
    response_get = sender_stand_request.get_order_by_track(track)
    assert response_get.status_code == 200
