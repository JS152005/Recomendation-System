import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

class RecommendationEngine:
    def __init__(self, data_path='data/products.csv'):
        """
        Initialize Recommendation Engine
        
        Parameters:
        -----------
        data_path : str, optional
            Path to the products CSV file (default is 'data/products.csv')
        """
        self.data_path = data_path
        self.products_df = None
        self.tfidf_matrix = None
        self.similarity_matrix = None
    
    def load_data(self):
        """
        Load product data from CSV file
        
        Returns:
        --------
        pandas.DataFrame
            DataFrame containing product information
        """
        try:
            # Read CSV file
            self.products_df = pd.read_csv(self.data_path)
            
            # Print data loading confirmation
            print(f"✅ Loaded {len(self.products_df)} products")
            print("\nProduct Data Preview:")
            print(self.products_df.head())
            
            return self.products_df
        
        except Exception as e:
            print(f"❌ Error loading data: {e}")
            return None
    
    def preprocess_data(self):
        """
        Preprocess data for recommendation
        
        Creates a combined features column for recommendation
        """
        if self.products_df is None:
            self.load_data()
        
        # Combine features for recommendation
        self.products_df['combined_features'] = (
            self.products_df['name'] + ' ' + 
            self.products_df['category'] + ' ' + 
            self.products_df['description']
        )
    
    def train(self):
        """
        Train recommendation model using TF-IDF and Cosine Similarity
        """
        # Preprocess data
        self.preprocess_data()
        
        # Create TF-IDF Vectorizer
        tfidf = TfidfVectorizer(stop_words='english')
        
        # Transform features
        self.tfidf_matrix = tfidf.fit_transform(
            self.products_df['combined_features']
        )
        
        # Calculate similarity matrix
        self.similarity_matrix = cosine_similarity(self.tfidf_matrix)
        
        print("✅ Recommendation model trained successfully")
    
    def get_recommendations(self, product_id=None, top_k=5):
        """
        Generate product recommendations
        
        Parameters:
        -----------
        product_id : int, optional
            Specific product ID to find similar products
        top_k : int, optional
            Number of recommendations to return (default is 5)
        
        Returns:
        --------
        pandas.DataFrame
            DataFrame of recommended products
        """
        # Ensure model is trained
        if self.products_df is None or self.tfidf_matrix is None:
            self.train()
        
        # If no specific product, choose random
        if product_id is None:
            product_id = np.random.choice(self.products_df['product_id'])
        
        try:
            # Find product index
            product_index = self.products_df[
                self.products_df['product_id'] == product_id
            ].index[0]
            
            # Get similarity scores
            similarity_scores = list(enumerate(self.similarity_matrix[product_index]))
            
            # Sort similar products
            sorted_scores = sorted(
                similarity_scores, 
                key=lambda x: x[1], 
                reverse=True
            )[1:top_k+1]
            
            # Get recommended product indices
            recommended_indices = [
                index for index, score in sorted_scores
            ]
            
            # Return recommendations
            recommendations = self.products_df.iloc[recommended_indices]
            
            # Print recommendations
            print(f"\n🔍 Recommendations for Product ID {product_id}:")
            for idx, row in recommendations.iterrows():
                print(f"- {row['name']} (Category: {row['category']}, Price: ${row['price']})")
            
            return recommendations
        
        except IndexError:
            print(f"❌ Product ID {product_id} not found")
            return None
    
    def recommend_by_category(self, category, top_k=5):
        """
        Recommend products within a specific category
        
        Parameters:
        -----------
        category : str
            Product category to filter
        top_k : int, optional
            Number of recommendations to return (default is 5)
        
        Returns:
        --------
        pandas.DataFrame
            DataFrame of recommended products
        """
        try:
            # Filter products by category
            category_products = self.products_df[
                self.products_df['category'] == category
            ]
            
            # Return top k products
            recommendations = category_products.head(top_k)
            
            print(f"\n🏷️ Top {top_k} Products in {category} Category:")
            for idx, row in recommendations.iterrows():
                print(f"- {row['name']} (Price: ${row['price']})")
            
            return recommendations
        
        except Exception as e:
            print(f"❌ Error in category recommendation: {e}")
            return None

def main():
    """
    Main function to demonstrate recommendation engine capabilities
    """
    # Initialize recommendation engine
    engine = RecommendationEngine()
    
    # Load data
    engine.load_data()
    
    # Train model
    engine.train()
    
    # Generate recommendations for a random product
    print("\n=== Random Product Recommendations ===")
    engine.get_recommendations()
    
    # Recommend by category
    print("\n=== Category-based Recommendations ===")
    engine.recommend_by_category('Electronics')

if __name__ == '__main__':
    main()