from _typeshed import FileDescriptorOrPath, Incomplete, StrPath
from collections.abc import Iterator
from typing import Any

from pygments.lexer import Lexer, LexerMeta

def get_all_lexers(plugins: bool = True) -> Iterator[tuple[str, tuple[str, ...], tuple[str, ...], tuple[str, ...]]]: ...
def find_lexer_class(name: str) -> LexerMeta | None: ...
def find_lexer_class_by_name(_alias: str) -> LexerMeta: ...
def get_lexer_by_name(_alias: str, **options: Any) -> Lexer: ...
def load_lexer_from_file(filename: FileDescriptorOrPath, lexername: str = "CustomLexer", **options: Any) -> Lexer: ...
def find_lexer_class_for_filename(_fn: StrPath, code: str | bytes | None = None) -> LexerMeta | None: ...
def get_lexer_for_filename(_fn: StrPath, code: str | bytes | None = None, **options: Any) -> Lexer: ...
def get_lexer_for_mimetype(_mime: str, **options: Any) -> Lexer: ...
def guess_lexer_for_filename(_fn: StrPath, _text: str, **options: Any) -> Lexer: ...
def guess_lexer(_text: str | bytes, **options: Any) -> Lexer: ...

# Having every lexer class here doesn't seem to be worth it
def __getattr__(name: str) -> Incomplete: ...
