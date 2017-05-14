# Tomboy to org-mode

Convert Tomboy notes to an Emacs org-mode file.

## Installation

``` shell
#> python setup.py install
```

The main executable will then be available globally:

``` shell
$> tomboy-to-orgmode -h
```

## Usage

`tomboy-to-orgmode` takes one positional argument -- the input directory
containing the Tomboy notes (it will be searched recursively).

``` shell
$> tomboy-to-orgmode ~/.local/share/tomboy > notes.org
```

## Help

``` shell
$> tomboy-to-orgmode -h
```

## Contributing

__Feel free to remix this piece of software.__ See [NOTICE](./NOTICE) and [LICENSE](./LICENSE) for license information.
