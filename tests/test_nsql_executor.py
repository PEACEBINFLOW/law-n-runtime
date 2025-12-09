from lnre.nsql_executor import NsqlExecutor


def test_nsql_executor_logs_query():
    state = {}
    executor = NsqlExecutor(state)

    result = executor.exec("SELECT 1")
    assert result["status"] == "OK"
    assert "nsql_log" in state
