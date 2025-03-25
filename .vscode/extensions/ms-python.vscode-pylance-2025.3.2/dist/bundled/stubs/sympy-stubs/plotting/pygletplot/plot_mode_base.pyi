from typing import Any, Callable

from sympy.plotting.pygletplot.plot_mode import PlotMode

class PlotModeBase(PlotMode):
    intervals = ...
    aliases = ...
    is_default = ...
    styles = ...
    style_override = ...
    default_wireframe_color = ...
    default_solid_color = ...
    default_rot_preset = ...
    def __init__(self, *args, bounds_callback=..., **kwargs) -> None: ...
    @staticmethod
    def synchronized(f) -> Callable[..., Any]: ...
    @synchronized
    def push_wireframe(self, function) -> None: ...
    @synchronized
    def push_solid(self, function) -> None: ...
    @synchronized
    def draw(self) -> None: ...

    style = ...
    color = ...
    calculating_verts = ...
    calculating_verts_pos = ...
    calculating_verts_len = ...
    calculating_cverts = ...
    calculating_cverts_pos = ...
    calculating_cverts_len = ...
