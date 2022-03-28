import pytest
from chaos_game import ChaosGame
import os.path


# Exercise 2h)
def test_n_chaos_game_raises_ValueError():
    for i in range(-1, 3):
        with pytest.raises(ValueError):
            ChaosGame(i)


def test_r_chaos_game_raises_ValueError():
    with pytest.raises(ValueError):
        ChaosGame(3, -0.1)
        ChaosGame(3, 2)


def test_savepng_file_saved_with_proper_filename():
    obj = ChaosGame(3)
    obj._starting_point()
    obj.iterate(1000)
    exp = "output_test.png"
    obj.savepng(exp)
    assert os.path.isfile(exp)


def test_savepng_raises_TypeError():
    obj = ChaosGame(3)
    obj._starting_point()
    obj.iterate(10)
    with pytest.raises(TypeError):
        obj.savepng(123)


def test_savepng_wrong_extension_raises_TypeError():
    obj = ChaosGame(3)
    obj._starting_point()
    obj.iterate(10)
    with pytest.raises(TypeError):
        obj.savepng("output_test.jpg")


if __name__ == "__main__":
    test_n_chaos_game_raises_ValueError()
    test_r_chaos_game_raises_ValueError()
    test_savepng_file_saved_with_proper_filename()
    test_savepng_wrong_extension_raises_TypeError()
