
#!/bin/bash

# Functions to perform the API call 
perform_api_add_call() {
    local url="$1"
    local num1="$2"
    local num2="$3"
    local expected_value="$4"

    # Make the API call
    local output=$(curl -s -k1 -X GET "$url/add?num1=$num1&num2=$num2")

    # Parse output using sed
    local actual_value=`echo $output | sed -e 's/{"result":\(.*\)}/\1/'`

    # Check whether they are equal
    if [[ $actual_value == $add_expected_value ]]; then
        echo "Add Test passed: $actual_value = $add_expected_value"
    else
        echo "Add Test failed: $actual_value is not equal to $add_expected_value"
    fi

    # Error handling for the curl command
    if [ $? -ne 0 ]; then
        echo "Error: Failed to execute the API call"
        exit 1
    fi
}

perform_api_sub_call() {
    local url="$1"
    local num1="$2"
    local num2="$3"
    local expected_value="$4"

    # Make the API call
    local output=$(curl -s -k1 -X GET "$url/subtract?num1=$num1&num2=$num2")

    # Parse output using sed
    local actual_value=`echo $output | sed -e 's/{"result":\(.*\)}/\1/'`

    # Check whether they are equal
    if [[ $actual_value == $sub_expected_value ]]; then
        echo "Subtract Test passed: $actual_value = $sub_expected_value"
    else
        echo "Subtract Test failed: $actual_value is not equal to $sub_expected_value"
    fi

    # Error handling for the curl command
    if [ $? -ne 0 ]; then
        echo "Error: Failed to execute the API call"
        exit 1
    fi
}

perform_api_mul_call() {
    local url="$1"
    local num1="$2"
    local num2="$3"
    local expected_value="$4"

    # Make the API call
    local output=$(curl -s -k1 -X GET "$url/multiply?num1=$num1&num2=$num2")

    # Parse output using sed
    local actual_value=`echo $output | sed -e 's/{"result":\(.*\)}/\1/'`

    # Check whether they are equal
    if [[ $actual_value == $mul_expected_value ]]; then
        echo "Multipication Test passed: $actual_value = $mul_expected_value"
    else
        echo "Multipication Test failed: $actual_value is not equal to $mul_expected_value"
    fi

    # Error handling for the curl command
    if [ $? -ne 0 ]; then
        echo "Error: Failed to execute the API call"
        exit 1
    fi
}

perform_api_div_call() {
    local url="$1"
    local num1="$2"
    local num2="$3"
    local expected_value="$4"

    # Make the API call
    local output=$(curl -s -k1 -X GET "$url/divide?num1=$num1&num2=$num2")

    # Parse output using sed
    local actual_value=`echo $output | sed -e 's/{"result":\(.*\)}/\1/'`

    # Check whether they are equal
    if [[ $actual_value == $div_expected_value ]]; then
        echo "Division Test passed: $actual_value = $div_expected_value"
    else
        echo "Division Test failed: $actual_value is not equal to $div_expected_value"
    fi

    # Error handling for the curl command
    if [ $? -ne 0 ]; then
        echo "Error: Failed to execute the API call"
        exit 1
    fi
}


### Main Block 
# Define variables
url='http://localhost:9000'
num1=35
num2=5
add_expected_value=40.0
sub_expected_value=30.0
mul_expected_value=175.0
div_expected_value=7.0

# Call the function
perform_api_add_call "$url" "$num1" "$num2" "$add_expected_value"
perform_api_sub_call "$url" "$num1" "$num2" "$sub_expected_value"
perform_api_mul_call "$url" "$num1" "$num2" "$mul_expected_value"
perform_api_div_call "$url" "$num1" "$num2" "$div_expected_value"