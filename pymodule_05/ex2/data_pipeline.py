import typing
from abc import ABC, abstractmethod
from typing import Protocol


class DataProcessor(ABC):
    def __init__(self) -> None:
        self._data: list[str] = []
        self._name = (self.__class__.__name__.
                      replace("Processor", " Processor"))
        self._rank: int = -1
        self._total: int = 0

    def get_data(self) -> list[str]:
        return self._data

    def get_total(self) -> int:
        return self._total

    def get_name(self) -> str:
        return self._name

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        self._rank += 1
        return self._rank, self._data.pop(0)

    def add_data(self, data: str) -> None:
        self._data.append(data)
        self._total += 1


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
                    self.add_data(str(element))
            else:
                self.add_data(str(data))
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
                    self.add_data(element)
            else:
                self.add_data(data)
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
                    self.add_data(': '.join(element.values()))
            else:
                self.add_data(': '.join(data.values()))
        else:
            raise TypeError('Improper dict data')


class ExportPlugin(Protocol):
    def process_output(self, data: list[tuple[int, str]]) -> None:
        ...


class CSVPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:  # noqa
        print("CSV output:")
        print(",".join(value for _, value in data))


class JSONPlugin:
    def process_output(self, data: list[tuple[int, str]]) -> None:  # noqa
        print("JSON output:")
        print("{" +
              ", ".join(f'"item_{str(key)}": "{value}"'
                        for key, value in data)
              + "}")


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
            return
        for processor in self._processors:
            print(f"{processor.get_name()}:"
                  f" total {processor.get_total()} items processed,"
                  f" remaining {len(processor.get_data())} on processor")

    def output_pipeline(self, nb: int, plugin: ExportPlugin) -> None:
        for proc in self._processors:
            pipe: list[tuple[int, str]] = []
            for _ in range(nb):
                if not proc.get_data():
                    break
                pipe.append(proc.output())
            if pipe:
                plugin.process_output(pipe)


def main() -> None:
    # processors
    num_proc = NumericProcessor()
    log_proc = LogProcessor()
    text_proc = TextProcessor()

    # random data
    data_batch1: list[typing.Any] = [
        'Hello world',
        [3.14, -1, 2.71],
        [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'},
         {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
        42,
        ['Hi', 'five']
    ]

    data_batch2: list[typing.Any] = [
        21,
        ['I love AI', 'LLMs are wonderful', 'Stay healthy'],
        [
            {'log_level': 'ERROR',
             'log_message': '500 server crash'},
            {'log_level': 'NOTICE',
             'log_message': 'Certificate expires in 10 days'}
        ],
        [32, 42, 64, 84, 128, 168],
        'World hello'
    ]

    print("=== Code Nexus - Data Pipeline ===\n")
    print("Initialize Data Stream...")
    data_stream = DataStream()
    data_stream.print_processors_stats()

    print("\nRegistering Processors")
    data_stream.register_processor(num_proc)
    data_stream.register_processor(text_proc)
    data_stream.register_processor(log_proc)

    print("\nSend first batch of data on stream:", data_batch1)
    data_stream.process_stream(data_batch1)
    data_stream.print_processors_stats()

    print("\nSend 3 processed data from each processor to a CSV plugin")
    data_stream.output_pipeline(3, CSVPlugin())

    print("\nSend another batch of data:", data_batch2)
    data_stream.process_stream(data_batch2)
    data_stream.print_processors_stats()

    print("\nSend 5 processed data from each processor to a JSON plugin")
    data_stream.output_pipeline(5, JSONPlugin())
    data_stream.print_processors_stats()


if __name__ == '__main__':
    main()
