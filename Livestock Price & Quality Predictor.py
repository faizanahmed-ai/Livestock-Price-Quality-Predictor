# Livestock Price and Quality Predictor

# Price for each animal per kilogram (PKR)
rates = {
    "cow": 1200,
    "buffalo": 1300,
    "goat": 1000,
    "sheep": 1000,
    "camel": 1400,
    "other": 1000
}

def predict_price(age, weight, animal):
    # find rate for this animal (if not found, use "other")
    rate = rates.get(animal.lower(), rates["other"])
    
    # base price
    price = weight * rate

    # change price based on age
    if age < 1:
        price = price * 0.9   # 10% less
    elif age > 2:
        price = price * 1.2   # 20% more

    # decide quality from weight
    if weight < 50:
        quality = "Fair"
    elif weight <= 70:
        quality = "Good"
    else:
        quality = "Excellent"

    return round(price), quality


def main():
    animals = []   # to store all entries
    total = 0      # total price

    while True:
        animal = input("Enter animal type (cow, buffalo, goat, sheep, camel): ")
        if animal == "":
            animal = "other"

        age = float(input("Enter age (years): "))
        weight = float(input("Enter weight (kg): "))

        price, quality = predict_price(age, weight, animal)

        animals.append((animal, age, weight, price, quality))
        total += price

        more = input("Do you want to add another animal? (y/n): ")
        if more.lower() != "y":
            break

    print("\n--- Summary ---")
    for i, (animal, age, weight, price, quality) in enumerate(animals, 1):
        print(f"{i}. {animal} | Age: {age} yrs | Weight: {weight} kg | Price: PKR {price} | Quality: {quality}")
    print("Total Price:", total)


if __name__ == "__main__":
    main()
c