from __future__ import print_function
import sys

try:
    from SConstructLocal import *
    print("INFO: SConstructLocal.py loaded")
except ImportError:
    print("ERROR: Cannot find SConstructLocal.py")
    print("INFO: Creating SConstructLocal.py")
    with open("SConstructLocal.py", 'w') as ofile:
        print("""
#Path to your python-dev header files
pyInc= '/usr/include/python2.7'
#Path to the panda3d header files
pandaInc= '/usr/include/panda3d'
#Path to the eigen3 header files
eigen= '/usr/include/eigen3'
#Path to the panda3d library files
pandaLib= '/usr/lib/x86_64-linux-gnu/panda3d'

#Remove these 4 lines after editing
import sys
print("ERROR: SConstLocal.py not set up yet")
print("       please edit it and then run scons again")
sys.exit(1)
""", file=ofile)
        print("      SConstructLocal.py created")
        print("      please edit it and re-run scons")
        sys.exit(0);

Program('pandatest', ['pandatest.cpp'],
	CCFLAGS=['-fPIC', '-O2'],
	CPPPATH=[pyInc, pandaInc, eigen],
	LIBPATH=pandaLib,
	LIBS=['libp3framework',
		'libpanda',
		'libpandafx',
		'libpandaexpress',
		'libp3dtoolconfig',
		'libp3dtool',
		'libp3pystub',
		'libp3direct'])
