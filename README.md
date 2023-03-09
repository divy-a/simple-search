# simple-search

A simple search algorithm that searches a `query` from given list of `data` and returns indexes of the best matches.

## Features

The best matches are arranged in the following **Priority Order**

`Priority = 1` If element of list starts with the query

`Priority = 2` If element of list contains the query

`Priority = 3` Fuzzy search results


## Usage

1. Install dependencies by `pip install -r requirements.txt`
2. `import simple_search`
3. Call `get_best_matches(query='app', data=['apple', 'application', 'cat'])`

## Parameters

`get_best_matches` has following parameters :

1. `query`
2. `data`
3. `max_results`
4. `case_senstivity`
5. `fuzzy_search`

Default value of parameters are :

1. `max_results` = `10`
2. `case_senstivity` = `False`
3. `fuzzy_search` = `True`

## Note

When `case_senstivity` is set `True` then `fuzzy_search` must be set to `False`
