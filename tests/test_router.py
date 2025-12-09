from lnre.router import ChannelRouter


def test_channel_router_basic():
    router = ChannelRouter()
    router.send("main", {"msg": "hello"})
    assert "main" in router.channels
    assert len(router.channels["main"]["buffer"]) == 1
