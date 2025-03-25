from _typeshed import Incomplete

from networkx.utils.backends import _dispatchable

@_dispatchable
def projected_graph(B, nodes, multigraph: bool = False): ...
@_dispatchable
def weighted_projected_graph(B, nodes, ratio: bool = False): ...
@_dispatchable
def collaboration_weighted_projected_graph(B, nodes): ...
@_dispatchable
def overlap_weighted_projected_graph(B, nodes, jaccard: bool = True): ...
@_dispatchable
def generic_weighted_projected_graph(B, nodes, weight_function: Incomplete | None = None): ...
