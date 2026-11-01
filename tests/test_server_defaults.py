"""Regression checks for the local-only Flask entry point.

The repository's test suite uses a bundled Flask stub. These tests verify
configuration decisions, not real cookie signing or network reachability.
"""
from localspiral.main import create_app, main


def test_each_app_gets_an_unpredictable_session_secret():
    first = create_app()
    second = create_app()

    assert isinstance(first.secret_key, str)
    assert len(first.secret_key) == 64  # 32 random bytes, hex encoded
    assert first.secret_key != second.secret_key
    assert first.secret_key != 'dev'


def test_entry_point_disables_debug_and_binds_loopback(monkeypatch):
    calls = []

    class RecordingApp:
        def run(self, **kwargs):
            calls.append(kwargs)

    monkeypatch.setattr('localspiral.main.create_app', RecordingApp)
    main()

    assert calls == [{'host': '127.0.0.1', 'debug': False}]
