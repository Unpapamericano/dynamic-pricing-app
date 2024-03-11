from flask import Flask, jsonify, request
import pandas as pd
from sklearn.linear_model import LinearRegression
import numpy as np

app = Flask(__name__)

# Dummy machine learning model for dynamic pricing
def train_dynamic_pricing_model():
    # Assuming 'data' is the historical pricing data
    data = {
        'product_id': [1, 2, 3, 4, 5],
        'price': [20, 30, 25, 40, 35],
        'user_history': [10, 5, 8, 12, 15]
    }

    df = pd.DataFrame(data)
    X = df[['product_id', 'user_history']]
    y = df['price']

    model = LinearRegression()
    model.fit(X, y)

    return model

dynamic_pricing_model = train_dynamic_pricing_model()

@app.route('/api/dynamic_price', methods=['GET'])
def dynamic_price():
    try:
        product_id = int(request.args.get('product_id'))
        user_history = int(request.args.get('user_history'))

        # Make a dynamic price prediction
        input_data = np.array([[product_id, user_history]])
        predicted_price = dynamic_pricing_model.predict(input_data)[0]

        return jsonify({'message': f'Predicted dynamic price for Product {product_id}: ${predicted_price:.2f}'})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(debug=True)

