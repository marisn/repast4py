# repast4py

Compile with: 

`CC=mpicc CXX=mpicxx python setup.py build_ext --inplace`

or for debugging:

`CC=mpicc CXX=mpicxx CFLAGS="-O0 -g" CXXFLAGS="-O0 -g" python setup.py build_ext --inplace`

## Tests ##

There are 3 types of python unit tests:

1. Ordinary single process tests. Run with:

`python -m unittest discover tests` 

2. Multiprocess (9 procs) mpi tests for 2D spaces. Run with:

`mpirun -n 9 python -m unittest tests.shared_obj_tests`
`mpirun -n 9 python -m unittest tests.shared_vl_tests`

3. Multiprocess (18 procs) mpi tests for 3D spaces. Run with:

`mpirun -n 18 python -m unittest tests.shared_obj_tests.SharedGridTests.test_buffer_data_3d`
`mpirun -n 18 python -m unittest tests.shared_obj_tests.SharedGridTests.test_buffer_data_3d_periodic`
`mpirun -n 18 python -m unittest tests.shared_vl_tests.SharedValueLayerTests.test_buffers_3x3x3_periodic`
`mpirun -n 18 python -m unittest tests.shared_vl_tests.SharedValueLayerTests.test_buffers_3x3x3_sticky`

Or for 3d tests if python >= 3.7:

`mpirun -n 18 python -m unittest -k tests.shared_obj_tests.SharedGridTests.test_buffer_data_3d*`


There also some C++ unitest. C++ tests can be compiled with makefile target 'tests' and run with:

`mpirun -n 9 ./unit_tests`

## Zombies ##

Requires compiled repast4py.

`PYTHONPATH=./src python src/zombies/zombies.py src/zombies/zombie_model.props`