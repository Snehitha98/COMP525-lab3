### months_and_days()

```
def months_and_days(self, month_names, month_days):
    """
    Create a string with info from the month_names and month_days lists
    month_names: list of words naming the 12 months of the year,
        in lower case. Example: ['january', 'february', ...]
    month_days: list of numbers corresponding to the number of days in
        each month, from January to December, and February having 28 days
        Example: [31, 28, 31, 30, 31, ...]
    Returns: list of of words, where each word has the following:
        First three letters of a month name, with first letter capitalized
        Followed by '-' and then the number of days in that month

    Example: Calling the function will produce the following list
        ['Jan-31', 'Feb-28', 'Mar-31', ... ]
    """
```

* initialize **three_letters_of_month_name** with null list
* use a for loop with loop variable called **month** to iterate over **month_names**
    * using string slicing first three letters of month name is added to a list **three_letters_of_month_name** and stores in a list **three_letters_of_month_name**
* initialize **first_letter_capital** with null list
* use a for loop with loop variable called **month_name** to iterate over **three_letters_of_month_name**
    * making first letter of month_name capital and adding it to first_letter_capital and storing it in a list **first_letter_capital**
* initialize **x** with null list
* use a for loop with loop variable called **month_name** to iterate over **first_letter_capital**
    * adding month_name followed by "-" and storing it in a list **x**
* initialize **expected_result** with null list
* Define and initialize an accumulator called **k**, of type integer that returns range of number of words in a list named **month_days**
* use a for loop with loop variable called **i** to iterate over **k**
    * concatenation of x and month_days of index i is assigned to variable called result
    * result is stored in a list of **expected_result**
* Returns **expected_result**
