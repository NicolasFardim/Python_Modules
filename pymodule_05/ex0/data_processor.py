import typing
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
        self._rank: int = -1

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        self._rank += 1
        return self._rank, self._data.pop(0)


class NumericProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, list):
            for element in data:
                if not isinstance(element, (int, float)):
                    return False
            return True
        else:
            return False

    def ingest(self, data: int | float | list[int | float]) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for element in data:
                    self._data.append(str(element))
            else:
                self._data.append(str(data))
        else:
            raise TypeError('Improper numeric data')


class TextProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            for element in data:
                if not isinstance(element, str):
                    return False
            return True
        else:
            return False

    def ingest(self, data: str | list[str]) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for element in data:
                    self._data.append(element)
            else:
                self._data.append(data)
        else:
            raise TypeError('Improper string data')


class LogProcessor(DataProcessor):
    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            for key, value in data.items():
                if not isinstance(key, str) or not isinstance(value, str):
                    return False
            return True
        elif isinstance(data, list):
            for element in data:
                if not isinstance(element, dict):
                    return False
                for key, value in element.items():
                    if not isinstance(key, str) or not isinstance(value, str):
                        return False
            return True
        else:
            return False

    def ingest(self, data: dict[str, str] | list[dict[str, str]]) -> None:
        if self.validate(data):
            if isinstance(data, list):
                for element in data:
                    self._data.append(': '.join(element.values()))
            else:
                self._data.append(': '.join(data.values()))
        else:
            raise TypeError('Improper dict data')


def main() -> None:
    print('=== Code Nexus - Data Processor ===')

    numeric_processor = NumericProcessor()
    print('Testing Numeric Processor...')
    print(" Trying to validate input '42':", numeric_processor.validate(42))
    print(" Trying to validate input 'Hello':",
          numeric_processor.validate('Hello'))
    print(" Test invalid ingestion of string 'foo' without prior validation:")
    try:
        numeric_processor.ingest('foo')  # type: ignore[arg-type] # noqa
    except TypeError as e:
        print('Got exception:', e)
    data_numbers: list[int | float] = [1, 2, 3, 4, 5]
    print('Processing data:', data_numbers)
    numeric_processor.ingest(data_numbers)
    print('Extracting 3 values:')
    for i in range(3):
        rank, value = numeric_processor.output()
        print(f'Numeric Value {rank}: {value}')

    text_processor = TextProcessor()
    print('\nTesting Text Processor...')
    print(' Trying to validate input', text_processor.validate(42))
    data_text: list[str] = ['Hello', 'Nexus', 'World']
    print('Processing data:', data_text)
    text_processor.ingest(data_text)
    print('extracting 1 value...')
    rank, value = text_processor.output()
    print(f'Numeric Value {rank}: {value}')

    log_processor = LogProcessor()
    print('\nTesting Log Processor...')
    print(" Trying to validate input 'Hello'", log_processor.validate('Hello'))
    data_log: list[dict[str, str]] = [
        {'log_level': 'NOTICE', 'log_message': 'Connection to server'},
        {'log_level': 'ERROR', 'log_message': 'Unauthorized access!!'}
    ]
    print('Trying to validate data:', data_log)
    log_processor.ingest(data_log)
    print('Extracting 2 values...')
    for i in range(2):
        rank, value = log_processor.output()
        print(f'Log Entry {rank}: {value}')


if __name__ == '__main__':
    main()
