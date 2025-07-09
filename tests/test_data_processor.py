import pandas as pd
import pytest

from src.data_processor import DataProcessor


@pytest.fixture
def processor():
    """Create DataProcessor instance for testing."""
    config = {"fill_value": 0}
    return DataProcessor(config)


@pytest.fixture
def sample_data():
    """Create sample DataFrame for testing."""
    return pd.DataFrame(
        {
            "id": [1, 2, 3, 2, 4],
            "name": ["Alice", "Bob", None, "Bob", "Charlie"],
            "value": [10.5, 20.0, None, 20.0, 30.5],
        }
    )


def test_clean_data_removes_duplicates(processor, sample_data):
    """Test that clean_data removes duplicate rows."""
    cleaned = processor.clean_data(sample_data)
    assert len(cleaned) == 4  # One duplicate removed


def test_clean_data_fills_missing_values(processor, sample_data):
    """Test that clean_data fills missing values."""
    cleaned = processor.clean_data(sample_data)
    assert cleaned["name"].isna().sum() == 0
    assert cleaned["value"].isna().sum() == 0


def test_validate_schema_valid_columns(processor):
    """Test schema validation with valid columns."""
    df = pd.DataFrame({"col1": [1], "col2": [2], "col3": [3]})
    assert processor.validate_schema(df, ["col1", "col2"]) is True


def test_validate_schema_missing_columns(processor):
    """Test schema validation with missing columns."""
    df = pd.DataFrame({"col1": [1], "col2": [2]})
    assert processor.validate_schema(df, ["col1", "col3"]) is False


def test_calculate_metrics_empty_dataframe(processor):
    """Test metrics calculation with empty DataFrame."""
    df = pd.DataFrame()
    metrics = processor.calculate_metrics(df)
    assert metrics["total_rows"] == 0
    assert metrics["null_percentage"] == 0


def test_calculate_metrics_with_data(processor, sample_data):
    """Test metrics calculation with actual data."""
    metrics = processor.calculate_metrics(sample_data)
    assert metrics["total_rows"] == 5
    assert metrics["duplicate_count"] == 1
    assert metrics["null_percentage"] > 0
