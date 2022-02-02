import psutil


def performance_testing(**test_type):
    def inner(func):
        def wrapper(expected_mem, expected_cpu):
            if test_type['name'] == 'memory & cpu':
                actual_result_mem = psutil.virtual_memory().percent
                actual_result_cpu = psutil.cpu_percent()

                if actual_result_mem > expected_mem:
                    print(f'Memory high consumption: {actual_result_mem}')
                else:
                    print(f'Normal memory consumption: {actual_result_mem}')

                if actual_result_cpu > expected_cpu:
                    print(f'CPU high consumption: {actual_result_cpu}')
                else:
                    print(f'Normal CPU consumption: {actual_result_cpu}')

            else:
                print('Invalid test case')

            func(expected_mem, expected_cpu)

        return wrapper

    return inner


@performance_testing(name='memory')
def search_performance(expected_mem, expected_cpu):
    print(f'Expected memory value is: {expected_mem}')
    print(f'Expected CPU value is: {expected_cpu}')


search_performance(40, 50)
