# Stubs for marathon.models.container (Python 3.6)
#
# NOTE: This dynamically typed stub was automatically generated by stubgen.

from typing import Any, Optional
from ..exceptions import InvalidChoiceError as InvalidChoiceError
from .base import MarathonObject as MarathonObject

class MarathonContainer(MarathonObject):
    TYPES = ...  # type: Any
    type = ...  # type: Any
    port_mappings = ...  # type: Any
    docker = ...  # type: Any
    volumes = ...  # type: Any
    def __init__(
        self,
        docker: Optional[Any] = ...,
        type: str = ...,
        port_mappings: Optional[Any] = ...,
        volumes: Optional[Any] = ...,
    ) -> None: ...

class MarathonDockerContainer(MarathonObject):
    NETWORK_MODES = ...  # type: Any
    image = ...  # type: Any
    network = ...  # type: Any
    port_mappings = ...  # type: Any
    parameters = ...  # type: Any
    privileged = ...  # type: Any
    force_pull_image = ...  # type: Any
    def __init__(
        self,
        image: Optional[Any] = ...,
        network: Optional[Any] = ...,
        port_mappings: Optional[Any] = ...,
        parameters: Optional[Any] = ...,
        privileged: Optional[Any] = ...,
        force_pull_image: Optional[Any] = ...,
        **kwargs,
    ) -> None: ...

class MarathonContainerPortMapping(MarathonObject):
    PROTOCOLS = ...  # type: Any
    name = ...  # type: Any
    container_port = ...  # type: Any
    host_port = ...  # type: Any
    service_port = ...  # type: Any
    protocol = ...  # type: Any
    labels = ...  # type: Any
    def __init__(
        self,
        name: Optional[Any] = ...,
        container_port: Optional[Any] = ...,
        host_port: int = ...,
        service_port: Optional[Any] = ...,
        protocol: str = ...,
        labels: Optional[Any] = ...,
    ) -> None: ...

class MarathonContainerVolume(MarathonObject):
    MODES = ...  # type: Any
    container_path = ...  # type: Any
    host_path = ...  # type: Any
    mode = ...  # type: Any
    persistent = ...  # type: Any
    external = ...  # type: Any
    def __init__(
        self,
        container_path: Optional[Any] = ...,
        host_path: Optional[Any] = ...,
        mode: str = ...,
        persistent: Optional[Any] = ...,
        external: Optional[Any] = ...,
    ) -> None: ...
