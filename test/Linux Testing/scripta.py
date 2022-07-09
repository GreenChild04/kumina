import sys, os

sys.path.append(os.path.abspath('..'))

from requestil import RequestPackage


class TestScript:
    def run(self, interPackage, req):
        print(req.test())
