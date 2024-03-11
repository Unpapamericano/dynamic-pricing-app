Dynamic Pricing Prediction API
Welcome to the Dynamic Pricing Prediction API! This Flask-based web application provides a simple API for predicting dynamic prices based on historical pricing data. The underlying machine learning model is a Linear Regression model trained on historical product prices and user interaction history.

##Getting Started
To use the Dynamic Pricing Prediction API, follow these steps:

#Clone the Repository:

bash
Copy code
git clone https://github.com/your-username/dynamic-pricing-api.git
cd dynamic-pricing-api
#Install Dependencies:

bash
Copy code
pip install -r requirements.txt
#Run the Application:

bash
Copy code
python app.py
The API will be accessible at http://127.0.0.1:5000/.

##API Usage
Predict Dynamic Price
Endpoint: /api/dynamic_price
Method: GET
Parameters:
product_id (integer): The ID of the product for which you want to predict the dynamic price.
user_history (integer): The user interaction history for the specified product.
Example Request
bash
Copy code
curl -X GET "http://127.0.0.1:5000/api/dynamic_price?product_id=3&user_history=8"
Example Response
json
Copy code
{
  "message": "Predicted dynamic price for Product 3: $27.50"
}
##Machine Learning Model
The machine learning model used for dynamic price prediction is a Linear Regression model. It has been trained on historical pricing data, considering the product_id and user_history as features to predict the product's price.

#Contributing
If you'd like to contribute to the development of this project, please follow the contribution guidelines.

#Issues
If you encounter any issues or have suggestions, please feel free to open an issue.

#Happy predicting! 🚀
