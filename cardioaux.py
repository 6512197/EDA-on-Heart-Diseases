from Cardiorespiratory import*

from sklearn.preprocessing import MinMaxScaler



#test

# Visualizationy y comapracion :
plt.figure(figsize=(10, 6))
sns.barplot(x='gender', y='maxheartrate', data=df, palette='viridis')
plt.title('males vs females heart rate')
plt.xlabel('gender')
plt.ylabel('Maximum Heart Rate')
plt.legend(title='gender', labels=['female=0', 'male=1'])
plt.show()

###################################
###################################
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
#####################################################
########################################################

X_disease = df.drop(columns='target')
y = df.target

scaler = MinMaxScaler(feature_range=(0, 1)).fit_transform(X_disease)
X = pd.DataFrame(scaler, columns=X_disease.columns)
X.describe().T.style.background_gradient(axis=0, cmap='plasma')