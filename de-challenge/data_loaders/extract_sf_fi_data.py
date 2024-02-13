import io
import pandas as pd
import requests
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    url = 'https://data.sfgov.org/api/views/wr8u-xric/rows.csv?fourfour=wr8u-xric'
    # url = 'https://data.sfgov.org/resource/wr8u-xric.csv'
    response = requests.get(url)
    column_types = {
        "Incident Number": str,
        "Exposure Number": str,
        "ID": str,
        "Address": str,
        "Incident Date": str,
        "Call Number": str,
        "Alarm DtTm": str,
        "Arrival DtTm": str,
        "Close DtTm": str,
        "City": str,
        "zipcode": str,
        "Battalion": str,
        "Station Area": str,
        "Box": str,
        "Suppression Units": str,
        "Suppression Personnel": str,
        "EMS Units": str,
        "EMS Personnel": str,
        "Other Units": str,
        "Other Personnel": str,
        "First Unit On Scene": str,
        "Estimated Property Loss": str,
        "Estimated Contents Loss": str,
        "Fire Fatalities": str,
        "Fire Injuries": str,
        "Civilian Fatalities": str,
        "Civilian Injuries": str,
        "Number of Alarms": str,
        "Primary Situation": str,
        "Mutual Aid": str,
        "Action Taken Primary": str,
        "Action Taken Secondary": str,
        "Action Taken Other": str,
        "Detector Alerted Occupants": str,
        "Property Use": str,
        "Area of Fire Origin": str,
        "Ignition Cause": str,
        "Ignition Factor Primary": str,
        "Ignition Factor Secondary": str,
        "Heat Source": str,
        "Item First Ignited": str,
        "Human Factors Associated with Ignition": str,
        "Structure Type": str,
        "Structure Status": str,
        "Floor of Fire Origin": str,
        "Fire Spread": str,
        "No Flame Spead": str,
        "Number of floors with minimum damage": str,
        "Number of floors with significant damage": str,
        "Number of floors with heavy damage": str,
        "Number of floors with extreme damage": str,
        "Detectors Present": str,
        "Detector Type": str,
        "Detector Operation": str,
        "Detector Effectiveness": str,
        "Detector Failure Reason": str,
        "Automatic Extinguishing System Present": str,
        "Automatic Extinguishing Sytem Type": str,
        "Automatic Extinguishing Sytem Perfomance": str,
        "Automatic Extinguishing Sytem Failure Reason": str,
        "Number of Sprinkler Heads Operating": str,
        "Supervisor District": str,
        "neighborhood_district": str,
        "point": str
    }

    return pd.read_csv(io.StringIO(response.text), dtype=column_types)


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
