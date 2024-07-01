# Speech/Music-Emotion-Recognition
Implementation focused on developing deep convolutional neural networks for automatic recognition of emotional characteristics in speech and music/singing audio recordings. Audio recordings were loaded from public datasets and standardized. Data augmentation techniques, such as adding Gaussian noise and modifying pitch, were used to expand the dataset. For each audio sample, features like Zero Crossing Rate, Root Mean Square Energy, and Mel-frequency Cepstral Coefficients were computed and combined into a single array for model training. Training employed the Adam optimizer with an initial learning rate of 0.0005, categorical crossentropy as the loss function, and accuracy as the performance metric. Training lasted 100 epochs for singing/music models and 50 epochs for speech models. A learning rate reduction strategy was implemented based on validation accuracy, halving the learning rate if no improvement was observed for 3 consecutive epochs. The models were evaluated using accuracy, loss, ROC curve, confusion matrices, and classification report. 

### Speech


### Music
<p align="center">
  <img src="https://github.com/PatrykSpierewka/Speech-Emotion-Recognition/blob/main/assets/101202344/c60f0ae0-5fab-4d59-bd92-b9556b35cfd4" alt="Music Image 1" width="200"><br>
  Music Image 1
</p>

<p align="center">
  <img src="https://github.com/PatrykSpierewka/Speech-Emotion-Recognition/blob/main/assets/101202344/31fa649b-d0e1-43d4-b0cf-f8b7d32917d3" alt="Music Image 2" width="250"><br>
  Music Image 2
</p>

<p align="center">
  <img src="https://github.com/PatrykSpierewka/Speech-Emotion-Recognition/blob/main/assets/101202344/6f245dc7-1754-4c03-b7f4-3c6cec80aa17" alt="Music Image 3" width="300"><br>
  Music Image 3
</p>

<p align="center">
  <img src="https://github.com/PatrykSpierewka/Speech-Emotion-Recognition/blob/main/assets/101202344/bf6867dd-bd1b-4379-b129-3e234e1bdde1" alt="Music Image 4" width="180"><br>
  Music Image 4
</p>


