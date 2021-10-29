# mime
Mime Type parsing and creation

## Usage
```python
>>> import mime
>>>
>>> mime_type = mime.parse('application/json+json-seq')
>>>
>>> mime_type
MimeType(type='application', subtype='json', suffix='json-seq', parameters=None)
>>>
```
