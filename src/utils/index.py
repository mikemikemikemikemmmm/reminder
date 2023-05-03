
from typing import Literal


def trans_date_str_to_second(val: str) -> int | Literal['error']:
    try:
        split_arr = val.split(":")
        min_str = split_arr[0]
        second_str = split_arr[1]
        min_num = 0
        second_num = 0
        if min_str[0] == "0":
            min_num = int(min_str[1])
        else:
            min_num = int(min_str)
        if second_str[0] == "0":
            second_num = int(second_str[1])
        else:
            second_num = int(second_str)
        return int(min_num)*60+int(second_num)
    except ValueError:
        return 'error'
