import enum

class StrEnum(str, enum.Enum): pass

class MediaType(StrEnum):
    _generate_next_value_ = lambda name, *_: name.lower()

    APPLICATION = enum.auto()
    AUDIO       = enum.auto()
    FONT        = enum.auto()
    EXAMPLE     = enum.auto()
    IMAGE       = enum.auto()
    MESSAGE     = enum.auto()
    MODEL       = enum.auto()
    MULTIPART   = enum.auto()
    TEXT        = enum.auto()
    VIDEO       = enum.auto()

class MediaSuffix(StrEnum):
    _generate_next_value_ = lambda name, *_: name.lower().replace('_', '-')

    XML         = enum.auto()
    JSON        = enum.auto()
    BER         = enum.auto()
    CBOR        = enum.auto()
    DER         = enum.auto()
    FASTINFOSET = enum.auto()
    WBXML       = enum.auto()
    ZIP         = enum.auto()
    TLV         = enum.auto()
    JSON_SEQ    = enum.auto()
    SQLITE3     = enum.auto()
    JWT         = enum.auto()
    GZIP        = enum.auto()
    CBOR_SEQ    = enum.auto()
    ZSTD        = enum.auto()
