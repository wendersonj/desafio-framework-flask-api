from re import sub

from pydantic import BaseModel


def camel_case(s):
    #https://www.w3resource.com/python-exercises/string/python-data-type-string-exercise-96.php
    s = sub(r"(_|-)+", " ", s).title().replace(" ", "")
    return ''.join([s[0].lower(), s[1:]])


class CamelModel(BaseModel):
    class Config:
        alias_generator = camel_case
        allow_population_by_field_name = True
