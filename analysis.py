import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('WA_Fn-UseC_-HR-Employee-Attrition.csv')
print("File loaded successfully.")
print(df.head())
df.info()
# from 'Yes'/'No' text to 1/0 numbers.
# We group the data by 'Department' and find the average of our new
# numerical attrition column. Multiplying by 100 gives the percentage.
df['Attrition_numerical'] = df['Attrition'].apply(lambda x: 1 if x == 'Yes' else 0)
attrition_by_dept = df.groupby('Department')['Attrition_numerical'].mean().sort_values(ascending=False) * 100
print("\nAttrition Rate (%) by Department:")
print(attrition_by_dept)

plt.figure(figsize=(10, 6))
sns.barplot(x=attrition_by_dept.index, y=attrition_by_dept.values, hue=attrition_by_dept.index, palette='viridis', legend=False)
plt.title('Attrition Rate by Department', fontsize=16)
plt.ylabel('Attrition Rate (%)')
plt.xlabel('Department')
plt.tight_layout()
plt.savefig('satisfaction_vs_attrition.png')
print("Chart saved as 'satisfaction_vs_attrition.png'")

plt.figure(figsize=(10, 6))
sns.boxplot(x='Attrition', y='JobSatisfaction', data=df, hue='Attrition', palette='pastel', legend=False)
plt.title('Years Since Last Promotion for Employees Who Stayed vs. Left', fontsize=16)
plt.ylabel('Years Since Last Promotion')
plt.xlabel('Attrition')
plt.tight_layout()
plt.savefig('promotion_vs_attrition.png')
print("Chart saved as 'promotion_vs_attrition.png'")