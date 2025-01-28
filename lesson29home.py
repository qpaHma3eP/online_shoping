from typing import Dict, Union

def add(a: Union[int, float], b: Union[int, float]) -> Dict[str, Union[int, float]]:
    result = a + b
    return {'operation': 'addition', 'result': result}

def subtract(a: Union[int, float], b: Union[int, float]) -> Dict[str, Union[int, float]]:
    result = a - b
    return {'operation': 'subtraction', 'result': result}

def multiply(a: Union[int, float], b: Union[int, float]) -> Dict[str, Union[int, float]]:
    result = a * b
    return {'operation': 'multiplication', 'result': result}

# Примеры использования
print(add(5, 3))        # {'operation': 'addition', 'result': 8}
print(subtract(10, 4))  # {'operation': 'subtraction', 'result': 6}
print(multiply(2, 7))   # {'operation': 'multiplication', 'result': 14}



from typing import Dict, Union
import logging

# Настраиваем логирование
logging.basicConfig(filename='errors.log', level=logging.ERROR,
                    format='%(asctime)s %(levelname)s:%(message)s')

def add(a: Union[int, float], b: Union[int, float]) -> Dict[str, Union[int, float]]:
    try:
        result = a + b
        return {'operation': 'addition', 'result': result}
    except Exception as e:
        logging.error(f"Error in addition function: {e}")
        return {'operation': 'addition', 'error': str(e)}

def subtract(a: Union[int, float], b: Union[int, float]) -> Dict[str, Union[int, float]]:
    try:
        result = a - b
        return {'operation': 'subtraction', 'result': result}
    except Exception as e:
        logging.error(f"Error in subtraction function: {e}")
        return {'operation': 'subtraction', 'error': str(e)}

def multiply(a: Union[int, float], b: Union[int, float]) -> Dict[str, Union[int, float]]:
    try:
        result = a * b
        return {'operation': 'multiplication', 'result': result}
    except Exception as e:
        logging.error(f"Error in multiplication function: {e}")
        return {'operation': 'multiplication', 'error': str(e)}

# Примеры использования
print(add(5, 'three'))        # Пример ошибки: {'operation': 'addition', 'error': "unsupported operand type(s) for +: 'int' and 'str'"}
print(subtract(10, 4))        # {'operation': 'subtraction', 'result': 6}
print(multiply(2, None))      # Пример ошибки: {'operation': 'multiplication', 'error': "unsupported operand type(s) for *: 'int' and 'NoneType'"}





