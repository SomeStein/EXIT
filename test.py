import ctypes
import os
import platform

# Get the path to the current script directory
current_dir = os.path.dirname(os.path.abspath(__file__))

# Build the path to the shared library (libworker.dylib for macos) inside the build directory
if platform.system() == 'Darwin':  # macOS
    lib_path = os.path.join(current_dir, 'build', 'libworker.dylib')
elif platform.system() == 'Linux':  # Linux
    lib_path = os.path.join(current_dir, 'build', 'libworker.so')
elif platform.system() == 'Windows':  # Windows
    lib_path = os.path.join(current_dir, 'build', 'worker.dll')

# Load the shared library
worker_lib = ctypes.CDLL(lib_path)

# Define the argument and return types for the C++ function
worker_lib.compute_step.argtypes = [ctypes.POINTER(ctypes.c_double), ctypes.c_size_t]  # double* and size_t
worker_lib.compute_step.restype = ctypes.c_double  # Return type is double

# Example function call: assuming your C++ function takes a pointer to an array of doubles
def compute_step(data):
    # If the data is empty, pass None to avoid sending an empty array
    if len(data) == 0:
        print("Warning: Empty array passed, handling in C++")
        return worker_lib.compute_step(None, 0)  # Pass None and 0 length
    
    # Convert the input list to a ctypes array of doubles
    array_type = ctypes.c_double * len(data)  # Define array type
    array = array_type(*data)  # Create the array with input data
    
    # Call the C++ function (e.g., compute_step)
    result = worker_lib.compute_step(array, len(data))  # Pass array and length
    return result

# Example usage
data = [1.0, 2.0, 3.0, 4.0]  # Input data
result = compute_step(data)
print(f"Result: {result}")
