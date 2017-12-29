#!/usr/bin/python


def outlierCleaner(predictions, ages, net_worths):
    """
        Clean away the 10% of points that have the largest
        residual errors (difference between the prediction
        and the actual net worth).

        Return a list of tuples named cleaned_data where 
        each tuple is of the form (age, net_worth, error).
    """
    
    cleaned_data = []

    ### your code goes here
    num_data = len(predictions)
    for x in range(0, num_data):
        age = ages[x][0]
        net_worth = net_worths[x][0]
        prediction = predictions[x][0]
        cleaned_data.append((age, net_worth, prediction - net_worth))
    
    cleaned_data = sorted(cleaned_data, key=lambda tdata: tdata[2])
    return cleaned_data[:-9]

