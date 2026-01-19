import pytest
from utils.converters import convert_mbti_to_cognitive_fns


def test_esfj():
    assert convert_mbti_to_cognitive_fns(["E", "S", "F", "J"]) == ["Fe","Si", "Ne", "Ti"]
    assert convert_mbti_to_cognitive_fns(["E", "S", "F", "J"], calculate_shadow_fns=True) == ["Fi", "Se", "Ni", "Te"]


def test_isfj():
    assert convert_mbti_to_cognitive_fns(["I", "S", "F", "J"]) == ["Si", "Fe", "Ti", "Ne"]
    assert convert_mbti_to_cognitive_fns(["I", "S", "F", "J"], calculate_shadow_fns=True) == ["Se", "Fi", "Te", "Ni"]


def test_estj():
    assert convert_mbti_to_cognitive_fns(["E", "S", "T", "J"]) == ["Te", "Si", "Ne", "Fi"]
    assert convert_mbti_to_cognitive_fns(["E", "S", "T", "J"], calculate_shadow_fns=True) == ["Ti", "Se", "Ni", "Fe"]


def test_istj():
    assert convert_mbti_to_cognitive_fns(["I", "S", "T", "J"]) == ["Si", "Te", "Fi", "Ne"]
    assert convert_mbti_to_cognitive_fns(["I", "S", "T", "J"], calculate_shadow_fns=True) == ["Se", "Ti", "Fe", "Ni"]


def test_enfj():
    assert convert_mbti_to_cognitive_fns(["E", "N", "F", "J"]) == ["Fe", "Ni", "Se", "Ti"]
    assert convert_mbti_to_cognitive_fns(["E", "N", "F", "J"], calculate_shadow_fns=True) == ["Fi", "Ne", "Si", "Te"]


def test_infj():
    assert convert_mbti_to_cognitive_fns(["I", "N", "F", "J"]) == ["Ni", "Fe", "Ti", "Se"]
    assert convert_mbti_to_cognitive_fns(["I", "N", "F", "J"], calculate_shadow_fns=True) == ["Ne", "Fi", "Te", "Si"]


def test_enfp():
    assert convert_mbti_to_cognitive_fns(["E", "N", "F", "P"]) == ["Ne", "Fi", "Te", "Si"]
    assert convert_mbti_to_cognitive_fns(["E", "N", "F", "P"], calculate_shadow_fns=True) == ["Ni", "Fe", "Ti", "Se"]


def test_infp():
    assert convert_mbti_to_cognitive_fns(["I", "N", "F", "P"]) == ["Fi", "Ne", "Si", "Te"]
    assert convert_mbti_to_cognitive_fns(["I", "N", "F", "P"], calculate_shadow_fns=True) == ["Fe", "Ni", "Se", "Ti"]


def test_esfp():
    assert convert_mbti_to_cognitive_fns(["E", "S", "F", "P"]) == ["Se", "Fi", "Te", "Ni"]
    assert convert_mbti_to_cognitive_fns(["E", "S", "F", "P"], calculate_shadow_fns=True) == ["Si", "Fe", "Ti", "Ne"]


def test_isfp():
    assert convert_mbti_to_cognitive_fns(["I", "S", "F", "P"]) == ["Fi", "Se", "Ni", "Te"]
    assert convert_mbti_to_cognitive_fns(["I", "S", "F", "P"], calculate_shadow_fns=True) == ["Fe", "Si", "Ne", "Ti"]


def test_estp():
    assert convert_mbti_to_cognitive_fns(["E", "S", "T", "P"]) == ["Se", "Ti", "Fe", "Ni"]
    assert convert_mbti_to_cognitive_fns(["E", "S", "T", "P"], calculate_shadow_fns=True) == ["Si", "Te", "Fi", "Ne"]


def test_istp():
    assert convert_mbti_to_cognitive_fns(["I", "S", "T", "P"]) == ["Ti", "Se", "Ni", "Fe"]
    assert convert_mbti_to_cognitive_fns(["I", "S", "T", "P"], calculate_shadow_fns=True) == ["Te", "Si", "Ne", "Fi"]


def test_entj():
    assert convert_mbti_to_cognitive_fns(["E", "N", "T", "J"]) == ["Te", "Ni", "Se", "Fi"]
    assert convert_mbti_to_cognitive_fns(["E", "N", "T", "J"], calculate_shadow_fns=True) == ["Ti", "Ne", "Si", "Fe"]


def test_intj():
    assert convert_mbti_to_cognitive_fns(["I", "N", "T", "J"]) == ["Ni", "Te", "Fi", "Se"]
    assert convert_mbti_to_cognitive_fns(["I", "N", "T", "J"], calculate_shadow_fns=True) == ["Ne", "Ti", "Fe", "Si"]


def test_entp():
    assert convert_mbti_to_cognitive_fns(["E", "N", "T", "P"]) == ["Ne", "Ti", "Fe", "Si"]
    assert convert_mbti_to_cognitive_fns(["E", "N", "T", "P"], calculate_shadow_fns=True) == ["Ni", "Te", "Fi", "Se"]


def test_intp():
    assert convert_mbti_to_cognitive_fns(["I", "N", "T", "P"]) == ["Ti", "Ne", "Si", "Fe"]
    assert convert_mbti_to_cognitive_fns(["I", "N", "T", "P"], calculate_shadow_fns=True) == ["Te", "Ni", "Se", "Fi"]
