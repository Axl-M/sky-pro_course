PATH = 'candidates.json'
PROJECT_NAME = 'Все о Flask'
PROJECT_DESCRIPTION = "Рецепты, руководства и примеры по Flask"


class Config:
    """
    Альтернативный вариант заполнения конфига
    """
    DEBUG = True
    STATICFOLDER = 'static'
    TEMPLATESFOLDER = 'templates'
    PATH = 'data.json'