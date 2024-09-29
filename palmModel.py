import tensorflow as tf
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Conv2D, MaxPooling2D, Flatten, Dense, Dropout
from tensorflow.keras.callbacks import EarlyStopping, ModelCheckpoint, ReduceLROnPlateau
from sklearn.metrics import classification_report, confusion_matrix
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import keras

# custom preprocessing with random sizing to account for different people's nail sizes and apperances
def custom_preprocessing(image):
    if np.random.random() < 0.3:
        # Randomly choose stretching or condensing
        if np.random.random() < 0.5:
            # Stretch horizontally
            scale_factor = np.random.uniform(1.1, 1.3)  # Adjust range as needed
        else:
            # Condense horizontally
            scale_factor = np.random.uniform(0.7, 0.9)  # Adjust range as needed
        
        # Compute new dimensions after scaling
        new_width = tf.cast(tf.cast(tf.shape(image)[1], tf.float32) * scale_factor, tf.int32)
        new_height = tf.cast(tf.cast(tf.shape(image)[0], tf.float32) * scale_factor, tf.int32)
        
        # Resize the image
        image = tf.image.resize(image, (new_height, new_width))
        
        # Crop the stretched image to the original size
        image = tf.image.resize_with_crop_or_pad(image, 150, 150)
        
        # Randomly flip horizontally
        image = tf.image.random_flip_left_right(image)
    
    return image


# Load images from directories
train_datagen = tf.keras.preprocessing.image.ImageDataGenerator(
    #purify the color so it appears brighter and easier to read
    rescale=1./255,
    validation_split=0.2,
    preprocessing_function=custom_preprocessing
)

train_generator = train_datagen.flow_from_directory(
    directory='palmData',
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary',
    subset='training',
    shuffle=True,  # Shuffle the data for better training
    seed=42,  # Set seed for reproducibility
    interpolation='nearest'  # Preserve image integrity
)  # Repeat indefinitely


validation_generator = train_datagen.flow_from_directory(
    directory= 'palmData',
    target_size=(150, 150),
    batch_size=32,
    class_mode='binary',
    subset='validation'
)

# Enhanced model with Dropout layers and regularization
model = Sequential([
   Conv2D(32, (3,3), activation='relu', input_shape=(150, 150, 3)),
   MaxPooling2D(2, 2),
   Conv2D(64, (3,3), activation='relu'),
   MaxPooling2D(2, 2),
   Conv2D(128, (3,3), activation='relu'),
   MaxPooling2D(2, 2),
   Dropout(0.3),
   Conv2D(256, (3,3), activation='relu'),
   MaxPooling2D(2, 2),
   Dropout(0.3),
   Conv2D(512, (3,3), activation='relu'),
   MaxPooling2D(2, 2),
   Dropout(0.4),
   Flatten(),
   Dense(512, activation='relu'),
   Dropout(0.5),
   Dense(1, activation='sigmoid')
])

batch_size = 25  # Define the batch size here

# Define the number of steps per epoch based on the length of your training data and batch size
steps_per_epoch = len(train_generator) // batch_size

# Train the model with callbacks for early stopping, model checkpointing, and reducing learning rate on plateau
early_stopping = EarlyStopping(monitor='val_loss', patience=5, restore_best_weights=True)

model_checkpoint = ModelCheckpoint("modelpalm.keras", save_best_only=True)

reduce_lr = ReduceLROnPlateau(monitor='val_loss', factor=0.2, patience=2, min_lr=1e-6)

# Define maximum number of steps (adjust according to your preference)
max_steps = 200

# Compile the model
model.compile(optimizer='adam', loss='binary_crossentropy', metrics=['accuracy'])

history = model.fit(
    train_generator,
    steps_per_epoch=steps_per_epoch,
    epochs=40,  
    validation_data=validation_generator,
    validation_steps=len(validation_generator),
    callbacks=[early_stopping, model_checkpoint, reduce_lr],
    verbose=1
)

# Evaluate the model
val_loss, val_acc = model.evaluate(validation_generator, steps=validation_generator.samples // 32)
print(f'Validation accuracy: {val_acc}, Validation loss: {val_loss}')

# Print classification report
val_predictions = model.predict(validation_generator)
val_predictions = np.round(val_predictions)
val_true_labels = validation_generator.classes
print("Validation Classification Report:")
print(classification_report(val_true_labels, val_predictions, zero_division=1))

# Confusion Matrix
conf_matrix = confusion_matrix(val_true_labels, val_predictions)
plt.figure(figsize=(8, 6))
sns.heatmap(conf_matrix, annot=True, fmt='d', cmap='Blues', xticklabels=['NAPalm', 'APalm'], yticklabels=['NApalm', 'APalm'])
plt.ylabel('Actual')
plt.xlabel('Predicted')
plt.title('Confusion Matrix')
plt.show()

# Save the model
model.save("modelpalm.keras")

# Prediction function remains the same for testing purposes

def predict_palm(image_path, model):
    img = tf.keras.preprocessing.image.load_img(image_path, target_size=(150, 150))
    img_array = tf.keras.preprocessing.image.img_to_array(img)
    img_array = np.expand_dims(img_array, axis=0)
    img_array /= 255.0
    prediction = model.predict(img_array)
    return (prediction[0][0])

# Example usage
image_path = 'palmData/NAPalm/Non-anemic-Pa-001 (2).png'
prediction = predict_palm(image_path, model)
print(f"Predicted NON anemic palm: {prediction}")

image_path = 'palmData/APalm/Anemic-260 (2).png'
prediction = predict_palm(image_path, model)
print(f"Predicted anemic palm: {prediction}")
