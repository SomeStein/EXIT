import os
import subprocess
import sys
import shutil
import platform
from pathlib import Path

def clean_build():
    """
    Clean up old build directories
    """
    print("Cleaning up old build files...")
    build_dir = Path("build")
    dist_dir = Path("dist")
    requirements_file = Path("requirements.txt")
    if requirements_file.exists():
        requirements_file.unlink()
    if build_dir.exists():
        shutil.rmtree(build_dir)
    if dist_dir.exists():
        shutil.rmtree(dist_dir)
  
      
def update_requirements_txt():
    """
    Updates the requirements.txt file with the current installed packages
    """
    print("Updating requirements.txt...")
    with open('requirements.txt', 'w') as f:
        subprocess.check_call([sys.executable, "-m", "pip", "freeze"], stdout=f)
    print("requirements.txt has been updated.")


def install_dependencies():
    """
    Installs dependencies from requirements.txt
    """
    print("Installing dependencies...")
    subprocess.check_call([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])


def build_cpp_library():
    """
    Configures and builds the C++ shared library using CMake
    """
    print("Building C++ library...")

    # Set platform-specific build directory
    build_dir = Path("build")
    if not build_dir.exists():
        build_dir.mkdir()

    cpp_worker_dir = Path("cpp_worker")  # Directory where CMakeLists.txt is located

    # Run CMake to configure the project
    subprocess.check_call(["cmake", "-S", str(cpp_worker_dir), "-B", str(build_dir)])

    # Build the shared library using CMake
    subprocess.check_call(["cmake", "--build", str(build_dir), "--config", "Release"])


def run_pyinstaller():
    """
    Run PyInstaller to package the application as a .app bundle for macOS
    """
    current_dir = os.path.dirname(os.path.abspath(__file__))
    
    # Adjust the shared library path for different platforms
    if platform.system() == "Darwin":  # macOS
        lib_path = os.path.join(current_dir, 'build', 'libworker.dylib')
        app_name = "main.app"  # The name of the .app bundle
    elif platform.system() == "Windows":
        lib_path = os.path.join(current_dir, 'build', 'worker.dll')
        app_name = "main.exe"  # Windows executable
    else:  # Linux
        lib_path = os.path.join(current_dir, 'build', 'libworker.so')
        app_name = "main"  # Linux executable

    # Run PyInstaller to create a macOS .app bundle
    pyinstaller_cmd = [
        "pyinstaller",
        "--onefile",  # Bundle into a single executable
        "--windowed",  # Prevent terminal window on GUI apps
        f"--add-data={lib_path}:build",  # Include the shared library
        "--name=main",  # Name of the app
        "--distpath=dist",  # Output directory for the package
        "--workpath=build",  # Temporary work directory for PyInstaller
        "--specpath=specs",  # Directory for .spec files
        "main.py"  # The main Python script to package
    ]
    
    print("Running PyInstaller to create a .app bundle...")
    subprocess.check_call(pyinstaller_cmd)
    
    # Rename the output to a .app bundle
    app_bundle_dir = os.path.join("dist", "main.app")
    if os.path.exists(app_bundle_dir):
        os.rename(app_bundle_dir, os.path.join("dist", app_name))
    print(f"Created macOS .app bundle: {app_name}")


def package_application():
    """
    Main function to automate the packaging process
    """
    clean_build()
    update_requirements_txt()
    install_dependencies()
    build_cpp_library()
    run_pyinstaller()

    print("Packaging complete! Your executable is located in the 'dist' folder.")


if __name__ == "__main__":
    package_application()

