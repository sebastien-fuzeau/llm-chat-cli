from src.memory import ChatMemory


def test_seed_adds_system():
    m = ChatMemory(system_prompt="sys")
    m.seed()
    assert m.messages[0]["role"] == "system"
    assert m.messages[0]["content"] == "sys"


def test_clear_to_system_keeps_only_system():
    m = ChatMemory(system_prompt="sys")
    m.seed()
    m.add_user("u")
    m.add_assistant("a")
    m.clear_to_system()
    assert len(m.messages) == 1
    assert m.messages[0]["role"] == "system"
