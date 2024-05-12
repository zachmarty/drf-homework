import re
from typing import Any

from django.forms import ValidationError




class LessonValidator:

    def __init__(self, field) -> None:
        self.field = field

    def __call__(self, value, *args: Any, **kwds: Any) -> Any:
        reg = re.compile(r'https:\/\/www.youtube.com')
        try:
            tmp_val = value[self.field]
        except:
            raise ValidationError("Link must be attached")
        if type(tmp_val) == None:
            raise ValidationError("Link cannot be blank") #Я это добавил, потому что у меня в модели ссылка blank = true, потом перепишу модель
        if not(bool(reg.match(tmp_val))):
            raise ValidationError("Video is not from youtube")