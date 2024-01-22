from archiver import archiver
from unarchiver import unarchiver
from archiver_with_nums import archiver_with_nums
from unarchiver_with_nums import unarchiver_with_nums


def test_archiver_wrong_nums1():
    assert archiver("hello5") == ""


def test_archiver_wrong_nums2():
    assert archiver("5hello") == ""


def test_archiver1():
    assert archiver("hello!!!   worrrld???") == "hel2o!3 wor3ld?3"


def test_archiver2():
    assert archiver("hello!!!   worrrld") == "hel2o!3 wor3ld"


def test_unarchiver1():
    assert unarchiver("h5el2o w11orld5!3") == "hhhhhello wwwwwwwwwwworlddddd!!!"


def test_unarchiver2():
    assert unarchiver("h5el2o w11orld5!") == "hhhhhello wwwwwwwwwwworlddddd!"


def test_archiver_with_nums():
    assert archiver_with_nums("корабли-коты хотят захватить планету, спасите свою планету, пока корабли-коты не захватили ее скорей скорей спасайте планету") == "корабли-коты хотят захватить планету, спасите свою[1c 7]у, пока [0 7]-коты не[12 7]или ее скорей[5d 7] спасайте[1c 7]у"


def test_archiver_with_nums_symbols():
    assert archiver_with_nums("[hello]") == "[*hello]"


def test_unarchiver_with_nums():
    assert unarchiver_with_nums("hello-[0 5] friends") == "hello-hello friends"


def test_unarchiver_with_nums_symbols():
    assert unarchiver_with_nums("[*hello")=="[hello"
