# python_verification.py
import sys
import platform
import importlib
import os

def check_python_environment():
    """Verify Python environment details"""
    print("=== Python Environment ===")
    print(f"Python Version: {sys.version}")
    print(f"Python Executable Path: {sys.executable}")
    print(f"Platform: {platform.platform()}")
    print(f"Python Implementation: {platform.python_implementation()}")
    print(f"Python Path: {sys.path}")

def check_library_imports():
    """Check import status of required libraries"""
    print("\n=== Library Import Check ===")
    required_libraries = [
        'pandas', 
        'numpy', 
        'sklearn', 
        'sklearn.feature_extraction.text',
        'sklearn.metrics.pairwise'
    ]
    
    for lib in required_libraries:
        try:
            importlib.import_module(lib)
            print(f"✅ {lib}: IMPORTED SUCCESSFULLY")
        except ImportError:
            print(f"❌ {lib}: IMPORT FAILED")

def check_project_configuration():
    """Verify project file structure and configuration"""
    print("\n=== Project Configuration ===")
    
    # Current working directory
    current_dir = os.getcwd()
    print(f"Current Directory: {current_dir}")
    
    # Project files to check
    project_files = [
        'recommendation_engine.py',
        'run.py',
        'data/products.csv'
    ]
    
    for file in project_files:
        file_path = os.path.join(current_dir, file)
        if os.path.exists(file_path):
            print(f"✅ {file}: EXISTS")
            # Additional file details
            file_size = os.path.getsize(file_path)
            print(f"   File Size: {file_size} bytes")
        else:
            print(f"❌ {file}: NOT FOUND")

def test_recommendation_engine():
    """Test the recommendation engine functionality"""
    print("\n=== Recommendation Engine Test ===")
    try:
        from recommendation_engine import RecommendationEngine
        
        # Initialize recommendation engine
        engine = RecommendationEngine()
        
        # Load data
        print("Loading data...")
        data = engine.load_data()
        
        if data is not None:
            print("✅ Data Loaded Successfully")
            print(f"Number of Products: {len(data)}")
            
            # Train model
            print("Training model...")
            engine.train()
            print("✅ Model Trained Successfully")
            
            # Get recommendations
            print("Generating recommendations...")
            recommendations = engine.get_recommendations()
            
            if recommendations is not None:
                print("✅ Recommendations Generated Successfully")
                print("Recommended Products:")
                for idx, row in recommendations.iterrows():
                    print(f"- {row['name']} (Category: {row['category']}, Price: ${row['price']})")
            else:
                print("❌ Failed to generate recommendations")
        else:
            print("❌ Failed to load data")
    
    except Exception as e:
        print(f"❌ Error in Recommendation Engine Test: {e}")

def system_compatibility_check():
    """Check system compatibility and resource availability"""
    print("\n=== System Compatibility ===")
    
    # Memory check
    import psutil
    memory = psutil.virtual_memory()
    print(f"Total Memory: {memory.total / (1024**3):.2f} GB")
    print(f"Available Memory: {memory.available / (1024**3):.2f} GB")
    print(f"Memory Usage: {memory.percent}%")
    
    # CPU Information
    import multiprocessing
    print(f"CPU Cores: {multiprocessing.cpu_count()}")

def main():
    """Main verification function"""
    print("🔍 Comprehensive Python Environment Verification 🔍")
    
    check_python_environment()
    check_library_imports()
    check_project_configuration()
    test_recommendation_engine()
    system_compatibility_check()

if __name__ == '__main__':
    main()