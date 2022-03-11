# mediatype
Media Type (aka MIME Type) parsing and creation

## Installation
```console
pip install mediatype
```

## Usage
```python
>>> import mediatype
```

### Parsing
```python
>>> media_type = mediatype.parse('application/manifest+json')
>>>
>>> media_type
MediaType(
    type='application',
    subtype='manifest',
    suffix='json',
    parameters=None
)
>>>
>>> str(media_type)
'application/manifest+json'
```

### Creation
```python
>>> media_type = mediatype.MediaType(
    type='application',
    subtype='manifest',
    suffix='json',
    parameters=None
)
>>>
>>> str(media_type)
'application/manifest+json'
```

## References
* [IANA - Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml)
* [RFC-6838 - Media Type Specifications and Registration Procedures](https://www.rfc-editor.org/rfc/rfc6838.html)
* [Mozilla - MIME types (IANA media types)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)
* [Wikipedia - Media type](https://en.wikipedia.org/wiki/Media_type)
