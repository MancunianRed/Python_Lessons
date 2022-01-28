#  EXIF: Задание 2 - 150 баллов
import exifread
from geopy.geocoders import Nominatim


# выводит на экран адрес где было сделано фото
def geo_locator(data):
    geolocator = Nominatim(user_agent="geo")
    location = geolocator.reverse(f"{data[0]}, {data[1]}")
    print(location.address)


# возвращает обьект с тэгами в виде словаря
def get_photo_info(path):
    with open(path, "rb") as reader:
        tags = exifread.process_file(reader)
        return tags


# возвращает значение ключа в словаре, если такой ключ существует
def if_exist(tags, key):
    if key in tags:
        return tags[key]


# возвращает широту или долготу в формате десятичных градусов
def convert_to_gps_data(value):
    d = float(value.values[0].num) / float(value.values[0].den)
    m = float(value.values[1].num) / float(value.values[1].den)
    s = float(value.values[2].num) / float(value.values[2].den)
    return d + (m / 60.0) + (s / 3600.0)


# возвращает значения широты и долготы с учетом
def get_lat_lon(tags):
    lat = None
    lon = None
    gps_lat = if_exist(tags, "GPS GPSLatitude")
    gps_lat_ref = if_exist(tags, "GPS GPSLatitudeRef")
    gps_lon = if_exist(tags, "GPS GPSLongitude")
    gps_lon_ref = if_exist(tags, "GPS GPSLongitudeRef")
    if gps_lat and gps_lat_ref and gps_lon and gps_lon_ref:
        lat = convert_to_gps_data(gps_lat)
        lon = convert_to_gps_data(gps_lon)
        if gps_lat_ref.values[0] != "N":
            lat = 0 - lat
        if gps_lon_ref.values[0] != "E":
            lon = 0 - lon
    print(lat)
    print(lon)
    return lat, lon


if __name__ == "__main__":
    path = "C:\\Users\\proic\\Desktop\\Python\\Part 2\\15 - " \
           "EXIF\\swan\\swan.jpg"
    data = get_lat_lon(get_photo_info(path))
    geo_locator(data)