# @file  Valid Word Abbreviation
# @brief Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

# https://leetcode.com/problems/valid-word-abbreviation

'''
Given a non-empty string s and an abbreviation abbr, return whether the string matches with the given abbreviation.

A string such as "word" contains only the following valid abbreviations:

["word", "1ord", "w1rd", "wo1d", "wor1", "2rd", "w2d", "wo2", "1o1d", "1or1", "w1r1", "1o2", "2r1", "3d", "w3", "4"]
Notice that only the above abbreviations are valid abbreviations of the string "word". Any other string is not a valid abbreviation of "word".

Note:
Assume s contains only lowercase letters and abbr contains only lowercase letters and digits.

Example 1:
Given s = "internationalization", abbr = "i12iz4n":

Return true.

Example 2:
Given s = "apple", abbr = "a2e":

Return false.
'''

# turn each number into that many dots to get a regular expression.
# For example, when asked whether "3t2de" is a valid abbreviation for word "leetcode", I turn "3t2de" into "...t..de" and check whether that regular expression matches "leetcode", which it does. 
# rule out the number "0" and leading zeros, with another regular expression.


def validWordAbbreviation(self, word, abbr):
        """
        :type word: str
        :type abbr: str
        :rtype: bool
        """
        # Replace all number with .{number}. example "i12iz4n" to "i.{12}iz.{4}n"
        # re.sub replaces 1st regex with the 2nd regex in the given input: syntax: re.sub(regex1, regex2, inputstr)
        # re.match matches re pattern to given string: syntax - re.match(pattern, string)
        
        regex = re.sub('([1-9]\d*)', r'.{\1}', abbr)
        return bool(re.match('^' + regex + '$', word))
