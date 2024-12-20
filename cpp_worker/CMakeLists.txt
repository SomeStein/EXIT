cmake_minimum_required(VERSION 3.10)

# Set project name and language
project(WorkerLib LANGUAGES CXX)

# Create the shared library from the C++ source file
add_library(worker SHARED worker.cpp)

# Set the output name of the shared library (OS-specific extensions)
if (APPLE)
    set_target_properties(worker PROPERTIES
        OUTPUT_NAME "worker"      # This removes the extra 'lib' prefix
        SUFFIX ".dylib")
elseif (MSVC)
    set_target_properties(worker PROPERTIES
        OUTPUT_NAME "worker"
        SUFFIX ".dll")
else()
    set_target_properties(worker PROPERTIES
        OUTPUT_NAME "worker"
        SUFFIX ".so")
endif()

# Include directories for headers (if needed)
# target_include_directories(worker PUBLIC ${CMAKE_SOURCE_DIR}/include)
