# Speech/Music-Emotion-Recognition
Implementation of deep convolutional neural networks for automatic recognition of emotional characteristics in speech and music/singing audio recordings. Audio recordings were loaded from public datasets and standardized. Data augmentation techniques, such as adding Gaussian noise and modifying pitch, were used to expand the dataset. For each audio sample, features like Zero Crossing Rate, Root Mean Square Energy, and Mel-frequency Cepstral Coefficients were computed and combined into a single array for model training. Training employed the Adam optimizer with an initial learning rate of 0.0005, categorical crossentropy as the loss function, and accuracy as the performance metric. Training lasted 100 epochs for singing/music models and 50 epochs for speech models. A learning rate reduction strategy was implemented based on validation accuracy, halving the learning rate if no improvement was observed for 3 consecutive epochs. The models were evaluated using accuracy, loss, ROC curve, confusion matrices, and classification report. 

<p align="center">
    <img src="https://github.com/PatrykSpierewka/Speech-Emotion-Recognition/assets/101202344/1b66f045-444d-4732-9cfc-a7a8f8291583">
</p>

<p align="center">
    <img src="https://github.com/PatrykSpierewka/Speech-Emotion-Recognition/assets/101202344/b3cef7b2-b12c-4e41-9d48-3f5284671d29">
</p>

<p align="center">
    <img src="https://github.com/PatrykSpierewka/Speech-Emotion-Recognition/assets/101202344/81c9e0b1-1fd5-4ec3-b04f-d10aa99f16a8">
</p>

### Speech

<p align="center">
    <img alt="Zrzut ekranu 1" src="https://github.com/PatrykSpierewka/Speech-Emotion-Recognition/assets/101202344/9ed21780-964a-46ff-af20-2af3987d8d6d">
</p>

### Music

<p align="center">
    <img alt="Zrzut ekranu 2" src="https://github.com/PatrykSpierewka/Speech-Emotion-Recognition/assets/101202344/bb79e3f8-b15c-40ac-a8f3-f96fdde7402a">
</p>
