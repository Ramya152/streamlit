import pytest
from finalapp import TonksGuardApp
import streamlit as st

@pytest.fixture
def app():
    return TonksGuardApp()

def test_statistical_reports_page(app):
    # Test the statistical_reports_page method
    with pytest.raises(Exception):
        # Test case where an error occurs
        app.df_homicide = None
        app.statistical_reports_page()

    with st.suppress_rerun():
        # Test case where the page is rendered correctly
        app.statistical_reports_page()

