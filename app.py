# import the packages 
import os
import streamlit as st
import pandas as pd
from matplotlib import pyplot as pyplot
import seaborn as sns  

def main():
    """ Police Shootings Data Visualizations"""
    st.title("Police Shootings Data Visualizations")
    st.subheader("Simple EDA with Streamlit Web App")
    
    df = pd.read_csv("datasets_723010_1257097_fatal-police-shootings-data.csv") #read in the data
    st.title("Police Shootings")
    if st.checkbox("show dataframe"):
        st.write(df)

    if st.button("Information of the data"):
        st.write(df.info())      

    if st.button("Columns Names"):
        st.write(df.columns) 

    if st.checkbox("Select Columns to show"):
        all_columns = df.columns.tolist() #turning the columns to list
        selected_columns = st.multiselect("select", all_columns)
        new_df = df[selected_columns]
        st.dataframe(new_df)    

    if st.checkbox("Shape of dataset"):
        st.write(df.shape)  
 
    if st.checkbox("Summary"):
        st.write(df.describe())

    st.subheader("Data Visualization")

    #correlation of the data using heatmap
    if st.checkbox("Heat Map"):
        st.write(sns.heatmap(df.corr(),annot=True))
        st.pyplot()

    if st.checkbox("Distplot"):
        st.write(sns.distplot(df["age"])) #distribution of the age      
        st.pyplot()

    if st.checkbox("Race-countplot"):
        st.write(sns.countplot(df["race"], hue=df["gender"]))
        st.pyplot()

    if st.checkbox("Race-stripplot"):
        st.write(sns.stripplot(df["race"], y=df["age"]))
        st.pyplot()

    #if st.checkbox("Stripplot-Manner of death"):
        #st.write(sns.stripplot(x=df["race"], y=df["age"], hue="manner_of_death"))
        #st.pyplot()

    if st.checkbox("Death and Threat"):
        st.write(sns.countplot(df["manner_of_death"], hue=df["threat_level"]))
        st.pyplot()


    #value counts and plot of manner of death
    if st.checkbox("Manner of Death"): 
        st.write(sns.countplot(df["manner_of_death"]))
        st.pyplot()

    if st.button("Death Count"):
        st.write(df["manner_of_death"].value_counts())

    if st.checkbox("Threat Level"):
        st.write(sns.countplot(df["threat_level"],hue=df["gender"]))
        st.pyplot()

    if st.button("Threat Count"):
        st.write(df["threat_level"].value_counts())

    if st.checkbox("Mental Illness"):
        st.write(sns.violinplot(x=df["signs_of_mental_illness"], y=df["age"]))
        st.pyplot()

    if st.button("Mental-Barplot"):
        st.write(sns.countplot(df["signs_of_mental_illness"], hue=df["gender"]))
        st.pyplot()

    if st.checkbox("Flee"):
        st.write(sns.violinplot(x=df["flee"], y=df["age"], hue=df["gender"], split=True))
        st.pyplot()

    if st.checkbox("Body Camera"):
        st.write(sns.countplot(df["body_camera"]))
        st.pyplot()


    if st.button("Arigato :)"):
        st.balloons()

    st.sidebar.header("About Visualizing App")
    st.sidebar.info("Basic Police Shootings Visualization Exploratory Data Analysis")
    
    
if __name__ == '__main__':
    main()
