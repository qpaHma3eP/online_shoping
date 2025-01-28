# Синхронный
import time

def red_light():
    print("Red Light: STOP")
    time.sleep(5)  # Светится 5 секунды

def yellow_light():
    print("Yellow Light: CAUTION")
    time.sleep(1)  # Светится 1 секунду

def green_light():
    print("Green Light: GO")
    time.sleep(5)  # Светится 5 секунды

def traffic_light():
    while True:
        red_light()
        yellow_light()
        green_light()

# Запуск синхронной модели
traffic_light()


# # Асинхронный
# import threading
# import time
#
# def red_light_async():
#     while True:
#         print("Red Light: STOP")
#         time.sleep(2)
#
# def yellow_light_async():
#     while True:
#         print("Yellow Light: CAUTION")
#         time.sleep(2)
#
# def green_light_async():
#     while True:
#         print("Green Light: GO")
#         time.sleep(2)
#
# def traffic_light_async():
#     red_thread = threading.Thread(target=red_light_async)
#     yellow_thread = threading.Thread(target=yellow_light_async)
#     green_thread = threading.Thread(target=green_light_async)
#
#     red_thread.start()
#     yellow_thread.start()
#     green_thread.start()
#
# # Запуск асинхронной модели
# traffic_light_async()


# # Многопоточный
# import threading
# import time
#
# def red_light_multithread():
#     while True:
#         print("Red Light: STOP")
#         time.sleep(5)
#
# def yellow_light_multithread():
#     while True:
#         print("Yellow Light: CAUTION")
#         time.sleep(1)
#
# def green_light_multithread():
#     while True:
#         print("Green Light: GO")
#         time.sleep(5)
#
# def traffic_light_multithread():
#     threads = []
#     threads.append(threading.Thread(target=red_light_multithread))
#     threads.append(threading.Thread(target=yellow_light_multithread))
#     threads.append(threading.Thread(target=green_light_multithread))
#
#     for thread in threads:
#         thread.start()
#
# # Запуск многопоточной модели
# traffic_light_multithread()


