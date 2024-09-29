import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
import joblib
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay

# Load your dataset
data = pd.read_csv('EyeConj.csv')  # Replace with your actual dataset file

# Split the dataset into features and labels
y = data['Hb_level']  # Corrected to match the column name
X = data[['red_pixel', 'green_pixel']]  # Features

print(X, y)

# Split the dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a Decision Tree Classifier
model = DecisionTreeClassifier(random_state=42)

# Train the model
model.fit(X_train, y_train)

# Make predictions
y_pred = model.predict(X_test)

# Evaluate the model
accuracy = accuracy_score(y_test, y_pred)
#print(f'Accuracy: {accuracy * 100:.2f}%')

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)

# Print confusion matrix
#print("Confusion Matrix:")
#print(cm)
disp.plot(cmap='Blues')

# Save the model to a file
joblib.dump(model, 'treeModel.pkl')
#print('Model saved as decision_tree_model.pkl')

def predict_hb(red_pixel, green_pixel, model_file='treeModel.pkl'):
    # Load the trained model
    model = joblib.load(model_file)

    # Prepare the input as a 2D list
    input_data = [[red_pixel, green_pixel]]

    # Make predictions (probabilities)
    probabilities = model.predict_proba(input_data)  # Get probabilities

    # Return the probability of being non-anemic (class 1)
    finalSwPo = probabilities[0][1]
    FIN = (0.5 - finalSwPo) + 0.5
    print(f"final amenia: {FIN}")
    return FIN

'''
# Test the prediction function NON-anemic
score = predict_hb(47, 26)
print(f'Probability of being anemic: {score:.2f}')  # Output the score
'''
