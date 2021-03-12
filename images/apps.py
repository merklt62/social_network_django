from django.apps import AppConfig


class ImagesConfig(AppConfig):
    name = 'images'

    def ready(self):
        # импортируем файл с описанной ф-цией-подписчиком на сигнал
        import images.signals
