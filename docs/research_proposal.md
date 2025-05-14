# Computer-Aided Diagnosis System for Esophagogastroduodenoscopy (EGD) Procedure  

**Discipline:** Medicine  
**Sub-discipline:** Gastroenterology  
 

In recent years, artificial intelligence (AI) has emerged as a transformative force in gastroenterology, particularly in enhancing diagnostic precision during esophagogastroduodenoscopy (EGD). However, current AI systems in EGD, such as ENDOANGEL and ENAD CAD-G, are based on simplistic examination protocols like the ESGE 4-image framework and KSGE protocol. These protocols fail to ensure complete mucosal visualization because of inadequate photo documentation, resulting in missed abnormalities and variable EGD quality in various clinical environments.  

To overcome this fundamental limitation, this paper introduces an AI system trained on the SSS-Kensho-Yahoo protocol—a screening protocol that divides the stomach into 21 zones to provide complete visual examination and emphasizes complete mucosal coverage for improving lesion detection. We trained three models—ConvNeXt-Large, ResNet-50, and Vision Transformer (ViT)—on a dataset of EGD images to classify gastric regions. Our findings show macro-F1 scores of 61% for ConvNeXt-Large, 66% for ResNet-50, and 68% for ViT, with ViT performing the best in learning global features.  

In contrast to traditional models which focused on lesion detection and disease classification, our approach redefines procedural standardization by prioritizing anatomical completeness, thus minimizing missed spots during EGD. Our model has the potential to assist inexperienced gastroenterologists by minimizing the time taken for EGD, ensuring complete stomach coverage, thereby enhancing procedural efficiency. By ensuring protocol adherence, our system improves the quality of the EGD procedure, marking a transformative leap forward in clinical gastroenterology and paving the way for superior patient outcomes and care.  




## References  

Lonseko, Z. M., Adjei, P. E., Du, W., Luo, C., Hu, D., Zhu, L., Gan, T., & Rao, N. (2021). Gastrointestinal Disease Classification in Endoscopic Images Using Attention-Guided Convolutional Neural Networks. *Applied Sciences, 11*(23), Article 23. [https://doi.org/10.3390/app112311136](https://doi.org/10.3390/app112311136)  

Väänänen, A., Haataja, K., Vehviläinen-Julkunen, K., & Toivanen, P. (2021). AI in healthcare: A narrative review (10:6). *F1000Research*. [https://doi.org/10.12688/f1000research.26997.2](https://doi.org/10.12688/f1000research.26997.2)  

Visaggi, P., de Bortoli, N., Barberio, B., Savarino, V., Oleas, R., Rosi, E. M., Marchi, S., Ribolsi, M., & Savarino, E. (2022). Artificial Intelligence in the Diagnosis of Upper Gastrointestinal Diseases. *Journal of Clinical Gastroenterology, 56*(1), 23. [https://doi.org/10.1097/MCG.0000000000001629](https://doi.org/10.1097/MCG.0000000000001629)  

Widya, A. R., Monno, Y., Imahori, K., Okutomi, M., Suzuki, S., Gotoda, T., & Miki, K. (2019). 3D Reconstruction of Whole Stomach from Endoscope Video Using Structure-from-Motion. *2019 41st Annual International Conference of the IEEE Engineering in Medicine and Biology Society (EMBC)*, 3900–3904. [https://doi.org/10.1109/EMBC.2019.8857964](https://doi.org/10.1109/EMBC.2019.8857964)  


