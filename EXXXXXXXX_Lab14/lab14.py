from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Flatten, Dropout, BatchNormalization
from tensorflow.keras.optimizers import Adam

# 建立模型
model = Sequential()

# 添加層數
model.add(Flatten(input_shape=(28, 28, 1)))  # 攤平輸入
model.add(Dense(128, activation='relu', kernel_initializer='he_normal'))  # 隱藏層1
model.add(BatchNormalization())  # 批量標準化
model.add(Dropout(0.3))  # Dropout 層

model.add(Dense(64, activation='relu', kernel_initializer='he_normal'))  # 隱藏層2
model.add(BatchNormalization())  # 批量標準化
model.add(Dropout(0.3))  # Dropout 層

model.add(Dense(10, activation='softmax'))  # 輸出層

# 編譯模型
model.compile(optimizer=Adam(learning_rate=0.001),
              loss='categorical_crossentropy',
              metrics=['accuracy'])

# 顯示模型摘要
print(model.summary())

# 訓練模型
train_history = model.fit(x=X_Train_normalize, y=y_TrainOneHot,
                          validation_split=0.2, epochs=30, batch_size=200,
                          verbose=2)
model.save('mnist_mlp_model.keras')

def show_train_history(train_history, train, validation):
    plt.plot(train_history.history[train])
    plt.plot(train_history.history[validation])
    plt.title('Train History')
    plt.ylabel(train)
    plt.xlabel('Epoch')
    plt.legend(['train', 'validation'], loc='upper left')
    plt.show()

# 顯示訓練過程中的準確度和損失
show_train_history(train_history, 'accuracy', 'val_accuracy')
show_train_history(train_history, 'loss', 'val_loss')

# 評估模型
scores = model.evaluate(X_Test_normalize, y_TestOneHot)
print()
print('accuracy = ', scores[1])

# 進行預測
prediction = model.predict(X_Test)
predicted_label = np.argmax(prediction, axis=-1)

# 顯示混淆矩陣
import pandas as pd
y_test_label = y_test_label.reshape(10000)
pd.crosstab(y_test_label, predicted_label, rownames=['label'], colnames=['predict'])

# 顯示預測結果
plot_images_labels_prediction(X_test_image, y_test_label, predicted_label, idx=340)
