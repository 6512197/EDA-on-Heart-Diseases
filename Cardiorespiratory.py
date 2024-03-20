import pandas as pd
import numpy as np
import seaborn as sns



# Leer el archivo CSV y mostrar the first 5 one
df = pd.read_csv('Cardiorespiratory_Health.csv')
print(df.head())

# Mostrar las columnas disponibles en el DataFrame
print(df.columns)

# Obtener información específica sobre la columna 'restingBP'
print(df['restingBP'].describe())
######################################################
######################################################
# Lista de países en el orden correspondiente a las condiciones
# logic of choosing this 
paises = ['Japan', 'France', 'South Korea', 'Switzerland', 'Norway',
          'Sweden', 'Finland', 'Italy', 'Spain', 'Greece']

# Definición de las condiciones basadas en los valores de 'restingBP' en tu DataFrame 'df'
condiciones = [
    (df['restingBP'] < 120),
    (df['restingBP'].between(120, 129)),
    (df['restingBP'].between(130, 139)),
    (df['restingBP'] >= 140) & (df['restingBP'] < 180),
    (df['restingBP'] >= 180)
]
def color_string(s):
    if isinstance(s, str):  # Check if the value is a string
        return 'color: blue'


# Apply style to DataFrame based on string conditions
styled_df = df.tail().style.applymap(color_string)

# Display the styled DataFrame
styled_df

#####################################################################
# Definición de los valores correspondientes a cada condición
valores = paises[:4] + [paises[7]]  # Asignar los países según las condiciones dadas

# Crear la nueva columna 'Origins' en tu DataFrame 'df' basada en las condiciones
df['Origins'] = np.select(condiciones, valores, default='Greece')
#i created this bcs they wouldnt let me  run that variable with weird char 

df.rename(columns={'restingBP': 'resting_blood_pressure'}, inplace=True)
## return male or female 

def gender_transform(gender):
    if gender == "0":
        return 'female'
    else:
        return 'male'
    
df['gender'] = df['gender'].apply(gender_transform)
df.rename(columns={'gender': 'gender_transform'}, inplace=True)

#print (df)
print(df['gender_transform'].describe())

#######################################
#######################################

import matplotlib.pyplot as plt

# Grouping the data by 'gender_transform' and 'age' to compare the ages of females and males
grouped = df.groupby('gender_transform')['age']

# Creating a figure and axis for plotting
fig, ax = plt.subplots()

# Plotting histogram for age distribution of each gender group
for group_name, group_data in grouped:
    ax.hist(group_data, label=group_name, alpha=0.7)

# Adding labels and title to the plot
ax.set_xlabel('Age')
ax.set_ylabel('Frequency')
ax.set_title('Age Distribution by Gender')
ax.legend()

# Displaying the plot
plt.show()
df['gender_transform'].value_counts()

#########################
#########################
average_oldpeak_by_gender = df.groupby('gender')['oldpeak'].mean()
average_oldpeak_by_gender
#######################
#######################