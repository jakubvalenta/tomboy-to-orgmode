# Tomboy to Org-mode

Convert Tomboy notes to an Emacs Org-mode file.

## Installation

``` shell
$ pip install --user .
```

The main executable will then be available globally:

``` shell
$ tomboy-to-orgmode --help
```

## Usage

`tomboy-to-orgmode` takes one positional argument -- the input directory
containing the Tomboy notes (it will be searched recursively).

The resulting org-mode file will be written to standard output.

Example:

``` shell
$ tomboy-to-orgmode ~/.local/share/tomboy > notes.org
```

You can try the script with the test data included in this repository:

``` shell
$ tomboy-to-orgmode tomboy_to_orgmode/tests/test_data
```

## Help

``` shell
$ tomboy-to-orgmode --help
```

## Development

### Installation

``` shell
make setup-dev
```

### Testing and linting

``` shell
make test
make lint
```

### Help

``` shell
make help
```

## Contributing

__Feel free to remix this project__ under the terms of the [Apache License,
Version 2.0](http://www.apache.org/licenses/LICENSE-2.0).
