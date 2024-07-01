# Speech/Music-Emotion-Recognition
Implementation focused on developing deep convolutional neural networks for automatic recognition of emotional characteristics in speech and music/singing audio recordings. Audio recordings were loaded from public datasets and standardized. Data augmentation techniques, such as adding Gaussian noise and modifying pitch, were used to expand the dataset. For each audio sample, features like Zero Crossing Rate, Root Mean Square Energy, and Mel-frequency Cepstral Coefficients were computed and combined into a single array for model training. Training employed the Adam optimizer with an initial learning rate of 0.0005, categorical crossentropy as the loss function, and accuracy as the performance metric. Training lasted 100 epochs for singing/music models and 50 epochs for speech models. A learning rate reduction strategy was implemented based on validation accuracy, halving the learning rate if no improvement was observed for 3 consecutive epochs. The models were evaluated using accuracy, loss, ROC curve, confusion matrices, and classification report. 

### Speech


### Music
<div style="text-align: center;">
    <img src="https://github.com/PatrykSpierewka/Speech-Emotion-Recognition/assets/101202344/67571dc2-1049-45c8-a779-c66f6243b32b" alt="Music Image 1" width="200" height="200">
    <img src="https://github.com/PatrykSpierewka/Speech-Emotion-Recognition/assets/101202344/ee475cf6-d09f-436f-885c-e93fe1756acb" alt="Music Image 2" width="200" height="200">
    <img src="https://github.com/PatrykSpierewka/Speech-Emotion-Recognition/assets/101202344/68cca303-9ece-4f36-a73b-c5420ab7c017" alt="Music Image 3" width="200" height="200">
    <img src="https://github.com/PatrykSpierewka/Speech-Emotion-Recognition/assets/101202344/509dff95-7161-4466-a5f2-8c0ae202538b" alt="Music Image 4" width="200" height="200">
</div>


