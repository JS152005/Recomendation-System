from recommendation_engine import RecommendationEngine

def run_recommendation_system():
    """
    Main function to run the recommendation system
    with comprehensive demonstration of features
    """
    try:
        # Initialize Recommendation Engine
        recommendation_engine = RecommendationEngine()
        
        # Section 1: Data Loading
        print("\n🚀 Recommendation System Initialization 🚀")
        print("=" * 50)
        
        # Load Product Data
        recommendation_engine.load_data()
        
        # Section 2: Model Training
        print("\n🧠 Training Recommendation Model")
        print("=" * 50)
        recommendation_engine.train()
        
        # Section 3: Random Product Recommendations
        print("\n🎲 Random Product Recommendations")
        print("=" * 50)
        recommendation_engine.get_recommendations()
        
        # Section 4: Specific Product Recommendations
        print("\n🔍 Specific Product Recommendations")
        print("=" * 50)
        print("Recommending similar products to Product ID 2")
        recommendation_engine.get_recommendations(product_id=2)
        
        # Section 5: Category-based Recommendations
        print("\n🏷️ Category-based Recommendations")
        print("=" * 50)
        recommendation_engine.recommend_by_category('Electronics')
        recommendation_engine.recommend_by_category('Wearables')
    
    except Exception as e:
        print(f"❌ Recommendation System Error: {e}")

def main():
    """
    Entry point for the recommendation system
    """
    run_recommendation_system()

if __name__ == '__main__':
    main()