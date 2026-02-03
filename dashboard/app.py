"""
Ethiopia Financial Inclusion Forecast Dashboard

Interactive dashboard for exploring financial inclusion data, 
understanding event impacts, and viewing forecasts.
"""

import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import plotly.express as px
import plotly.graph_objects as go
from plotly.subplots import make_subplots
from pathlib import Path
import warnings
warnings.filterwarnings('ignore')

# Page configuration
st.set_page_config(
    page_title="Ethiopia Financial Inclusion Forecast",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Paths
DATA_DIR = Path('data/raw')
PROCESSED_DIR = Path('data/processed')
REPORTS_DIR = Path('reports/figures')

# Custom CSS
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .metric-card {
        background-color: #f0f2f6;
        padding: 1rem;
        border-radius: 0.5rem;
        border-left: 4px solid #1f77b4;
    }
    </style>
""", unsafe_allow_html=True)

# Load data
@st.cache_data
def load_data():
    """Load the financial inclusion dataset"""
    try:
        if (PROCESSED_DIR / 'ethiopia_fi_unified_data_enriched.csv').exists():
            df = pd.read_csv(PROCESSED_DIR / 'ethiopia_fi_unified_data_enriched.csv')
        else:
            df = pd.read_csv(DATA_DIR / 'ethiopia_fi_unified_data.csv')
        return df
    except FileNotFoundError:
        st.error("Data file not found. Please ensure data files are in the correct directory.")
        return None

@st.cache_data
def load_forecasts():
    """Load forecast data"""
    try:
        if (PROCESSED_DIR / 'forecasts_2025_2027.csv').exists():
            return pd.read_csv(PROCESSED_DIR / 'forecasts_2025_2027.csv')
        return None
    except:
        return None

# Load data
df = load_data()
forecast_df = load_forecasts()

if df is None:
    st.stop()

# Extract data subsets
observations = df[df['record_type'] == 'observation'].copy()
events = df[df['record_type'] == 'event'].copy()
impact_links = df[df['record_type'] == 'impact_link'].copy()

# Convert dates
date_cols = [col for col in observations.columns if 'date' in col.lower()]
for col in date_cols:
    if col in observations.columns:
        observations[col] = pd.to_datetime(observations[col], errors='coerce')

# Sidebar navigation
st.sidebar.title("📊 Navigation")
page = st.sidebar.radio(
    "Select Page",
    ["Overview", "Trends", "Forecasts", "Inclusion Projections"]
)

# ============================================================================
# OVERVIEW PAGE
# ============================================================================
if page == "Overview":
    st.markdown('<div class="main-header">Ethiopia Financial Inclusion Dashboard</div>', unsafe_allow_html=True)
    st.markdown("### Key Metrics Summary")
    
    # Get latest account ownership
    acc_obs = observations[
        (observations['indicator_code'].str.contains('ACC_OWNERSHIP', case=False, na=False)) |
        (observations['indicator'] == 'Account Ownership Rate')
    ].copy()
    
    if len(acc_obs) > 0 and 'observation_date' in acc_obs.columns:
        acc_obs = acc_obs.sort_values('observation_date')
        latest_acc = acc_obs.iloc[-1]
        latest_year = latest_acc['observation_date'].year if hasattr(latest_acc['observation_date'], 'year') else pd.to_datetime(latest_acc['observation_date']).year
        latest_value = latest_acc['value_numeric']
        
        # Calculate growth rate
        if len(acc_obs) > 1:
            prev_value = acc_obs.iloc[-2]['value_numeric']
            growth_rate = ((latest_value - prev_value) / prev_value) * 100
        else:
            growth_rate = 0
    else:
        latest_value = 49.0  # Default from project description
        latest_year = 2024
        growth_rate = 0
    
    # Get mobile money data
    mm_obs = observations[
        (observations['indicator_code'].str.contains('MM_ACCOUNT', case=False, na=False)) |
        (observations['indicator'].str.contains('mobile money', case=False, na=False))
    ].copy()
    
    if len(mm_obs) > 0 and 'observation_date' in mm_obs.columns:
        mm_obs = mm_obs.sort_values('observation_date')
        latest_mm = mm_obs.iloc[-1]['value_numeric']
    else:
        latest_mm = 9.45  # Default from project description
    
    # Create metric cards
    col1, col2, col3, col4 = st.columns(4)
    
    with col1:
        st.metric(
            label="Account Ownership (2024)",
            value=f"{latest_value:.1f}%",
            delta=f"{growth_rate:+.1f}%"
        )
    
    with col2:
        st.metric(
            label="Mobile Money Accounts",
            value=f"{latest_mm:.1f}%",
        )
    
    with col3:
        st.metric(
            label="Total Events Cataloged",
            value=len(events)
        )
    
    with col4:
        st.metric(
            label="Impact Links",
            value=len(impact_links)
        )
    
    # P2P/ATM Crossover Ratio (if data available)
    st.markdown("---")
    st.markdown("### P2P/ATM Crossover Indicator")
    st.info("""
    **Key Milestone:** For the first time, interoperable P2P digital transfers have 
    surpassed ATM cash withdrawals in Ethiopia. This indicates a shift toward digital 
    payment adoption.
    """)
    
    # Growth rate highlights
    st.markdown("---")
    st.markdown("### Growth Rate Highlights")
    
    if len(acc_obs) > 1:
        acc_obs_sorted = acc_obs.sort_values('observation_date')
        growth_data = []
        
        for i in range(1, len(acc_obs_sorted)):
            prev_year = acc_obs_sorted.iloc[i-1]['observation_date'].year if hasattr(acc_obs_sorted.iloc[i-1]['observation_date'], 'year') else pd.to_datetime(acc_obs_sorted.iloc[i-1]['observation_date']).year
            curr_year = acc_obs_sorted.iloc[i]['observation_date'].year if hasattr(acc_obs_sorted.iloc[i]['observation_date'], 'year') else pd.to_datetime(acc_obs_sorted.iloc[i]['observation_date']).year
            prev_val = acc_obs_sorted.iloc[i-1]['value_numeric']
            curr_val = acc_obs_sorted.iloc[i]['value_numeric']
            change_pp = curr_val - prev_val
            
            growth_data.append({
                'Period': f"{prev_year}-{curr_year}",
                'Change (pp)': change_pp,
                'Previous': prev_val,
                'Current': curr_val
            })
        
        growth_df = pd.DataFrame(growth_data)
        st.dataframe(growth_df, use_container_width=True)

# ============================================================================
# TRENDS PAGE
# ============================================================================
elif page == "Trends":
    st.markdown('<div class="main-header">Financial Inclusion Trends</div>', unsafe_allow_html=True)
    
    # Date range selector
    st.sidebar.markdown("### Filters")
    
    if len(observations) > 0 and 'observation_date' in observations.columns:
        min_date = observations['observation_date'].min()
        max_date = observations['observation_date'].max()
        
        date_range = st.sidebar.date_input(
            "Date Range",
            value=(min_date, max_date),
            min_value=min_date,
            max_value=max_date
        )
    
    # Indicator selector
    indicators = observations['indicator_code'].dropna().unique() if 'indicator_code' in observations.columns else []
    selected_indicators = st.sidebar.multiselect(
        "Select Indicators",
        options=sorted(indicators),
        default=sorted(indicators)[:3] if len(indicators) >= 3 else sorted(indicators)
    )
    
    # Account Ownership Trend
    st.markdown("### Account Ownership Trend")
    acc_obs = observations[
        (observations['indicator_code'].str.contains('ACC_OWNERSHIP', case=False, na=False)) |
        (observations['indicator'] == 'Account Ownership Rate')
    ].copy()
    
    if len(acc_obs) > 0 and 'observation_date' in acc_obs.columns:
        acc_obs = acc_obs.sort_values('observation_date')
        
        fig = go.Figure()
        fig.add_trace(go.Scatter(
            x=acc_obs['observation_date'],
            y=acc_obs['value_numeric'],
            mode='lines+markers',
            name='Account Ownership',
            line=dict(color='steelblue', width=3),
            marker=dict(size=10)
        ))
        
        # Add events as vertical lines
        if len(events) > 0:
            for _, event in events.iterrows():
                event_date = pd.to_datetime(event.get('event_date', event.get('observation_date', '2000-01-01')))
                event_name = event.get('event_name', 'Event')
                fig.add_vline(
                    x=event_date,
                    line_dash="dash",
                    line_color="gray",
                    annotation_text=event_name[:20] if len(event_name) > 20 else event_name
                )
        
        fig.update_layout(
            title="Account Ownership Trajectory (2011-2024)",
            xaxis_title="Year",
            yaxis_title="Account Ownership Rate (%)",
            height=500,
            hovermode='x unified'
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Channel Comparison
    st.markdown("### Channel Comparison")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Account Ownership vs Mobile Money
        if len(acc_obs) > 0:
            mm_obs = observations[
                (observations['indicator_code'].str.contains('MM_ACCOUNT', case=False, na=False)) |
                (observations['indicator'].str.contains('mobile money', case=False, na=False))
            ].copy()
            
            if len(mm_obs) > 0 and 'observation_date' in mm_obs.columns:
                mm_obs = mm_obs.sort_values('observation_date')
                
                fig = make_subplots(specs=[[{"secondary_y": True}]])
                
                fig.add_trace(
                    go.Scatter(x=acc_obs['observation_date'], y=acc_obs['value_numeric'],
                             name='Account Ownership', line=dict(color='steelblue')),
                    secondary_y=False
                )
                
                fig.add_trace(
                    go.Scatter(x=mm_obs['observation_date'], y=mm_obs['value_numeric'],
                             name='Mobile Money Accounts', line=dict(color='coral')),
                    secondary_y=True
                )
                
                fig.update_xaxes(title_text="Year")
                fig.update_yaxes(title_text="Account Ownership (%)", secondary_y=False)
                fig.update_yaxes(title_text="Mobile Money Accounts (%)", secondary_y=True)
                fig.update_layout(title="Account Ownership vs Mobile Money Accounts", height=400)
                st.plotly_chart(fig, use_container_width=True)
    
    with col2:
        # Digital Payment Usage
        usage_obs = observations[
            (observations['indicator_code'].str.contains('USG_DIGITAL', case=False, na=False)) |
            (observations['pillar'] == 'usage')
        ].copy()
        
        if len(usage_obs) > 0 and 'observation_date' in usage_obs.columns:
            usage_obs = usage_obs.sort_values('observation_date')
            
            fig = go.Figure()
            fig.add_trace(go.Scatter(
                x=usage_obs['observation_date'],
                y=usage_obs['value_numeric'],
                mode='lines+markers',
                name='Digital Payment Usage',
                line=dict(color='mediumseagreen', width=3),
                marker=dict(size=10)
            ))
            fig.update_layout(
                title="Digital Payment Usage Trend",
                xaxis_title="Year",
                yaxis_title="Usage Rate (%)",
                height=400
            )
            st.plotly_chart(fig, use_container_width=True)

# ============================================================================
# FORECASTS PAGE
# ============================================================================
elif page == "Forecasts":
    st.markdown('<div class="main-header">Financial Inclusion Forecasts (2025-2027)</div>', unsafe_allow_html=True)
    
    # Model selection
    model_type = st.sidebar.selectbox(
        "Select Model",
        ["Baseline Trend", "Event-Augmented", "Scenario Analysis"]
    )
    
    # Account Ownership Forecast
    st.markdown("### Account Ownership Forecast")
    
    acc_obs = observations[
        (observations['indicator_code'].str.contains('ACC_OWNERSHIP', case=False, na=False)) |
        (observations['indicator'] == 'Account Ownership Rate')
    ].copy()
    
    if len(acc_obs) >= 2 and 'observation_date' in acc_obs.columns:
        acc_obs = acc_obs.sort_values('observation_date')
        acc_obs['year'] = pd.to_datetime(acc_obs['observation_date']).dt.year
        
        # Simple linear forecast
        from sklearn.linear_model import LinearRegression
        X = acc_obs[['year']].values
        y = acc_obs['value_numeric'].values
        model = LinearRegression()
        model.fit(X, y)
        
        # Historical + forecast years
        historical_years = acc_obs['year'].values
        forecast_years = np.array([2025, 2026, 2027])
        all_years = np.concatenate([historical_years, forecast_years])
        
        predictions = model.predict(all_years.reshape(-1, 1))
        
        # Create visualization
        fig = go.Figure()
        
        # Historical data
        fig.add_trace(go.Scatter(
            x=acc_obs['year'],
            y=acc_obs['value_numeric'],
            mode='lines+markers',
            name='Historical',
            line=dict(color='steelblue', width=3),
            marker=dict(size=10)
        ))
        
        # Forecast
        forecast_mask = all_years >= 2025
        fig.add_trace(go.Scatter(
            x=all_years[forecast_mask],
            y=predictions[forecast_mask],
            mode='lines+markers',
            name='Forecast',
            line=dict(color='coral', width=3, dash='dash'),
            marker=dict(size=10)
        ))
        
        fig.update_layout(
            title="Account Ownership Forecast (2025-2027)",
            xaxis_title="Year",
            yaxis_title="Account Ownership Rate (%)",
            height=500,
            hovermode='x unified'
        )
        st.plotly_chart(fig, use_container_width=True)
        
        # Forecast table
        st.markdown("#### Forecast Values")
        forecast_data = {
            'Year': forecast_years,
            'Forecast (%)': predictions[forecast_mask]
        }
        forecast_table = pd.DataFrame(forecast_data)
        st.dataframe(forecast_table, use_container_width=True)
    
    # Key Projected Milestones
    st.markdown("---")
    st.markdown("### Key Projected Milestones")
    
    milestones = [
        "**2025:** Account ownership expected to reach 50-52%",
        "**2026:** Potential crossing of 55% threshold",
        "**2027:** Progress toward 60% target (NFIS-II goal)"
    ]
    
    for milestone in milestones:
        st.markdown(f"- {milestone}")

# ============================================================================
# INCLUSION PROJECTIONS PAGE
# ============================================================================
elif page == "Inclusion Projections":
    st.markdown('<div class="main-header">Financial Inclusion Projections</div>', unsafe_allow_html=True)
    
    # Scenario selector
    scenario = st.sidebar.selectbox(
        "Select Scenario",
        ["Optimistic", "Base", "Pessimistic"]
    )
    
    st.markdown(f"### {scenario} Scenario Projections")
    
    # Financial inclusion rate projections
    acc_obs = observations[
        (observations['indicator_code'].str.contains('ACC_OWNERSHIP', case=False, na=False)) |
        (observations['indicator'] == 'Account Ownership Rate')
    ].copy()
    
    if len(acc_obs) >= 2 and 'observation_date' in acc_obs.columns:
        acc_obs = acc_obs.sort_values('observation_date')
        acc_obs['year'] = pd.to_datetime(acc_obs['observation_date']).dt.year
        
        # Simple projections with scenarios
        from sklearn.linear_model import LinearRegression
        X = acc_obs[['year']].values
        y = acc_obs['value_numeric'].values
        model = LinearRegression()
        model.fit(X, y)
        
        forecast_years = np.array([2025, 2026, 2027])
        base_forecast = model.predict(forecast_years.reshape(-1, 1))
        
        # Apply scenario multipliers
        multipliers = {
            'Optimistic': 1.15,
            'Base': 1.0,
            'Pessimistic': 0.85
        }
        
        scenario_forecast = base_forecast * multipliers[scenario]
        
        # Progress toward 60% target
        target = 60.0
        current = acc_obs['value_numeric'].iloc[-1]
        
        col1, col2 = st.columns(2)
        
        with col1:
            st.metric(
                "Current Rate (2024)",
                f"{current:.1f}%"
            )
        
        with col2:
            progress_2027 = scenario_forecast[-1]
            st.metric(
                f"Projected Rate (2027 - {scenario})",
                f"{progress_2027:.1f}%",
                delta=f"{progress_2027 - target:.1f}% to target"
            )
        
        # Progress visualization
        st.markdown("### Progress Toward 60% Target")
        
        years = np.concatenate([acc_obs['year'].values, forecast_years])
        values = np.concatenate([acc_obs['value_numeric'].values, scenario_forecast])
        
        fig = go.Figure()
        
        # Historical
        hist_mask = years < 2025
        fig.add_trace(go.Scatter(
            x=years[hist_mask],
            y=values[hist_mask],
            mode='lines+markers',
            name='Historical',
            line=dict(color='steelblue', width=3)
        ))
        
        # Forecast
        forecast_mask = years >= 2025
        fig.add_trace(go.Scatter(
            x=years[forecast_mask],
            y=values[forecast_mask],
            mode='lines+markers',
            name=f'Forecast ({scenario})',
            line=dict(color='coral', width=3, dash='dash')
        ))
        
        # Target line
        fig.add_hline(
            y=target,
            line_dash="dot",
            line_color="red",
            annotation_text="60% Target",
            annotation_position="right"
        )
        
        fig.update_layout(
            title="Financial Inclusion Progress Toward 60% Target",
            xaxis_title="Year",
            yaxis_title="Account Ownership Rate (%)",
            height=500
        )
        st.plotly_chart(fig, use_container_width=True)
    
    # Answers to consortium questions
    st.markdown("---")
    st.markdown("### Answers to Consortium's Key Questions")
    
    st.markdown("""
    **1. What drives financial inclusion in Ethiopia?**
    - Mobile money adoption (Telebirr, M-Pesa) is the primary driver
    - Infrastructure investments (4G coverage, agent networks)
    - Market competition between providers
    - Policy frameworks (NFIS-II)
    
    **2. How do events affect inclusion outcomes?**
    - Product launches (Telebirr, M-Pesa) have immediate and sustained impacts
    - Competition increases adoption and usage
    - Infrastructure investments have longer-term effects
    - Policy changes create enabling environments
    
    **3. How did financial inclusion change in 2025 and how will it look in 2026-2027?**
    - 2025: Expected to reach 50-52% (baseline scenario)
    - 2026: Projected 52-55% range
    - 2027: Potential to reach 55-58%, progressing toward 60% target
    """)
    
    # Data download
    st.markdown("---")
    st.markdown("### Download Data")
    
    if forecast_df is not None:
        csv = forecast_df.to_csv(index=False)
        st.download_button(
            label="Download Forecast Data (CSV)",
            data=csv,
            file_name="ethiopia_fi_forecasts_2025_2027.csv",
            mime="text/csv"
        )

# Footer
st.sidebar.markdown("---")
st.sidebar.markdown("**Ethiopia Financial Inclusion Forecast**")
st.sidebar.markdown("Selam Analytics Project")
