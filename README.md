# Investigating US Insurance Costs

The goal of this project is to identify trends in insurance costs in the United States based on various identity factors.

Dataset: https://www.kaggle.com/datasets/mirichoi0218/insurance

### Conclusion from Correlation Analyses:

After examining the correlation coeeficient for the quantitative and categorical factors, it is clear that smoking is most positively correlated (0.787) followed by age (0.300) and bmi (0.199). These factors will be examined first as single variable analyses, followed by multivariable analyses.

## Visualizations for Single Variable Analyses
### Age
![image](https://user-images.githubusercontent.com/28024140/221909980-0b983235-d695-407b-99ac-a3fb20c173bd.png)
![image](https://user-images.githubusercontent.com/28024140/221910001-d04f7a1e-e1c0-4bd6-8c56-b77a6f6c30d4.png)

### Bmi
![image](https://user-images.githubusercontent.com/28024140/221910159-023d0db9-55c0-4a47-b175-ef34e488349d.png)
![image](https://user-images.githubusercontent.com/28024140/221910167-d9aa3748-bd63-4f75-85d1-64b636546636.png)

### Smoking
![image](https://user-images.githubusercontent.com/28024140/221910211-0c8ee666-0753-4e15-a921-ac044fc73bf4.png)

## Visualizations for Multivaraible Analyses
![image](https://user-images.githubusercontent.com/28024140/221910362-109750c0-dbbf-42f3-a85e-e4216d443372.png)
<br>
![image](https://user-images.githubusercontent.com/28024140/222746487-0dcf6434-0ec6-42ff-9042-74fe86099e27.png)

Upon visualizing the 3 factors of medical insurance charge with the highest correlations, a few trends become evident: firstly, when looking at the charges vs. ages, 3 clusters are immediately apparent. When these points are visualized by the patient's smoking habits, it is clear that those who smoke generally pay more than those who don't; however, the smoking groups have a clear boundary, and it is not represented in the bmi data of the patients. Further investigation could be conducted to determine the validity of this correlation and what other factors might determine this boundary among smokers.

## Verifying Correlations with Machine Learning

Features: Age, BMI, Smoking

Labels: Charges (1 for above average, 0 for below)

### Visualization of Decision Tree Classification

![image](https://user-images.githubusercontent.com/28024140/221910664-890e484c-1fd8-4afe-ab03-713e80f0804d.png)

### Multiple Linear Regression

Training R?? : 74%
Testing R?? : 76%

For a 26 year old with a BMI of 22, they are predicted to pay $26077.92 if they smoke and $2354.44 if they do not.

### Conclusions

The decision tree was trained to split groups based on whether they paid above or below the average insurance charges. The first branching of the tree divides smokers and non smokers who pay higher and lower than the average cost of insurance (respectively); this split also yields the most information gain (shown by the biggest drop in entropy), so it is evident that the decision tree confirms the conclusion of the exploratory analysis.

Likewise, the multiple linear regression predicts that individuals who smoke will pay substantially more in insurance charges than those who don't, even if they are otherwise young and have a healthy BMI. 
