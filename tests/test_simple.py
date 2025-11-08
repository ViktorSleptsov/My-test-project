import pytest

class TestSimple:
    def test_always_passes(self):
        """Этот тест всегда проходит"""
        assert 1 + 1 == 2
    
    def test_string_operations(self):
        """Тест строковых операций"""
        assert "hello".upper() == "HELLO"
        assert " world".strip() == "world"
    
    def test_list_operations(self):
        """Тест операций со списками"""
        numbers = [1, 2, 3]
        assert len(numbers) == 3
        assert sum(numbers) == 6