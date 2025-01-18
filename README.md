# 🚀 Product Recommendation System

## 📌 Project Overview

This is a product recommendation system built using Python, designed to provide intelligent product suggestions based on similarity and features. 

### 🌟 Key Features
- TF-IDF based recommendation engine
- Product similarity matching
- Category-based recommendations
- Comprehensive verification script for testing

## 🛠 Technologies Used

![Python](https://img.shields.io/badge/Python-3.8+-blue)
![Pandas](https://img.shields.io/badge/Pandas-Data_Analysis-green)
![Scikit-learn](https://img.shields.io/badge/Scikit--learn-ML_Library-orange)

- **Language**: Python 3.8+
- **Libraries**: 
  - Pandas
  - NumPy
  - Scikit-learn
- **Recommendation Technique**: TF-IDF Vectorization
- **Similarity Metric**: Cosine Similarity

## 📦 Project Structure

recommendationsys/ │ ├── data/ │ └── products.csv # Product dataset ├── recommendation_engine.py # Core recommendation logic ├── run.py # Main execution script ├── python_verification.py # Verification script for testing ├── recommendation_env/ # Virtual environment └── README.md # Project documentation


## 🚦 Prerequisites

### System Requirements
- Python 3.8+
- 8GB RAM
- Virtual Environment support

### Required Libraries
- pandas
- numpy
- scikit-learn

## 🔧 Setup and Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/recommendationsys.git
cd recommendationsys

2. Create Virtual Environment

# Windows
python -m venv recommendation_env
recommendation_env\Scripts\activate

# macOS/Linux
python3 -m venv recommendation_env
source recommendation_env/bin/activate

3. Install Dependencies

pip install -r requirements.txt

🏃 Running the Application
Activate Virtual Environment

# Windows
recommendation_env\Scripts\activate

# macOS/Linux
source recommendation_env/bin/activate

# Windows
recommendation_env\Scripts\activate

# macOS/Linux
source recommendation_env/bin/activate

Execute Recommendation System

python run.py

🔍 Verification Script
To ensure the system is set up correctly, you can run the verification script:

Run Verification
python python_verification.py

This script will check:

Python environment details
Library imports
Project configuration
Recommendation engine functionality
System compatibility
📊 Recommendation Strategies
1. Product Similarity Recommendations
Uses TF-IDF vectorization
Computes cosine similarity between products
Recommends most similar items
2. Category-based Recommendations
Filter products by category
Provide top recommendations within a category

🔍 Example Usage
# Create recommendation engine
engine = RecommendationEngine()

# Load and train model
engine.load_data()
engine.train()

# Get recommendations for a specific product
recommendations = engine.get_recommendations(product_id=2)

# Get category-based recommendations
category_recommendations = engine.recommend_by_category('Electronics')


📈 Performance Metrics
Data Loading Speed: O(n)
Recommendation Generation: O(n log n)
Memory Efficiency: Optimized with sparse matrix


📞 Contact
Jothi Prakash B S

Email: bsjothiprakash155@gmail.com
LinkedIn: https://www.linkedin.com/in/jothiprakash1/

<<<<<<<< Built by Jothi Prakash B S >>>>>>>>


