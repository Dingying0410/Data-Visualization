
# coding: utf-8

# In[2]:


import pandas as pd
import matplotlib.pyplot as plt

# 1) Create a pandas DataFrame from the file
df = pd.read_csv('fortune1000.csv')


# In[5]:


df


# In[6]:


# 2) Display the first 5 rows of the data
df.head(5)


# In[10]:


# 3) How many unique sectors are in the data set?
"Number of unique sectors: " + str(df.Sector.nunique())


# In[11]:


# 4) How many unique industries are in the data set?
"Number of unique industries: " + str(df.Industry.nunique())


# In[325]:


# 5) How many companies are in each sector?
df_sector = df.groupby('Sector')[['Company']].nunique()
df_sector.columns = ['Number of Companies']
df_sector


# In[326]:


# 6) How many companies are in each industry?
df_industry = df.groupby('Industry')[['Company']].nunique()
df_industry.columns = ['Number of companies']
df_industry


# In[343]:


# 7) How many industries are in each sector? 
df_sector2 = df.groupby('Sector')[['Industry']].nunique()
df_sector2.columns = ['Number of industries']
df_sector2


# In[334]:


# 9) What are the top 5 sectors based on the total employee size. Show the sectors and the total employee number
df_employee = df.groupby('Sector')[['Employees']].sum()
df_employee.columns = ['Employee Number']
df_employee.nlargest(5, 'Employee Number')


# In[345]:


# 10) What are the top 10 industries basd on the total revnue . Show the industres and their revenues
df_revenue = df.groupby('Industry')[['Revenue']].sum()
df_revenue.columns = ['Total Revenue']
df_revenue.nlargest(10, 'Total Revenue')


# In[344]:


# 11) List the top 20 companies based on their profits, show their sectors and industries, and profits
df_company = df[['Company', 'Sector', 'Industry', 'Profits']]
df_company.nlargest(20, 'Profits')


# In[13]:


# 12) List the average revenue, profit, and employee size for each industry. 
df_mean1 = df.groupby('Industry')[['Revenue', 'Profits', 'Employees']].mean()
df_mean1.columns = [['Mean Revenue', 'Mean Profits', 'Mean Employee Size']]
df_mean1


# In[18]:


# 13) Group the companies by sector and industry, list their average revenue, profit, and employee size.
df_mean2 = df.groupby(['Sector', 'Industry']).mean()[['Revenue', 'Profits', 'Employees']]
df_mean2.columns = [['Mean Revenue', 'Mean Profits', 'Mean Employee Size']]
df_mean2


# In[351]:


# 14) Find the top 10 industries based on the average profits/revenue ratio?
def ratio (df):
    return (df['Profits'] * 1.0) / (df['Revenue'] * 1.0)
df2 = df.copy()
df2['Ratio'] = df2.apply(ratio, axis = 1)
df2.groupby('Industry')[['Ratio']].mean().nlargest(10, 'Ratio')


# In[352]:


# 15) Find the top 10 companies based on the profits/revenue ratio?
df2.groupby('Company')[['Ratio']].mean().nlargest(10, 'Ratio')


# In[34]:


# 16) Draw a pie chart of the sectors based on the total employee sizes
employee_size = df.groupby('Sector')['Employees'].sum()
employee_size.name = ""
plt.figure(figsize= (15, 15))
plt.title("Pie Chart for Employee Size of Sectors", fontsize = 20)
employee_size.plot.pie(autopct="%1.1f%%")
plt.show()


# In[32]:


# 17) Draw a bar chart to show the revnues of the top 20 companies
df_max_revenues = df.groupby('Company')['Revenue'].sum().nlargest(20)
plt.figure(figsize = (10, 6))
df_max_revenues.plot.bar()
plt.title("Bar Chart for Revenues of the top 20 companies", fontsize = 20)
plt.ylabel('Revenue')
plt.show()


# In[31]:


# 18) Draw a histogram of the companies based on their profits
df_profits = df.groupby('Company')['Profits'].sum()
plt.figure(figsize = (10, 6))
plt.title("Histogram of companies based on profits", fontsize = 20)
df_profits.plot.hist()
plt.xlabel("Company Profits")
plt.show()


# In[30]:


# 19)   Draw a histogram of the industries based on their total employee sizes 
df_employee_size = df.groupby('Industry')['Employees'].sum()
plt.figure(figsize = (10, 6))
plt.title("Histogram of industries based on total employee sizes", fontsize = 20)
df_employee_size.plot.hist()
plt.xlabel("Employee Size")
plt.show()


# In[29]:


# 20)  Draw a scatter plot based on revenue and profit of the top 20 companies based on the employee size, 
#      use the employee number as the size of the circle
df_company = df[['Company', 'Revenue', 'Profits', 'Employees']]
plt.figure()
df_company.nlargest(20, 'Employees').plot(kind = 'scatter', x = 'Revenue', y = 'Profits', s = df_company['Employees'] / 10000)
plt.title("Profits VS Revenue of the top 20 companies based on employee size")
plt.show()

