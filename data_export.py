import time

def measure_time(function, data: list, vbegin: int):
    # IDEA: zrobić tuple "parameters" rozpakowywaną we wnętrzu każdej funkcji
    start = time.clock()
    function(vbegin, data)
    end = time.clock()

    duration = end - start
    return duration

def measure_time(function, data: list):
    # IDEA: zrobić tuple "parameters" rozpakowywaną we wnętrzu każdej funkcji
    start = time.clock()
    function(data)
    end = time.clock()

    duration = end - start
    return duration

def export_data_to_file(filename: str, data: float):
    file = open(filename,"a")
    file.write("{0:02f}\n".format(data))
    file.close()
    return 0

if __name__ == "__main__":
    export_data_to_file(2,3,"data/wynik.txt", createList)
