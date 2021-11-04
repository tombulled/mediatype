from .parsers import Parser
from .enums   import MediaTypeType, MediaTypeSubtype, MediaTypeSuffix
from .models  import MediaType

parse = Parser.parse

import sys
import types

class MimeTypeModule(types.ModuleType):
    @staticmethod
    def __call__(mediatype: str) -> MediaType:
        return MediaType(**Parser.parse(mediatype))

sys.modules[__name__].__class__ = MimeTypeModule
