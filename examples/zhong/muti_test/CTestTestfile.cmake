# CMake generated Testfile for 
# Source directory: /Users/shaoyc/Github/Cython_Pycharm/examples/zhong/muti_test
# Build directory: /Users/shaoyc/Github/Cython_Pycharm/examples/zhong/muti_test
# 
# This file includes the relevant testing commands required for 
# testing this directory and lists subdirectories to be tested as well.
add_test(test_run "use_power" "2" "3")
add_test(test_usage "use_power")
set_tests_properties(test_usage PROPERTIES  PASS_REGULAR_EXPRESSION "Usage: .* base exponent")
add_test(test_5_2 "use_power" "5" "2")
set_tests_properties(test_5_2 PROPERTIES  PASS_REGULAR_EXPRESSION "is 25")
add_test(test_2_3 "use_power" "2" "3")
set_tests_properties(test_2_3 PROPERTIES  PASS_REGULAR_EXPRESSION "is 8")
add_test(test_3_4 "use_power" "3" "4")
set_tests_properties(test_3_4 PROPERTIES  PASS_REGULAR_EXPRESSION "is 81")
