def transform_data(df, steps_per_floor_):
    """Transform original dataset.

    :param df: Input DataFrame.
    :param steps_per_floor_: The number of steps per-floor at 43 Tanner
        Street.
    :return: Transformed DataFrame.
    """
    # df_transformed = (
    #     df
    #     .select(
    #         col('id'),
    #         concat_ws(
    #             ' ',
    #             col('first_name'),
    #             col('second_name')).alias('name'),
    #            (col('floor') * lit(steps_per_floor_)).alias('steps_to_desk')))

    return None