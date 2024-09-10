import yfinance as yf
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

st.write("""

# Simple Financial Data Visualistion App
         
         Shown below is the HeatMap depicting the corellation between the fields in the dataset
         - And as visible by the chart Debentures and Government Bonds show the most correlation.

""")


df = pd.read_csv("Finance_data.csv")

# let us look at the first 10 data entries in the table
df.head(10)

# get more detailed information of the variables in the table
df.info()
df.describe()


# Heat map in streamlit - to view the corelation between the fields
numerical_df = df.select_dtypes(include=[ 'int64'])
fig, ax = plt.subplots()
sns.heatmap(numerical_df.corr(), annot=True, cmap='coolwarm', fmt=".2f")

st.pyplot(fig)


st.write("""
            Given below is count of the gender distribution in the dataset based on number of males and females
         """)

# Barchart to compare the gender of the respondents
fig2, ax2 = plt.subplots()
sns.countplot(df['gender'],linewidth=3, palette="Set1")
st.pyplot(fig2)


# st.write("""

# We will now also view the age distribution of respondents in the dataset
#          """)

# # Linechart to represent the distribution of respondents accross the age
# # fig3, ax3 = plt.subplots()
# # sns.barplot(df['age'], palette = "Set3", ax=ax3)
# # st.pyplot(fig3)

# # Create the plot
# fig3, ax3 = plt.subplots()

# # Create a horizontal line plot
# sns.lineplot(x = df, y=df['age'], data=df, ax=ax3, marker='o')

# # Set labels
# ax.set_xlabel("Count")
# ax.set_ylabel("Age")

# # Display the plot in Streamlit
# st.pyplot(fig3)


