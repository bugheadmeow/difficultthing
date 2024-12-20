import doctest

class KpopAlbum:
    def __init__(self, title: str, group_name: str):
        """
        Создание и подготовка объекта "K-pop Альбом"

        :param title: Название альбома
        :param group_name: Название группы, выпустившей альбом

        Примеры:
        >>> album = KpopAlbum("The War", "EXO")
        """
        if not isinstance(title, str):
            raise TypeError("Название альбома должно быть строкой")
        if not isinstance(group_name, str):
            raise TypeError("Название группы должно быть строкой")

    self.title = title
    self.group_name = group_name

def add_track(self, track_name: str) -> None:
    """
    Добавление трека в альбом.
    :param track_name: Название трека
    :raises TypeError: Если название трека не является строкой.
    Примеры:
    >>> album = KpopAlbum("The War", "EXO")
    >>> album.add_track("Ko Ko Bop")
    """
    if not isinstance(track_name, str):
        raise TypeError("Название трека должно быть строкой")
    self.tracks.append(track_name)

def list_tracks(self) -> list[str]:
    """
    Возвращает список треков альбома.
    :return: Список треков
    Примеры:
    >>> album = KpopAlbum("The War", "EXO")
    >>> album.add_track("Ko Ko Bop")
    >>> album.list_tracks()
    ['Ko Ko Bop']
    """
    return self.tracks

def play_track(self, track_name: str) -> str:
    """
    Воспроизведение трека из альбома.

    :param track_name: Название трека для воспроизведения
    :return: Сообщение о воспроизведении трека
    :raises ValueError: Если трек не найден в альбоме.

    Примеры:
    >>> album = KpopAlbum("The War", "EXO")
    >>> album.add_track("Ko Ko Bop")
    >>> album.play_track("Ko Ko Bop")
    'Playing: Ko Ko Bop by EXO'
    """
    if track_name not in self.tracks:
        raise ValueError(f"Трек '{track_name}' не найден в альбоме")
    return f"Playing: {track_name} by {self.group_name}"

if __name__ == "__main__":
    doctest.testmod()