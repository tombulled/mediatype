import pydantic

import typing

from . import enums

class BaseModel(pydantic.BaseModel): pass

class MimeType(BaseModel):
    type:       str
    subtype:    str
    suffix:     typing.Optional[str]
    parameters: typing.Dict[str, str]

    def __str__(self, parameters = True) -> str:
        return ''.join \
        (
            (
                f'{self.type}/',
                f'{self.subtype}',
                f'+{self.suffix}' if self.suffix else '',
                ';' if parameters and self.parameters else '',
                ';'.join \
                (
                    f'{key}="{value}"'
                    for key, value in self.parameters.items()
                ) if parameters and self.parameters else '',
            ),
        )
