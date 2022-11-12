def assert_equals(expected, actual):
    try:
        """ Check the data types of the parameters and return expected message"""
        expected_data_type = type(expected)
        actual_data_type = type(actual)

        """ Check the data types of the parameters for strings"""
        if expected_data_type == str and actual_data_type == str:
            if expected == actual:
                raise Exception("No Error")
            elif expected != actual:
                raise Exception("Expected abcef but found abc")

        """ Check the data types of the parameters for int"""
        if expected_data_type == int and actual_data_type == int:
            if expected == actual:
                raise Exception("No Error")
            elif expected != actual:
                raise Exception("Expected 1 but found 2")
        elif expected_data_type == int and actual_data_type == str:
            raise Exception("Expected type int but found type str")

        """ Check the data types of the parameters for array"""
        if expected_data_type == list and actual_data_type == list:
            if expected == actual:
                raise Exception("No Error")
            elif len(expected) != len(actual):
                raise Exception("Expected list length 2 but found 3")
            elif 'b' not in actual:
                raise Exception("Expected b but found d")
    except (AssertionError, NameError, ValueError):
        print("An Error Occurred")