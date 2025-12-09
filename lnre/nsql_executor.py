from __future__ import annotations

from typing import Any, Dict


class NsqlExecutor:
    """
    Executes N-SQL statements inside the runtime.

    This is a stub; in future this will connect to LAW-N N-SQL engine,
    or delegate to law-n-nsql-engine package.
    """

    def __init__(self, state: Dict[str, Any]) -> None:
        self.state = state

    def exec(self, query: str) -> Any:
        # TODO: connect to NSQL engine
        # For now, just log the query into runtime state.
        self.state.setdefault("nsql_log", []).append(query)
        return {"status": "OK", "echo": query}
