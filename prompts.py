def recommend_fruits(party_on_weekends, flavor_preference, texture_dislike, price_range):
    fruits = ["oranges", "apples", "pears", "grapes", "watermelon", "lemon", "lime"]
    
    # Apply rules based on user's answers
    if party_on_weekends == "yes":
        fruits = ["apples", "pears", "grapes", "watermelon"]
    if flavor_preference == "cider":
        fruits = ["apples", "oranges", "lemon", "lime"]
    elif flavor_preference == "sweet":
        fruits = ["watermelon", "oranges"]
    elif flavor_preference == "waterlike":
        fruits = ["watermelon"]
    if "grapes" in fruits:
        fruits.remove("watermelon")
    if texture_dislike == "smooth":
        if "pears" in fruits:
            fruits.remove("pears")
    elif texture_dislike == "slimy":
        if "watermelon" in fruits:
            fruits.remove("watermelon")
        if "lime" in fruits:
            fruits.remove("lime")
        if "grapes" in fruits:
            fruits.remove("grapes")
    elif texture_dislike == "waterlike":
        if "watermelon" in fruits:
            fruits.remove("watermelon")
    if price_range < 3:
        if "lime" in fruits:
            fruits.remove("lime")
        if "watermelon" in fruits:
            fruits.remove("watermelon")
    elif price_range > 4 and price_range < 7:
        if "pears" in fruits:
            fruits.remove("pears")
        if "apples" in fruits:
            fruits.remove("apples")
    
    return fruits

# Example usage:
party_on_weekends = input("Do you go out to party on weekends? (yes or no): ")
flavor_preference = input("What flavors do you like? (cider, sweet, waterlike): ")
texture_dislike = input("What texture do you dislike? (smooth, slimy, rough): ")
price_range = float(input("What price range will you buy drink for? ($1, $2, $3, $4, $5, $6, $7, $8, $9, $10): "))

recommended_fruits = recommend_fruits(party_on_weekends, flavor_preference, texture_dislike, price_range)
print("Recommended fruits:", recommended_fruits)

# from flask import Flask, request, jsonify

# app = Flask(__name__)

# @app.route('/answers', methods=['POST'])
# def get_answers():
#     data = request.json
    
#     # Extracting answers from JSON data
#     party_on_weekends = data.get('party_on_weekends')
#     flavor_preference = data.get('flavor_preference')
#     texture_dislike = data.get('texture_dislike')
#     price_range = data.get('price_range')
    
#     # Your logic to process the answers and generate the responses goes here
#     # For simplicity, let's just return the received answers
#     return jsonify({
#         "party_on_weekends": party_on_weekends,
#         "flavor_preference": flavor_preference,
#         "texture_dislike": texture_dislike,
#         "price_range": price_range
#     })

# if __name__ == '__main__':
#     app.run(debug=True)

