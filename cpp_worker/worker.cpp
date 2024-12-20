#include <iostream>
#include <vector>
#include <numeric>

extern "C" {
    double compute_step(double* data, size_t length) {
        // Handle empty array case by checking for a nullptr or zero length
        if (length == 0 || data == nullptr) {
            std::cout << "Received empty array, returning 0" << std::endl;
            return 0.0;  // Return a sensible value for an empty array
        }
        
        double sum = 0.0;
        for (size_t i = 0; i < length; ++i) {
            sum += data[i];
        }
        return sum;
    }
}


