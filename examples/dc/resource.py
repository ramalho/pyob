"""
Media resource description class with subset of the Dubin Core fields.

Default field values:

    >>> r = Resource()
    >>> r
    Resource(
        identifier = '0000000000000',
        title = '<untitled>',
        creators = [],
        date = '',
        type = '',
        description = '',
        language = '',
        subjects = [],
    )

A complete resource record:

    >>> description = 'A hands-on guide to idiomatic Python code.'
    >>> book = Resource('9781491946008', 'Fluent Python', 
    ...   ['Luciano Ramalho'], '2015-08-20', 'book', description,
    ...   'EN', ['computer programming', 'Python'])
    >>> book
    Resource(
        identifier = '9781491946008',
        title = 'Fluent Python',
        creators = ['Luciano Ramalho'],
        date = '2015-08-20',
        type = 'book',
        description = 'A hands-on guide to idiomatic Python code.',
        language = 'EN',
        subjects = ['computer programming', 'Python'],
    )

"""

from dataclasses import dataclass, field, fields
from typing import List

@dataclass
class Resource:
    """Media resource description."""
    identifier: str = "0" * 13
    title: str = "<untitled>"
    creators: List[str] = field(default_factory=list)
    date: str = ""
    type: str = ""
    description: str = ""
    language: str = ""
    subjects: List[str] = field(default_factory=list)


    def __repr__(self):
        cls = self.__class__
        cls_name = cls.__name__
        res = [f'{cls_name}(']
        for field in fields(cls):
            value = getattr(self, field.name)
            res.append(f'    {field.name} = {value!r},')
        res.append(f')')
        return '\n'.join(res)
