import pytest


@pytest.mark.usefixtures('Start')
class Baike_test():

    def test_001(self, Start):
        Start[1].search()
        print("this is test_001")

    def test_002(self,Start):
        Start[1].get_url()

        print("this is test_002")

    def test_003(self):

        print("this is test_003")