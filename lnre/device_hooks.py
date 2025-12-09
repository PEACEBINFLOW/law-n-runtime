from __future__ import annotations

from typing import Any, Protocol


class Device(Protocol):
    def dispatch(self, event: str, payload: Any) -> None:
        ...


class DeviceHooks:
    """
    Bridge between LNRE and external devices defined in law-n-device-profiles.
    """

    def __init__(self) -> None:
        self.devices: dict[str, Device] = {}

    def register(self, name: str, device: Device) -> None:
        self.devices[name] = device

    def emit(self, name: str, event: str, payload: Any) -> None:
        if name in self.devices:
            self.devices[name].dispatch(event, payload)
