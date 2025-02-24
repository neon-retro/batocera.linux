from collections.abc import Iterator
from contextlib import contextmanager
from os import PathLike
from typing import Literal, NamedTuple, overload

from .eventio_async import EventIO

class AbsInfo(NamedTuple):
    value: int
    min: int
    max: int
    fuzz: int
    flat: int
    resolution: int

class KbdInfo(NamedTuple):
    repeat: int
    delay: int

class DeviceInfo(NamedTuple):
    bustype: int
    vendor: int
    product: int
    version: int


class InputDevice(EventIO):
    path: str | bytes
    fd: int
    info: DeviceInfo
    name: str
    phys: str
    uniq: str
    def __init__(self, dev: str | bytes | PathLike) -> None: ...
    def __del__(self) -> None: ...
    @overload
    def capabilities(self, verbose: Literal[False] = ..., absinfo: Literal[True] = ...) -> dict[int, list[int | tuple[int, AbsInfo]]]: ...
    @overload
    def capabilities(self, verbose: Literal[False], absinfo: Literal[False]) -> dict[int, list[int]]: ...
    @overload
    def capabilities(self, verbose: Literal[True], absinfo: Literal[True]) -> dict[tuple[str, int], list[tuple[tuple[str, int], AbsInfo]]]: ...
    @overload
    def capabilities(self, verbose: Literal[True], absinfo: Literal[False]) -> dict[tuple[str, int], list[tuple[str, int]]]: ...
    @overload
    def input_props(self, verbose: Literal[False] = ...) -> list[int]: ...
    @overload
    def input_props(self, verbose: Literal[True]) -> list[tuple[str, int]]: ...
    @overload
    def input_props(self, verbose: bool) -> list[int] | list[tuple[str, int]]: ...
    @overload
    def leds(self, verbose: Literal[False] = ...) -> list[int]: ...
    @overload
    def leds(self, verbose: Literal[True]) -> list[tuple[str, int]]: ...
    @overload
    def leds(self, verbose: bool) -> list[int] | list[tuple[str, int]]: ...
    def set_led(self, led_num: int, value: int) -> None: ...
    def __eq__(self, other: object) -> bool: ...
    def __fspath__(self) -> str | bytes: ...
    def close(self) -> None: ...
    def grab(self) -> None: ...
    def ungrab(self) -> None: ...
    @contextmanager
    def grab_context(self) -> Iterator[None]: ...
    def upload_effect(self, effect: object) -> int: ...
    def erase_effect(self, ff_id: int) -> None: ...
    repeat: KbdInfo
    @overload
    def active_keys(self, verbose: Literal[False] = ...) -> list[int]: ...
    @overload
    def active_keys(self, verbose: Literal[True]) -> list[tuple[str, int]]: ...
    @overload
    def active_keys(self, verbose: bool) -> list[int] | list[tuple[str, int]]: ...
    def absinfo(self, axis_num: int) -> AbsInfo: ...
    def set_absinfo(
        self,
        axis_num: int,
        value: int | None = None,
        min: int | None = None,
        max: int | None = None,
        fuzz: int | None = None,
        flat: int | None = None,
        resolution: int | None = None,
    ) -> None: ...
