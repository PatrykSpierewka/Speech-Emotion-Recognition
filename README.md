# Speech/Music-Emotion-Recognition
Implementation focused on developing deep convolutional neural networks for automatic recognition of emotional characteristics in speech and music/singing audio recordings. Audio recordings were loaded from public datasets and standardized. Data augmentation techniques, such as adding Gaussian noise and modifying pitch, were used to expand the dataset. For each audio sample, features like Zero Crossing Rate, Root Mean Square Energy, and Mel-frequency Cepstral Coefficients were computed and combined into a single array for model training. Training employed the Adam optimizer with an initial learning rate of 0.0005, categorical crossentropy as the loss function, and accuracy as the performance metric. Training lasted 100 epochs for singing/music models and 50 epochs for speech models. A learning rate reduction strategy was implemented based on validation accuracy, halving the learning rate if no improvement was observed for 3 consecutive epochs. The models were evaluated using accuracy, loss, and confusion matrices. 

### Speech

### Music

