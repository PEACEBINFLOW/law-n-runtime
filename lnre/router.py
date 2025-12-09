from __future__ import annotations

from typing import Any, Dict


class ChannelRouter:
    """
    Manages logical channels and routing between LAW-N nodes.
    """

    def __init__(self) -> None:
        self.channels: Dict[str, Any] = {}

    def open_channel(self, name: str) -> None:
        self.channels.setdefault(name, {"open": True, "buffer": []})

    def close_channel(self, name: str) -> None:
        if name in self.channels:
            self.channels[name]["open"] = False

    def send(self, name: str, payload: Any) -> None:
        if name not in self.channels:
            self.open_channel(name)
        self.channels[name]["buffer"].append(payload)
