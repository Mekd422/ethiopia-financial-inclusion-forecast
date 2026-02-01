"""
Data Enrichment Module for Ethiopia Financial Inclusion Forecast

This module provides functions to enrich the financial inclusion dataset
with additional observations, events, and impact links.
"""

import pandas as pd
from datetime import datetime
from pathlib import Path
from typing import Dict, Optional


def add_observation(
    record_type: str,
    pillar: str,
    indicator: str,
    indicator_code: str,
    value_numeric: float,
    observation_date: str,
    source_name: str,
    source_url: str,
    confidence: str = 'medium',
    original_text: str = '',
    notes: str = '',
    collected_by: str = 'Data Team',
    collection_date: Optional[str] = None
) -> Dict:
    """
    Create a new observation record following the unified schema.
    
    Parameters:
    -----------
    record_type : str
        Should be 'observation'
    pillar : str
        'access' or 'usage'
    indicator : str
        Description of the indicator
    indicator_code : str
        Code for the indicator (e.g., 'ACC_OWNERSHIP', 'USG_DIGITAL_PAYMENT')
    value_numeric : float
        Numeric value of the observation
    observation_date : str
        Date of the observation (YYYY-MM-DD)
    source_name : str
        Name of the data source
    source_url : str
        URL or reference to the source
    confidence : str
        'high', 'medium', or 'low'
    original_text : str
        Original quote or figure from source
    notes : str
        Additional notes about the observation
    collected_by : str
        Name of person/team who collected the data
    collection_date : str
        Date when data was collected (YYYY-MM-DD)
    
    Returns:
    --------
    dict : Observation record
    """
    if collection_date is None:
        collection_date = datetime.now().strftime('%Y-%m-%d')
    
    return {
        'record_type': record_type,
        'pillar': pillar,
        'indicator': indicator,
        'indicator_code': indicator_code,
        'value_numeric': value_numeric,
        'observation_date': observation_date,
        'source_name': source_name,
        'source_url': source_url,
        'confidence': confidence,
        'original_text': original_text,
        'notes': notes,
        'collected_by': collected_by,
        'collection_date': collection_date
    }


def add_event(
    record_type: str,
    category: str,
    event_date: str,
    event_name: str,
    description: str,
    source_name: str,
    source_url: str,
    confidence: str = 'medium',
    original_text: str = '',
    notes: str = '',
    collected_by: str = 'Data Team',
    collection_date: Optional[str] = None
) -> Dict:
    """
    Create a new event record following the unified schema.
    
    Parameters:
    -----------
    record_type : str
        Should be 'event'
    category : str
        Event category (e.g., 'policy', 'product_launch', 'infrastructure')
    event_date : str
        Date of the event (YYYY-MM-DD)
    event_name : str
        Name of the event
    description : str
        Description of the event
    source_name : str
        Name of the data source
    source_url : str
        URL or reference to the source
    confidence : str
        'high', 'medium', or 'low'
    original_text : str
        Original quote or figure from source
    notes : str
        Additional notes about the event
    collected_by : str
        Name of person/team who collected the data
    collection_date : str
        Date when data was collected (YYYY-MM-DD)
    
    Returns:
    --------
    dict : Event record
    """
    if collection_date is None:
        collection_date = datetime.now().strftime('%Y-%m-%d')
    
    return {
        'record_type': record_type,
        'category': category,
        'event_date': event_date,
        'event_name': event_name,
        'description': description,
        'source_name': source_name,
        'source_url': source_url,
        'confidence': confidence,
        'original_text': original_text,
        'notes': notes,
        'collected_by': collected_by,
        'collection_date': collection_date,
        'pillar': None  # Events don't have pillars
    }


def add_impact_link(
    record_type: str,
    parent_id: str,
    pillar: str,
    related_indicator: str,
    impact_direction: str,
    impact_magnitude: float,
    lag_months: int,
    evidence_basis: str,
    source_name: str,
    source_url: str,
    confidence: str = 'medium',
    original_text: str = '',
    notes: str = '',
    collected_by: str = 'Data Team',
    collection_date: Optional[str] = None
) -> Dict:
    """
    Create a new impact link record following the unified schema.
    
    Parameters:
    -----------
    record_type : str
        Should be 'impact_link'
    parent_id : str
        ID of the parent event
    pillar : str
        'access' or 'usage'
    related_indicator : str
        Indicator code that is affected
    impact_direction : str
        'positive' or 'negative'
    impact_magnitude : float
        Magnitude of the impact (percentage points or multiplier)
    lag_months : int
        Number of months before impact is felt
    evidence_basis : str
        Basis for the estimate (e.g., 'comparable_country', 'expert_estimate')
    source_name : str
        Name of the data source
    source_url : str
        URL or reference to the source
    confidence : str
        'high', 'medium', or 'low'
    original_text : str
        Original quote or figure from source
    notes : str
        Additional notes about the impact link
    collected_by : str
        Name of person/team who collected the data
    collection_date : str
        Date when data was collected (YYYY-MM-DD)
    
    Returns:
    --------
    dict : Impact link record
    """
    if collection_date is None:
        collection_date = datetime.now().strftime('%Y-%m-%d')
    
    return {
        'record_type': record_type,
        'parent_id': parent_id,
        'pillar': pillar,
        'related_indicator': related_indicator,
        'impact_direction': impact_direction,
        'impact_magnitude': impact_magnitude,
        'lag_months': lag_months,
        'evidence_basis': evidence_basis,
        'source_name': source_name,
        'source_url': source_url,
        'confidence': confidence,
        'original_text': original_text,
        'notes': notes,
        'collected_by': collected_by,
        'collection_date': collection_date
    }


def enrich_dataset(df: pd.DataFrame, new_records: list) -> pd.DataFrame:
    """
    Add new records to the dataset.
    
    Parameters:
    -----------
    df : pd.DataFrame
        Original dataset
    new_records : list
        List of new record dictionaries
    
    Returns:
    --------
    pd.DataFrame : Enriched dataset
    """
    if not new_records:
        return df
    
    new_df = pd.DataFrame(new_records)
    
    # Ensure all columns match
    for col in df.columns:
        if col not in new_df.columns:
            new_df[col] = None
    
    # Reorder columns to match original
    new_df = new_df[df.columns]
    
    # Concatenate
    df_enriched = pd.concat([df, new_df], ignore_index=True)
    
    return df_enriched
