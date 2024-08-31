''' ITERATION 5

Module: Quantum Insights - A Comprehensive Tool for Data Analytics

This module is designed to serve as a robust foundation for data analytics projects. 
It offers reusable components that help streamline the process of analyzing data and generating insightful metrics.
In this iteration, we refine our byline to include key statistical summaries, enhancing the module’s ability to convey essential information at a glance.

Features:
1. **Global Variables**: Define and initialize various metrics and settings relevant to our analytics work.
2. **Statistics Calculation**: Compute essential statistics such as minimum, maximum, mean, and standard deviation for data lists.
3. **Dynamic Byline**: Update the byline to reflect statistical insights derived from the data, offering a concise overview of key metrics.

This module is a cornerstone for any data-driven project, providing clarity and efficiency in data analysis.
'''

import statistics  # Import the statistics module for calculations

#####################################
# Declare global variables.
#####################################

company_name: str = 'Quantum Insights'
company_tagline: str = 'Empowering Data-Driven Decisions'
is_privately_held: bool = True
company_established_year: int = 2024
tools_used: list[str] = ["Git", "GitHub", "Python"]
recent_temperatures: list[float] = [72.5, 75.0, 71.0, 69.5]
client_satisfaction_scores: list[int] = [85, 90, 78, 92, 88]

# Calculate statistics for recent temperatures
min_temp: float = min(recent_temperatures)
max_temp: float = max(recent_temperatures)
mean_temp: float = statistics.mean(recent_temperatures)
stdev_temp: float = statistics.stdev(recent_temperatures)

# Calculate statistics for client satisfaction scores
min_score: int = min(client_satisfaction_scores)
max_score: int = max(client_satisfaction_scores)
mean_score: float = statistics.mean(client_satisfaction_scores)
stdev_score: float = statistics.stdev(client_satisfaction_scores)

# Define the byline using a multiline f-string to include additional information.
byline: str = f"""
{company_name}: {company_tagline}

Company Details:
- Privately Held: {is_privately_held}
- Established Year: {company_established_year}
- Tools Used: {', '.join(tools_used)}

Statistics:
- Recent Temperatures:
  - Min: {min_temp}
  - Max: {max_temp}
  - Mean: {mean_temp:.2f}
  - Std Dev: {stdev_temp:.2f}

- Client Satisfaction Scores:
  - Min: {min_score}
  - Max: {max_score}
  - Mean: {mean_score:.2f}
  - Std Dev: {stdev_score:.2f}
"""

#####################################
# Define a function to return the byline.
#####################################

def get_byline() -> str:
    '''Return the byline string.'''
    return byline

#####################################
# Define a main() function for this module.
#####################################

def main() -> None:
    '''Print the byline returned by get_byline() to the console when this function is called.'''
    print(get_byline())

#####################################
# Conditional Execution - Only call main() when executing this module as a script.
#####################################

if __name__ == '__main__':
    main()
