import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

sns.set(style='dark')

# Helper function untuk menampilkan data overview
def show_data_overview(df):
    st.subheader('Data Overview')
    st.write(df.describe())
    st.write(f'Total entri: {df.shape[0]}')
    st.write(f'Total kolom: {df.shape[1]}') 

# key metrics
def display_key_metrics(df):
    st.subheader('Key Metrics')
    total_users = df['total'].sum()  
    total_casual = df['casual'].sum()  
    total_registered = df['registered'].sum()  

    # Menampilkan metrics
    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric(label='Users', value=f'{total_users:,}')

    with col2:
        st.metric(label='Casual Users', value=f'{total_casual:,}')

    with col3:
        st.metric(label='Registered Users', value=f'{total_registered:,}')
        
# 1. Perbedaan Total Penyewaan Hari Libur/Kerja Setiap Bulan
def weekday_weekend(df):
    df['is_weekend'] = df['weekday'].apply(lambda x: 'Weekend' if x in ['Sat', 'Sun'] else 'Weekday')
    st.subheader('Weekday vs Weekend Rentals')
    weekend_data = df.groupby('is_weekend')['total'].sum().reset_index()
    fig, ax = plt.subplots()
    sns.barplot(data=weekend_data, x='is_weekend', y='total', ax=ax, palette=['#E4B1F0', '#433878'])
    ax.set_title('Total Rentals per Weekday/Weekend')
    ax.set_xlabel('Days')
    ax.set_ylabel('Total Users')
    st.pyplot(fig)

# 2. Penyewaan Berdasarkan Tipe Pengguna (Casual vs Registered)
def user_types(df):
    st.subheader('Casual vs Registered Users Rentals')
    fig, ax = plt.subplots(1, 2, figsize=(12, 6))
    sns.barplot(data=df, x='season', y='casual', ax=ax[0], palette=['#E4B1F0'])
    ax[0].set_title('Casual Rentals per Season')
    sns.barplot(data=df, x='season', y='registered', ax=ax[1], palette=['#433878'])
    ax[1].set_title('Registered Rentals per Season')
    st.pyplot(fig)


# 3. Pola Penggunaan Sepeda Berdasarkan Musim
def seasonal_trends(df):
    st.subheader('Seasonal Rental Trends')
    fig, ax = plt.subplots()
    df['month'] = df['date'].dt.strftime('%b')  

    season_colors = {
        'Spring': '#FFB6C1',  
        'Summer': '#FFD700',  
        'Fall': '#FF8C00',    
        'Winter': '#ADD8E6'   
    }

    sns.barplot(data=df, x='month', y='total', hue='season', ax=ax, palette= season_colors)
    ax.set_title('Total Rental Counts per Month')
    ax.set_xlabel('Month')
    ax.set_ylabel('Total Users')
    ax.set_xticklabels(ax.get_xticklabels(), rotation=45, ha='right')
    st.pyplot(fig)

# 4. Pie Chart Total Penyewaan (Casual & Registered)
def rental_pie_chart(df):
    st.subheader('Total Casual vs Registered Users')
    total_casual = df['casual'].sum()
    total_registered = df['registered'].sum()
    labels = ['Casual', 'Registered']
    sizes = [total_casual, total_registered]
    colors = ['#E4B1F0', '#433878']
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', startangle=90, wedgeprops={'edgecolor': 'black'})
    ax.set_title('', fontsize=16)
    ax.axis('equal')
    st.pyplot(fig)
    
# 5. RFM Analysis
def rfm_analysis(df):
    st.subheader('RFM Analysis by Day Type')
    last_rental_date = df['date'].max()
    rfm_df = df.groupby('day_type').agg({
        'date': 'count',  # Frequency
        'total': 'sum'    # Monetary
    }).reset_index()

    recency = df.groupby('day_type')['date'].max().reset_index()
    recency['recency'] = (last_rental_date - recency['date']).dt.days
    rfm_df = rfm_df.merge(recency[['day_type', 'recency']], on='day_type')
    rfm_df.columns = ['day_type', 'frequency', 'monetary', 'recency']
    st.write(rfm_df)
    fig, ax = plt.subplots(nrows=1, ncols=3, figsize=(30, 6))
    colors = ['#E4B1F0', '#433878']
    sns.barplot(x='day_type', y='recency', data=rfm_df.sort_values(by='recency', ascending=True), palette=colors, ax=ax[0])
    ax[0].set_ylabel(None)
    ax[0].set_xlabel(None)
    ax[0].set_title('By Recency', loc='center', fontsize=18)
    ax[0].tick_params(axis='x', labelsize=35)
    
    sns.barplot(x='day_type', y='frequency', data=rfm_df.sort_values(by='frequency', ascending=False), palette=colors, ax=ax[1])
    ax[1].set_ylabel(None)
    ax[1].set_xlabel(None)
    ax[1].set_title('Frequency', loc='center', fontsize=18)
    ax[1].tick_params(axis='x', labelsize=35)

    sns.barplot(x='day_type', y='monetary', data=rfm_df.sort_values(by='monetary', ascending=False), palette=colors, ax=ax[2])
    ax[2].set_ylabel(None)
    ax[2].set_xlabel(None)
    ax[2].set_title('Monetary', loc='center', fontsize=18)
    ax[2].tick_params(axis='x', labelsize=35)
    plt.suptitle('RFM Analysis by Day Type', fontsize=35)
    st.pyplot(fig)

# 6. Correlation Analysis
def correlation_analysis(df):
    st.subheader('Correlation Analysis')
    correlation = df[['casual', 'registered', 'total', 'temp', 'humidity']].corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation, annot=True, fmt='.2f', cmap='Purples', linewidths=0.5, cbar_kws={'shrink': .8}, ax=ax)
    ax.set_title('Heatmap Correlation', fontsize=16)
    ax.set_xlabel('Correlation', fontsize=14)
    ax.set_ylabel('Correlation', fontsize=14)
    st.pyplot(fig)

# Fungsi untuk menambahkan filter di sidebar
def add_sidebar_filters(df):
    with st.sidebar:
        st.logo("bikery-high-resolution-logo.png")
        st.subheader('Filter Data')

        # Filter Bulan
        months = df['month'].unique()
        month_filter = st.multiselect('Choice Month', options=months)

        # Filter Musim
        seasons = df['season'].unique()
        season_filter = st.multiselect('Choice Season', options=seasons, default=seasons)

        apply_filter = st.checkbox('Show Data')

    # Menerapkan filter jika checkbox dicentang
    if apply_filter:
        if month_filter:
            df = df[df['month'].isin(month_filter)]
        if season_filter:
            df = df[df['season'].isin(season_filter)]
    return df

# Main function
def main():
    st.title('Bike Sharing Data Analysis')
    
    all_df = pd.read_csv('day_df_clean.csv')
    all_df['date'] = pd.to_datetime(all_df['date'])
    all_df['month'] = all_df['date'].dt.month_name()  
    
    filtered_df = add_sidebar_filters(all_df)
    
    # Tampilkan hasil analisis
    display_key_metrics(all_df)
    weekday_weekend(filtered_df)
    user_types(filtered_df)
    seasonal_trends(filtered_df)
    rental_pie_chart(all_df)
    rfm_analysis(all_df)
    correlation_analysis(all_df)

    show_data_overview(filtered_df)
    
if __name__ == '__main__':
    main()
