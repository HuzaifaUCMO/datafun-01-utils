''' Module: Quantum Insights - Reusable Module for My Data Analytics Projects

This module provides a simple, reusable foundation for my analytics projects.
When we work hard to write useful code, we want it to be reusable.
A good byline could be used in every Python analytics project we do.
'''

is_remote_friendly: bool = True
number_of_clients: int = 50
services_offered: list = ["Data Visualization", "Machine Learning", "Statistical Analysis"]

byline: str = f'''Quantum Insights: Delivering Actionable Intelligence
- Remote Friendly: {is_remote_friendly}
- Clients Served: {number_of_clients}
- Services: {', '.join(services_offered)}'''

def get_byline() -> str:
    '''Returns the byline string.'''
    return byline

def main() -> None:
    '''Print the byline returned by get_byline() to the console.'''
    print(get_byline())

if __name__ == '__main__':
    main()
