from typing import Callable
import timeit

from bm import boyer_moore_search
from rk import rabin_karp_search
from kmp import kmp_search


def read_file(filename, enc="utf-8"):
    try:
        with open(filename, "r", encoding=enc, errors="ignore") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Файл не найден: {filename}")
        return ""
    except Exception as e:
        print(f"Ошибка при чтении {filename}: {e}")
        return ""


def benchmark(algorithm_func: Callable, text: str, pattern: str):
    setup = f"from __main__ import {algorithm_func.__name__}"
    stmt = f"{algorithm_func.__name__}(text, pattern)"
    return timeit.timeit(stmt=stmt, setup=setup, globals={"text": text, "pattern": pattern}, number=10)


if __name__ == "__main__":

    filenames = [("стаття 1.txt", "cp1251"),
                 ("стаття 2.txt", "utf-8-sig")]

    algorithms = [boyer_moore_search,
                  rabin_karp_search,
                  kmp_search]

    texts = [read_file(filename[0], enc=filename[1]) for filename in filenames]

    real_patterns = ["Автори публiкації",
                     "Література"]

    fake_pattern = "Люблять мене тваринки"

    patterns = real_patterns + [fake_pattern]

    results = []
    for itext, text in enumerate(texts):
        for algorithm in algorithms:
            for pattern in patterns:
                time = benchmark(algorithm, text, pattern)
                results.append(
                    (algorithm.__name__, pattern, text.find(pattern), itext, len(text), time))

    for result in results:
        algorithm, pattern, pos, itext, text_size, time = result
        pattern_name = "real pattern" if pattern in real_patterns else "fake pattern"
        pattern_str = f"{pattern_name}(pos={pos})"
        text_str = f"{filenames[itext][0]}({text_size})"

        print(f"{algorithm:^20}|{pattern_str:^30}|{text_str:^25}| {time:.8f}")
