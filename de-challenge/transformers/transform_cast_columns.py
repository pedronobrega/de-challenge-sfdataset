if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):
    """
    Template code for a transformer block.

    Add more parameters to this function if this block has multiple parent blocks.
    There should be one parameter for each output variable from each parent block.

    Args:
        data: The output from the upstream parent block
        args: The output from any additional upstream blocks (if applicable)

    Returns:
        Anything (e.g. data frame, dictionary, array, int, str, etc.)
    """
    
    columns = [
        "Incident Number",
        "Exposure Number",
        "Suppression Units",
        "Suppression Personnel",
        "EMS Units",
        "EMS Personnel",
        "Other Units",
        "Other Personnel",
        "Estimated Property Loss",
        "Estimated Contents Loss",
        "Fire Fatalities",
        "Fire Injuries",
        "Civilian Fatalities",
        "Civilian Injuries",
        "Number of Alarms",
        "Floor of Fire Origin",
        "Number of floors with minimum damage",
        "Number of floors with significant damage",
        "Number of floors with heavy damage",
        "Number of floors with extreme damage",
        "Number of Sprinkler Heads Operating"
    ]

    for col in []:
        data[col] = data[col].astype('float64')

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
