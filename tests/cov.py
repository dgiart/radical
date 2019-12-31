import coverage
from tests import *

cov = coverage.Coverage()
cov.erase()
cov.start()
ns=TestNitrosalt()
sg=TestSugar()
ns.test_nitro_salt_returns_mass1()
ns.test_nitro_salt_returns_int2()
ns.test_nitro_salt_receives_str_returns_int3()
ns.test_nitro_salt_receives_alpha_returns_zero4()

sg.test_sugar_mass5()

cov.stop()
cov.save()

cov.html_report()
# cov.report()
# cov.report('html_from_py')
