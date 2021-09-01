#!/usr/bin/env python
# coding: utf-8

# In[1]:


### 1. Mailing Address

print('To')
print('Maaz_Khan')
print('B-21, Near Samsung India Elecgtronics Pvt. Ltd')
print('Sec-81, Phase-2, Noida')
print('201305')


# In[5]:


### 2. Hello!

Name = input('Enter Youre Name- ')               # input function is used to enter the value 
print(f'Hello, {Name}! ')


# In[9]:


### 3. Calculating Area of Room

L = float(input('Length of Room(M): '))          ### float function has been used in case area is in after decimal values!
W = float(input('Width of Room(M): '))
Area = L*W
print('\nArea of Room : {} Sq.Mtr'.format(Area)) ### .format is been used to define the text or value after the calculation done


# In[10]:


### 4. Area of Field 

L = float(input("Length of field(ft.): "))
W = float(input("Width of field(ft.): "))
Area = (L*W)/43560                               ### 1 acre Is equal to 43560 Sq.ft.
print("\nArea of field: {} acre".format(Area))


# In[1]:


### 5. Bottle Deposits

low_con = int(input("Number of containers(<= 1 liter): "))
high_con = int(input("Number of containers(> 1 liter): "))
refund_amt = (low_con*0.1) + (high_con*0.25)

#print(refund_amt)

print("\nRefund amount: " + "{:.2f}".format(refund_amt) + "$")      ## {:.2f}.format(variable) for display upto 2 decimal point


# In[4]:


# 6. MEAL COST CALCULATION ALONG WITH THE FOOD TAX AND TIP COST 


MEAL_COST = float(input("MEAL COST: "))
TAX_COST = MEAL_COST*0.18                 # APPLICABLE FOOD TAX IN NOIDA IS 18%
TIP_COST = MEAL_COST*0.18
TOTAL_COST = MEAL_COST + TAX_COST + TIP_COST
TAX_AMOUNT = "{:.2f}".format(TAX_COST)
TIP_AMOUNT = "{:.2f}".format(TIP_COST)
TOTAL_AMOUNT = "{:.2f}".format(TOTAL_COST)

print("\nTAX_AMOUNT: {}rs, TIP_AMOUNT: {}rs and TOTAL_AMOUNT: {}rs".format(TAX_AMOUNT, TIP_AMOUNT, TOTAL_AMOUNT))


# In[2]:


# 7. FEUL EFFECIENCY CALCULATION


Feul_Efficiency = float(input("Enter Feul Efficiency in Miles per Gallon(MPG): ")) # 1 mpg=235.215 l/100km 
print(f"Feul Efficiency in Canadian unit: {235.215/Feul_Efficiency} Ltrs./100km")  # THE UNIT OF FUEL IN CANADIAN UNITS IS=  35282.25 


# In[22]:


print("Enter your height in feets and inches\n")
feet = int(input("Feets: "))
inches = float(input("Inches: "))
height = (inches*2.54) + (feet*12*2.54)
print("\nHeight: {} cm".format(height))


# In[ ]:




