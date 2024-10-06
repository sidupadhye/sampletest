import pytest


#@pytest.mark.sanity
def test_sample_one(setup_and_teardown):
    print("Inside sample one")

#@pytest.mark.regreesion
#@pytest.mark.skip
def test_Sample_two(setup_and_teardown):
    print("Inside Sample two")

#@pytest.mark.smoke
#@pytest.mark.xfail
def test_Sample_three(setup_and_teardown):
    print("Inside Sample Three")
    #assert False

#@pytest.mark.xfail
def test_Sample_don(setup_and_teardown):
    print("Inside test sample DON" )
