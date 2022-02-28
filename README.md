# Pneumonia Detection
![Untitled design](https://user-images.githubusercontent.com/72313581/155876777-a1082dee-eef8-446b-a84a-37afd3738f84.jpg)
## Why?
Pneumonia affects many individuals, especially in developing and underdeveloped nations, where high levels of pollution, unhygienic living conditions, and overcrowding are relatively common, together with inadequate medical infrastructure. According to a study in 2015, among the 5.9 million deaths of children under 5, over 15.6% were due to pneumonia. Early diagnosis of pneumonia is crucial to ensure curative treatment and increase survival rates. Chest X-rays which are primarily used for the diagnosis of this disease need expert radiotherapists for evaluation. Thus, developing an automatic system for detecting pneumonia would be beneficial for treating the disease without any delay particularly in remote areas. It could also aid radiologists in their decision making process.
## Dataset
Chest X-Ray Images (Pneumonia)
https://www.kaggle.com/paultimothymooney/chest-xray-pneumonia
## Custom Vision
Built on Azure's Custom Vision, the classification model is trained on 3675 'Pneumonia' and 1340 'Normal' images with General [A1] domain. The model has the following performance scores:
![image](https://user-images.githubusercontent.com/72313581/155974432-a64d8aa7-647f-44bb-bab7-66c4c26642ad.png)
## Deployment
The model is deployed as a web-service. The website is developed using HTML/CSS/Bootstrap and Flask framework, and hosted using Azure App Service. Bootstrap Studio was also used during development.
## Disclaimer
This capability is not designed or intended to be implemented or deployed as a substitute for professional medical advice or healthcare opinion, diagnosis, treatment, or the clinical judgment of a healthcare professional, and should not be used as such.
