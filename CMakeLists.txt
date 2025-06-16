cmake_minimum_required(VERSION 3.8)
project(robo_3)

if(CMAKE_COMPILER_IS_GNUCXX OR CMAKE_CXX_COMPILER_ID MATCHES "Clang")
  add_compile_options(-Wall -Wextra -Wpedantic)
endif()

# find dependencies
find_package(ament_cmake REQUIRED)
find_package(gazebo_ros_pkgs REQUIRED)
find_package(rclcpp REQUIRED)
find_package(geometry_msgs REQUIRED)
find_package(sensor_msgs REQUIRED)
# uncomment the following section in order to fill in
# further dependencies manually.
# find_package(<dependency> REQUIRED)

# Set up Gazebo model directory for SDF files
set(MODEL_PATH "/home/kifelix/ros2_ws/src/robo_3/model")
 
# Ensure the path to Gazebo models is included in CMake
file(GLOB MODEL_FILES "${MODEL_PATH}/*.sdf")
 
# Optional: If you have custom Gazebo plugins, find them
# find_package(gazebo REQUIRED) # If you're writing your own plugins, this may be necessary
 
# Install launch files
install(DIRECTORY launch/
  DESTINATION share/${PROJECT_NAME}/launch
)
 
install(DIRECTORY ${MODEL_PATH}/
  DESTINATION share/${PROJECT_NAME}/model
)

add_executable(cefet src/cefet.cpp)
target_include_directories(cefet PUBLIC
  $<BUILD_INTERFACE:${CMAKE_CURRENT_SOURCE_DIR}/include>
  $<INSTALL_INTERFACE:include>)
target_compile_features(cefet PUBLIC c_std_99 cxx_std_17)  # Require C99 and C++17

install(TARGETS cefet
  DESTINATION lib/${PROJECT_NAME})

if(BUILD_TESTING)
  find_package(ament_lint_auto REQUIRED)
  # the following line skips the linter which checks for copyrights
  # comment the line when a copyright and license is added to all source files
  set(ament_cmake_copyright_FOUND TRUE)
  # the following line skips cpplint (only works in a git repo)
  # comment the line when this package is in a git repo and when
  # a copyright and license is added to all source files
  set(ament_cmake_cpplint_FOUND TRUE)
  ament_lint_auto_find_test_dependencies()
endif()

ament_package()
