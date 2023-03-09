from fuzzywuzzy import fuzz as __fuzz__, process as __process__


def get_best_matches(query, data: list, max_results=10, case_senstivity=False, fuzzy_search=True) -> list[int]:
    '''
    Note : When `fuzzy_search` is set `True` then `case_senstivity` must be set to `False`.
    '''

    if case_senstivity and fuzzy_search:
        raise Exception(
            'When case_senstivity is set True then fuzzy_search must be set to False')

    query = str(object=query)

    if max_results <= 0:
        return []

    if not case_senstivity:
        query = query.lower()

    starts_with_indexes = []
    contains_indexes = []

    for index, element in enumerate(data):
        if len(starts_with_indexes) == int(max_results):
            break

        element_for_search = ''

        if not case_senstivity:
            element_for_search = str(element).lower()
        else:
            element_for_search = str(element)

        if element_for_search.startswith(query):
            starts_with_indexes.append(index)

        elif query in element_for_search:
            contains_indexes.append(index)

    if (fuzzy_search):
        fuzzy_search_results = __process__.extract(
            query, data, scorer=__fuzz__.token_sort_ratio, limit=max_results)

        fuzzy_indexes = []
        for element in fuzzy_search_results:
            fuzzy_indexes.append(data.index(element[0]))

        unique_indexes = []
        seen_indexes = []

        for index in starts_with_indexes + contains_indexes + fuzzy_indexes:
            if index not in seen_indexes:
                unique_indexes.append(index)
            seen_indexes.append(index)

        return unique_indexes

    else:
        return (starts_with_indexes + contains_indexes)[:int(max_results)]


if __name__ == "__main__":
    pass
