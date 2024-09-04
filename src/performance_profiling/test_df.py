from src.performance_profiling.df_row import DfRow


def odd_even():
    return DfRow([{"a": 1, "b": 3}, {"a": 2, "b": 4}])


def test_filter():
    def odd(a, b):
        return (a % 2) == 1

    df = odd_even()
    assert df.filter(odd).eq(DfRow([{"a": 1, "b": 3}]))
