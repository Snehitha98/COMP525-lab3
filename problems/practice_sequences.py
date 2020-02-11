"""
practice_sequences.py
Get more practice with sequences
Mihaela Sabin
Created February 10, 2020
"""


class Practice(object):
    """
    Illustrate methods that transform input sequences
        into something else
    """

    def months_and_days(self, month_names, month_days):
        """
        Create a string with info from the month_names and month_days lists
        month_names: list of words naming the 12 months of the year,
            in lower case. Example: ['january', 'february', ...]
        month_days: list of numbers corresponding to the number of days in
            each month, from January to December, and February having 28 days
            Example: [31, 28, 31, 30, 31, ...]
        Returns: list of of words, where each word has the following:
            First three letters of a month hame, with first letter capitalized
            Followed by '-' and then the number of days in that month

        Example: Calling the function will produce the following list
            ['Jan-31', 'Feb-28', 'Mar-31', ... ]
        """
        pass


if __name__ == '__main__':
    p = Practice()
    input1 = ['january', 'february']
    input2 = [31, 28]
    result = p.months_and_days(input1, input2)
    print(f'months_and_days({input1}, {input2}) returns {result}')
