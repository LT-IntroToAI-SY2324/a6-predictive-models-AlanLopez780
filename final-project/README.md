# Project - Create your own predictive model

Alan Lopez

Predictive models are used across industries to analyze and make predictions about data. From sports to beauty products to app usage, predictive models provide individuals and businesses with data to make informed decisions.

Throughout this module, you have learned how to program both supervised and unsupervised learning models. In this final project, you will create your own! Throughout this project, you will work through activities to complete the following steps:

1. Choose a dataset.
I chose a student clustering dataset.
2. Determine which algorithm is the best fit. Based on the dataset you choose, you will need to figure out which algorithm to use. This will require you to get to know your data and your goals! Is there a linear correlation between variables? Are you looking for numerical value or a label/category? Do you know the labels or do you need the model to create them for you?
- Do some tests with matplotlib and visualize your data.  Does it provide a good correlation?  Why or why not?
I tried the linear regression algorithm, but it turns out the data from the dataset I used is not linear. So I went with the clusters algorithm, because most of the data seems to be grouped together.
3. Program your model. Once you have chosen your type of model, it’s time to create it! In this step, you will write a program that fits your chosen model to the data. Your program and output will be specific to the model you choose.  
4. Analyze and present your findings. An important part of creating predictive models is being able to communicate the results. In this final step of the project, you will present your findings using slides or an infographic. Your product should include the following components:
- Your reasoning for the algorithm you chose
- An explanation and analysis of the output of your model: What results did your model produce? What do they mean?
- A prediction based on your model
- A summary of the accuracy of your model
- Real world implications

I chose the clusters algorithm because the data I got is more grouped together. When I ran the program, the resulting graph groups the data into 4 clusters, hence the k-value is 4. The model actually managed to group the data pretty well without leaving any outliers, so I would say the accuracy of the model is really good. An implication of the model could be that CGPA does not necessarily dictate the IQ. For example, a student with a low GPA can have either a high or low IQ. Some factors that could impact a student's IQ is how much they pay attention in class, their age, their mental health, etc.