#!/usr/bin/env python
# coding: utf-8

# # U.S. Medical Insurance Costs
# 
# 
# The goal of this project is to determine trends in U.S. Medical insurance costs based on identity markers: age, sex, bmi, children, smoking, and region. Trends will be determinded first through a graphical representation of the variables, followed by a numerical analysis (linear regression, supported vector machines, K-nearest neighbors)
# 

# In[7]:


# Data Extraction
import csv
insurance_data = []
with open("insurance.csv") as insurance_file:
        insurance_reader = csv.DictReader(insurance_file)
        for row in insurance_reader:
            insurance_data.append(row)
print(insurance_data[0:10])


# In[13]:


# Calculate average + standard deviation, visualize insurance costs in histograph
import statistics as stat
import matplotlib.pyplot as plt
import numpy as np

insurance_costs = [float(row['charges']) for row in insurance_data]
avg = stat.mean(insurance_costs)
avg = round(avg,2)
std_dev = stat.stdev(insurance_costs)
std_dev = round(std_dev,2)
print("The average insurance cost is ${} +/- {}".format(avg,std_dev))

plt.hist(insurance_costs, bins = 100)
plt.xlabel("US Insurance Costs ($)")
plt.ylabel("Frequency")
plt.show()


# In[17]:


# Identity Class Representation

class identity:
# Creates a class that returns a list of costs for a particular identify marker and comparison type of a desired value, and also
# contains functions that plot histograms, average value bar graphs, or line graphs

    def __init__(self,identity_marker,comparison_type,desired_value):
        
        costs = []
                    
        if comparison_type == 'equal':
            for row in insurance_data:
                if row[identity_marker] == desired_value:
                    costs.append(float(row['charges']))  
        
        elif comparison_type == 'greater than':
            for row in insurance_data:
                if int(row[identity_marker]) > desired_value:
                    costs.append(float(row['charges']))  
            
        elif comparison_type == 'lesser than':
            for row in insurance_data:
                if float(row[identity_marker]) < desired_value:
                    costs.append(float(row['charges']))      
        
        elif comparison_type == "contains":
            for row in insurance_data:
                if desired_value in row[identity_marker]:
                    costs.append(float(row['charges']))
        
        elif comparison_type == "within range":
            for row in insurance_data:
                compared_value = float(row[identity_marker])
                if compared_value >= desired_value[0] and compared_value <= desired_value[1]:
                    costs.append(float(row['charges']))
        
        self.costs = costs
        self.avg = stat.mean(costs)
        self.std_dev = stat.stdev(costs)
        self.identity_marker = identity_marker
        
    def id_val_mean(self):
        values = [float(row[self.identity_marker]) for row in insurance_data]
        unique_values = list(set(values))
        unique_values_costs = np.zeros(len(unique_values))

        for row in insurance_data:
            for value in unique_values:
                if float(row[identity_marker]) == value:
                    unique_values_costs[unique_values.index(value)] += float(row['charges'])
        return values, unique_values, unique_values_costs


    def get_histo(self,group):
        plt.hist(self.costs,bins = 100)
        plt.title("Histogram for {}".format(group))
        plt.xlabel("Insurance Cost($) for {}".format(group))
        plt.ylabel("Frequency")
        plt.show()
    
    
    def get_weighted_bar(self,title,group):
        values, unique_values, unique_values_costs = self.id_val_mean(self)
        N = len(values)
        weights = np.zeros(N)
        nums = np.zeros(N)
        for i in range(N):
            
        plt.bar(unique_values,weighted_costs)
        plt.title(title)
        plt.xlabel(group)
        plt.ylabel("Weighted Cost ($)")
        plt.show()
    


# Data Visualization

# In[15]:


# Age
        
# All Ages
ages = [float(row['age']) for row in insurance_data]
all_ages = identity('age','within range',[min(ages),max(ages)])
all_ages.get_weighted_bar("Weighted Cost vs Age")



# Compare old to young histograms
avg_age = round(stat.mean(ages))
old_age = identity('age','greater than',avg_age)
plt.subplot(2,1,1)
old_age.get_histo('individuals older than {}'.format(avg_age))


young_age = identity('age','lesser than',avg_age)
plt.subplot(2,1,2)
young_age.get_histo('individuals younger than {}'.format(avg_age))


# In[ ]:


# BMI
bmis, unique_bmis, unique_bmis_costs = id_val_mean('bmi')
bmi = identity('bmi','within range',[min(bmis),max(bmis)])
plt.bar(unique_bmis,unique_bmis_costs)
plt.title("Insurance Cost vs BMI")
plt.xlabel("BMI")
plt.ylabel("Cost ($)")
plt.show()


# In[ ]:


# Age & BMI


# In[ ]:


# Sex

# Children

# Smoker


# In[ ]:


# Region


# In[ ]:


# Data Transformation

# Sex
sex_codes = []
for row in insurance_data:
    if row['sex'] == 'female':
        sex_codes.append(1)
    else:
        sex_codes.append(0)

