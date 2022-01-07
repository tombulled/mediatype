# mediatype
Media Type parsing and creation

## Usage
```python
>>> import mediatype
>>>
>>> mediatype('application/manifest+json')
MediaType(type='application', subtype='manifest', suffix='json', parameters=None)
```

## References
* [IANA - Media Types](https://www.iana.org/assignments/media-types/media-types.xhtml)
* [RFC-6838 - Media Type Specifications and Registration Procedures](https://www.rfc-editor.org/rfc/rfc6838.html)
* [Mozilla - MIME types (IANA media types)](https://developer.mozilla.org/en-US/docs/Web/HTTP/Basics_of_HTTP/MIME_types)
* [Wikipedia - Media type](https://en.wikipedia.org/wiki/Media_type)
