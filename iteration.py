import string
from random import randint, choice
from timeit import timeit


class ListAppend():
    def __init__(self) -> None:
        self.iters = 1000
        self.repeat_num = 100

    def with_for(self):
        lst = []
        for i in range(self.iters):
            lst.append(i)
        
        return lst
    
    def without_for(self):
        return [i for i in range(self.iters)]
    
    def compare(self):
        time_with_for = timeit(self.with_for, number=self.repeat_num)
        time_without_for = timeit(self.without_for, number=self.repeat_num)
        print(f"===== {self.__class__.__name__} =====")
        print(f"With For: {time_with_for} Seconds")
        print(f"Without For: {time_without_for} Seconds")
        print(f"Without For {time_with_for/time_without_for}x Faster Than With For", end="\n\n")


class BuiltinMax():
    def __init__(self) -> None:
        self.repeat_num = 100
        self.gen_lb = -10000
        self.gen_ub = 10000
        self.lst_length = 100000
        self.search_lst = [randint(self.gen_lb, self.gen_ub) for _ in range(self.lst_length)]
    
    def custom_max(self):
        max_num = self.gen_lb
        for num in self.search_lst:
            if num > max_num:
                max_num = num
        
        return max_num
    
    def builtin_max(self):
        return max(self.search_lst)
    
    def compare(self):
        time_custom_max = timeit(self.custom_max, number=self.repeat_num)
        time_builtin_max = timeit(self.builtin_max, number=self.repeat_num)
        print(f"===== {self.__class__.__name__} =====")
        print(f"Custom Max: {time_custom_max} Seconds")
        print(f"Builtin Max: {time_builtin_max} Seconds")
        print(f"Builtin Max {time_custom_max/time_builtin_max}x Faster Than Custom Max", end="\n\n")


class BuiltinAny():
    def __init__(self) -> None:
        self.repeat_num = 100
        self.gen_lb = -10000
        self.gen_ub = 10000
        self.lst_length = 100000
        self.threshold = 9000
        self.search_lst = [randint(self.gen_lb, self.gen_ub) for _ in range(self.lst_length)]
    
    def custom_any(self):
        for num in self.search_lst:
            if num > self.threshold:
                return True
        
        return False
    
    def builtin_any(self):
        # 內建的 any 執行速度比較慢，但程式碼的可讀性較高
        return any(num > self.threshold for num in self.search_lst)
    
    def compare(self):
        time_custom_any = timeit(self.custom_any, number=self.repeat_num)
        time_builtin_any = timeit(self.builtin_any, number=self.repeat_num)
        print(f"===== {self.__class__.__name__} =====")
        print(f"Custom Any: {time_custom_any} Seconds")
        print(f"Builtin Any: {time_builtin_any} Seconds")
        print(f"Custom Any {time_custom_any/time_builtin_any}x Faster Than Builtin Any", end="\n\n")


class Filter():
    def __init__(self) -> None:
        self.repeat_num = 100
        self.gen_lb = 0
        self.gen_ub = 100
        self.lst_length = 100000
        self.pass_num = 60
        self.search_lst = [randint(self.gen_lb, self.gen_ub) for _ in range(self.lst_length)]
    
    def good(self, num):
        return num >= self.pass_num

    def custom_filter(self):
        ret = []
        for num in self.search_lst:
            if self.good(num):
                ret.append(num)
        return ret
    
    def builtin_filter(self):
        return list(filter(self.good, self.search_lst))
    
    def compare(self):
        time_custom_filter = timeit(self.custom_filter, number=self.repeat_num)
        time_builtin_filter = timeit(self.builtin_filter, number=self.repeat_num)
        print(f"===== {self.__class__.__name__} =====")
        print(f"Custom Filter: {time_custom_filter} Seconds")
        print(f"Builtin Filter: {time_builtin_filter} Seconds")
        print(f"Builtin Filter {time_custom_filter/time_builtin_filter}x Faster Than Custom Filter", end="\n\n")


class Mapping():
    def __init__(self) -> None:
        self.repeat_num = 100
        self.gen_lb = 0
        self.gen_ub = 100
        self.lst_length = 100000
        self.search_lst = [randint(self.gen_lb, self.gen_ub) for _ in range(self.lst_length)]
    
    def double(self, num):
        return num * 2
    
    def custom_map(self):
        ret = []
        for num in self.search_lst:
            ret.append(self.double(num))
        
        return ret
    
    def builtin_map(self):
        return list(map(self.double, self.search_lst))
    
    def compare(self):
        time_custom_map = timeit(self.custom_map, number=self.repeat_num)
        time_builtin_map = timeit(self.builtin_map, number=self.repeat_num)
        print(f"===== {self.__class__.__name__} =====")
        print(f"Custom Map: {time_custom_map} Seconds")
        print(f"Builtin Map: {time_builtin_map} Seconds")
        print(f"Builtin Map {time_custom_map/time_builtin_map}x Faster Than Custom Map", end="\n\n")


class Zipper():
    def __init__(self) -> None:
        self.repeat_num = 100
        self.lst_length = 100000
        self.gen_lb = 0
        self.gen_ub = 100
        self.alphabet = string.ascii_uppercase
        self.letters = string.ascii_letters
        self.names = [choice(self.letters) for _ in range(self.lst_length)]
        self.grades = [choice(self.alphabet) for _ in range(self.lst_length)]
        self.scores = [randint(self.gen_lb, self.gen_ub) for _ in range(self.lst_length)]
    
    def custom_zip(self):
        for idx in range(self.lst_length):
            name = self.names[idx]
            grade = self.grades[idx]
            score = self.scores[idx]
    
    def builtin_zip(self):
        for name, grade, score in zip(self.names, self.grades, self.scores):
            pass
    
    def compare(self):
        time_custom_zip = timeit(self.custom_zip, number=self.repeat_num)
        time_builtin_zip = timeit(self.builtin_zip, number=self.repeat_num)
        print(f"===== {self.__class__.__name__} =====")
        print(f"Custom Zip: {time_custom_zip} Seconds")
        print(f"Builtin Zip: {time_builtin_zip} Seconds")
        print(f"Builtin Zip {time_custom_zip/time_builtin_zip}x Faster Than Custom Zip", end="\n\n")

if __name__ == "__main__":
    case_list_append = ListAppend()
    case_list_append.compare()

    case_builtin_max = BuiltinMax()
    case_builtin_max.compare()

    case_builtin_any = BuiltinAny()
    case_builtin_any.compare()

    case_filter = Filter()
    case_filter.compare()

    case_mapping = Mapping()
    case_mapping.compare()

    case_zipper = Zipper()
    case_zipper.compare()