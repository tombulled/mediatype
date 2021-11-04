# mediatype
Media Type parsing and creation

## Usage
```python
>>> import mediatype
>>>
>>> mime = mediatype.parse('application/json+json-seq')
>>>
>>> mime
MimeType(type='application', subtype='json', suffix='json-seq', parameters=None)
>>>
```

## References
* [IANA - Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml)
* [RFC-6838 - Media Type Specifications and Registration Procedures](https://www.rfc-editor.org/rfc/rfc6838.html)
* [Mozilla - MIME types (IANA media types)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)
* [Wikipedia - Media type](https://en.wikipedia.org/wiki/Media_type)
