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
            First three letters of a month name, with first letter capitalized
            Followed by '-' and then the number of days in that month

        Example: Calling the function will produce the following list
            ['Jan-31', 'Feb-28', 'Mar-31', ... ]
        """
        three_letters_of_month_name=[]
        for month in month_names:
            three_letters_of_month_name=three_letters_of_month_name+[month[0:3]]

        first_letter_capital=[]
        for month_name in three_letters_of_month_name:
            first_letter_capital=first_letter_capital+[month_name.capitalize()]

        x=[]
        for month_name in first_letter_capital:
            x=x+[month_name+"-"]

        expected_result=[]
        k=range(len(month_days))
        for i in k:
            result=(x[i])+str(month_days[i])
            expected_result=expected_result+[result]
        return expected_result

if __name__ == '__main__':
    p = Practice()
    input1 = ['january', 'february']
    input2 = [31, 28]
    result = p.months_and_days(input1, input2)
    print(f'months_and_days({input1}, {input2}) returns {result}')
