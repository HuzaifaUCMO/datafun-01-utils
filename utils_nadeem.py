''' Module: Quantum Insights - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects.
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.
'''

#####################################
# Declare a global variable named byline.
#####################################

byline: str = 'Quantum Insights: Delivering Actionable Intelligence'

#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    '''Print the byline to the console when this function is called.'''
    print(byline)

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
