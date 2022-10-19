from dataclasses import dataclass
import re
import typer
import json
import os

app = typer.Typer()

# Data structure to represent data point in the batch
# The color method identifies the color of the data point
# The distance method calculates the distance between 2 data points
@dataclass
class DataPoint:
    rank: str
    suit: str

    def color(self):
        red = ('C', 'S')
        black = ('H', 'D')
        R = "red"
        B = "black"
        if self.suit in red:
            return R
        else:
            return B

    def get_rank_value(self):
        if self.rank == 'A':
            rank_value = 1
        elif self.rank in ('J', "Q", "K"):
            rank_value = 10
        else:
            rank_value = int(self.rank)
        return rank_value

    def distance(self, other):
        if self.suit == other.suit:
            factor = 1
        elif self.color() == other.color():
            factor = 2
        else:
            factor = 3
        return factor * abs(self.get_rank_value() - other.get_rank_value())

# Extract data from JSON file (raw batch)
def open_raw_batch(full_path_raw_batch_name: str):
    '''
    It reads the input batch file (json)
    and returns a list of strings containing the data points
    in raw format
    If takes as input the name of the batch file (including the full path
    if the batch is in a different directory)
    '''
    try:
        with open(full_path_raw_batch_name, 'r') as raw_json:
            raw_batch = json.load(raw_json)
        return raw_batch
    except FileNotFoundError as e:
        print(f'{full_path_raw_batch_name} not found')
        return None
    except ValueError as e:
        print(f'{full_path_raw_batch_name} is malformed')
        return None

# Validate dapa points in input JSON file (raw batch)
def validate_data_point(data_point: str) -> tuple:
    """
    Validates data point and returns tuple (rank, suit)
    """
    # Regex expression used to validate data point
    # It is also used to extract rank and suit
    INPUT_SYNTAX = '^([2-9AJQK]|10)([CHSD])$'
    try:
        return re.search(INPUT_SYNTAX, data_point).groups()
    except:
        return data_point, -1


# Formatting raw batch to internal data model
def format_batch(raw_batch):
    '''
    This function takes the raw batch (as read from the input json file
    and returns a formatted batch
    Each element of the batch has type = DataPoint
    '''
    rank = lambda t: t[0]
    suit = lambda t: t[1]
    formatted_input = [validate_data_point(input_point) for input_point in raw_batch]
    return [DataPoint(rank(data_point), suit(data_point)) for data_point in formatted_input]

# Calculation of waste metric (batch)
def waste_metric_int(batch: list) -> int:
    '''
    Calculates the waste-metric of a formatted batch
    It takes as input a formatted batch
    It returns the waste-metric
    '''
    return sum([e1.distance(e2) for e1, e2 in zip(batch[1:], batch[:-1])])

# Contribution to waste of each data point in batch
def waste_contribution(batch, pos):
    """
    Waste contribution by data point
    It calculates the distance with its sucessor and its predecessor
    """
    successor = 0 if pos >= len(batch) - 1 else batch[pos].distance(batch[pos+1])
    predecessor = 0 if pos-1 < 0 else batch[pos].distance(batch[pos-1])
    return successor + predecessor


# Finds the optimal swap to minimize waste metric 
def optimal_swap(batch: list) -> tuple:
    '''
    This function finds the swap that minimizes the waste metric of the batch
    It iterates over all the possible swaps of 2 elements in the batch
    Possible waps = number of 2-combinations of a set of 52 elements: 2,652 combinations
    [naive implementation]
    It calculates the delta waste before and after the swap
    Receives a formatted batch and returns a tuple of 5 elements:
    1. Data point 1 involved in the optimal swap (in raw format)
    2. Data point 2 involved in the optimal swap (in raw format)
    3. Waste metric before the swap
    4. Waste metric after the swap
    5. New batch after the swap
    '''
    opt_change = 0
    final_swap = (0, 0)
    for i in range(len(batch)):
        for j in range(i+1, len(batch)):
            # Calculation of waste before changing i and j data points
            bc_waste = waste_contribution(batch, i) + waste_contribution(batch, j)
            # Makes a copy of the batch and swaps 2 data points
            swapped_batch = batch.copy()
            swapped_batch[i], swapped_batch[j] = swapped_batch[j], swapped_batch[i]
            # Calculates the waste after the swap
            ac_waste = waste_contribution(swapped_batch, i) + waste_contribution(swapped_batch, j) 
            # Calculates the difference of the swap metric before and after the swap
            waste_change = ac_waste - bc_waste
            if waste_change < opt_change:
                opt_change = waste_change
                final_swap = (i, j)
                new_batch = swapped_batch
        # Produces the output with the recommendation that
        # minimizes the waste metric in the batch
        i, j = final_swap
        i_data_point = batch[i].rank + batch[i].suit
        j_data_point = batch[j].rank + batch[j].suit
        initial_waste = waste_metric_int(batch)
        final_waste = waste_metric_int(new_batch)
    return i_data_point, j_data_point, initial_waste, final_waste, new_batch


def is_invalid_batch_int(raw_batch: list) -> bool:
    """
    Returns a tuple indicating the result of the validation
    In case of 'not valid' it also returns a problematic data point
    (the first one found)
    """
    is_valid = False
    batch_size = 52

    # Check no duplicates
    if len(raw_batch) != batch_size:
        return is_valid, 'Batch file malformed: incorrect size'

    # Check no duplicates
    if len(set(raw_batch)) != len(raw_batch):
        return is_valid, 'Batch file malformed: duplicate records'

    # Check validity of all the data points
    for data_point in raw_batch:
        if validate_data_point(data_point)[1] == -1:
            return is_valid, f'Batch file malformed: found not valid data point: {data_point}'
    
    # Batch is valid
    is_valid = True
    return is_valid, None


@app.command()
def is_invalid_batch(full_path_raw_batch_name: str):
    '''
    Implements the is-invalid-batch CLI command
    '''    
    raw_batch = open_raw_batch(full_path_raw_batch_name)
    if raw_batch != None:
        is_valid, error_message = is_invalid_batch_int(raw_batch)
        if is_valid == False:
            print(error_message)
        elif is_valid == True:
            print("The batch is syntactically valid")


@app.command()
def waste_metric(full_path_raw_batch_name: str):
    '''
    Implements the waste-metric CLI command
    '''
    raw_batch = open_raw_batch(full_path_raw_batch_name)
    if raw_batch != None:
        batch = format_batch(raw_batch)
        batch_waste = waste_metric_int(batch)
        print(f'batch file: {full_path_raw_batch_name}')
        print(f'Waste metric: {batch_waste}')


@app.command()
def one_swap_recommendation(full_path_raw_batch_name: str):
    '''
    Implements the one-swap-recommendation CLI command
    '''    
    raw_batch = open_raw_batch(full_path_raw_batch_name)
    if raw_batch != None:
        batch = format_batch(raw_batch)
        i_data_point, j_data_point, initial_waste, final_waste, _ = optimal_swap(batch)

        message = f'By swapping {i_data_point} and {j_data_point}, '\
                  f'you could reduce waste metric from ' \
                  f'{initial_waste} to {final_waste}'
        print(message)


@app.command()
def two_swap_recommendation(full_path_raw_batch_name: str):
    '''
    Implements the two-swap-recommendation CLI command
    '''
    raw_batch = open_raw_batch(full_path_raw_batch_name)
    if raw_batch != None:
        batch = format_batch(raw_batch)
        
        ## First swap
        i_data_point_1, j_data_point_1, initial_waste, _, new_batch = optimal_swap(batch)

        ## Second swap
        i_data_point_2, j_data_point_2, _, final_waste, _ = optimal_swap(new_batch)

        message = f'By swapping {i_data_point_1} and {j_data_point_1}, then ' \
                f'swapping {i_data_point_2} and {j_data_point_2}, you ' \
                f'could reduce waste metric ' \
                f'from {initial_waste} to {final_waste}'
        print(message)


@app.command()
def process_batch(full_path_raw_batch_name: str):
    '''
    Implements end-user functionality
    '''
    raw_batch = open_raw_batch(full_path_raw_batch_name)
    if raw_batch != None:
    
        # Step 1: receive an alarm if the batch is invalid

        is_valid, error_message = is_invalid_batch_int(raw_batch)
        if is_valid == False:
            print(error_message)

        elif is_valid == True:
            # Step 2: understand the waste metric for the batch
            batch = format_batch(raw_batch)
            print(f'Waste metric: {waste_metric_int(batch)}')

            # Step 3: receive a proactive recommendation that maximizes reduction
            #         in the waste metric if one swap of any two entries anywhere
            #         in the batch could occur
            i_data_point_1, j_data_point_1, initial_waste, int_waste, new_batch = optimal_swap(batch)
            message = f'By swapping {i_data_point_1} and {j_data_point_1}, '\
                    f'you could reduce waste metric from ' \
                    f'{initial_waste} to {int_waste}'
            print(message)

            # Step 4: receive a proactive recommendation that maximizes reduction
            #         in the waste metric if two swaps of any two entries anywhere
            #         in the batch could occur
            i_data_point_2, j_data_point_2, _, final_waste, _ = optimal_swap(new_batch)

            message = f'By swapping {i_data_point_1} and {j_data_point_1}, then ' \
                    f'swapping {i_data_point_2} and {j_data_point_2}, you ' \
                    f'could reduce waste metric ' \
                    f'from {initial_waste} to {final_waste}'
            print(message)


if __name__ == '__main__':
    app()