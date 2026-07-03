import typing
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
        self._rank: int = -1
        self._total: int = 0

    def get_data(self):
        return self._data

    def get_total(self):
        return self._total

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
        if isinstance(data, list):
            for element in data:
                if not isinstance(element, (int, float)):
                    return False
            return True
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
        if isinstance(data, list):
            for element in data:
                if not isinstance(element, str):
                    return False
            return True
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
        if isinstance(data, list):
            for element in data:
                if not isinstance(element, dict):
                    return False
                for key, value in element.items():
                    if not isinstance(key, str) or not isinstance(value, str):
                        return False
            return True
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


class DataStream:
    def __init__(self) -> None:
        self._processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self._processors.append(proc)

    def process_stream(self, stream: list[typing.Any]) -> None:
        for data in stream:
            for process in self._processors:
                if process.validate(data):
                    process.ingest(data)
                    break
            else:
                print("DataStream error - Can't process element in stream:", data)

    def print_processors_stats(self) -> None:
        print("=== DataStream statistics ===")
        if not self._processors:
            print("No processors found, no data")
        for processor in self._processors:
            print(f"{processor.__class__.__name__}: total "
                  f"{len(processor.get_data())} items processed,"
                  f" remaining {processor.get_total()} on processor")


def main() -> None:
    # processors
    num_proc = NumericProcessor()
    log_proc = LogProcessor()
    text_proc = TextProcessor()

    # random data
    data_batch1 = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
    ]

    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("\nRegistering Numeric Processor")
    data_stream.register_processor(num_proc)

    # processing data
    print("Send first batch of data on stream:", data_batch1)
    data_stream.process_stream(data_batch1)
    data_stream.print_processors_stats()

    print("\nRegistering other data processors"
          "\nSend same batch again")
    data_stream.register_processor(text_proc)
    data_stream.register_processor(log_proc)
    data_stream.process_stream(data_batch1)
    data_stream.print_processors_stats()
    print("\nConsume some elements from the data processors:"
          "Numeric 3, Text 2, Log 1")
    for _ in range(3):
        num_proc.output()
    for _ in range(2):
        text_proc.output()
    log_proc.output()
    data_stream.print_processors_stats()


if __name__ == '__main__':
    main()
