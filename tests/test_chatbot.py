"""Kiểm thử phần không cần mạng của bot chat Claude."""
import pytest

pytest.importorskip("anthropic")  # chỉ có khi cài chatbot/requirements.txt

from chatbot.main import parse_ids, split_text, trim


def test_parse_ids():
    assert parse_ids("123, -100456,") == {123, -100456}
    assert parse_ids("") == set()


def test_split_text_respects_limit():
    text = "\n".join(f"dòng {i} " + "x" * 50 for i in range(200))
    parts = split_text(text, limit=500)
    assert all(len(p) <= 500 for p in parts)
    assert "".join(parts).replace("\n", "") == text.replace("\n", "")


def test_trim_cuts_from_front_at_user_turn():
    h = []
    for i in range(5):
        h += [{"role": "user", "content": f"q{i}"}, {"role": "assistant", "content": [{"type": "text", "text": f"a{i}"}]}]
    trim(h, 2)
    assert [m["content"] for m in h if m["role"] == "user"] == ["q3", "q4"]
    assert h[0]["role"] == "user"
