def get_file_length(input_data):
    import os
    len_val = None
    print(input_data)

    # Check if it is a file
    try:
        if os.path.isfile(str(input_data)):
            len_val = os.path.getsize(str(input_data))
    except:
        pass

    # Otherwise, get the length of it
    if not len_val:
        len_val = len(input_data)

    return len_val
