# Tomboy to org-mode

Convert Tomboy notes to an Emacs org-mode file.

## Installation

```
$ pip install --user .
```

The main executable will then be available globally:

```
$ tomboy-to-orgmode -h
```

## Usage

`tomboy-to-orgmode` takes one positional argument -- the input directory
containing the Tomboy notes (it will be searched recursively).

The resulting org-mode file will be written to standard output.

Example:

```
$ tomboy-to-orgmode ~/.local/share/tomboy > notes.org
```

## Help

```
$ tomboy-to-orgmode -h
```

## Contributing

__Feel free to remix this piece of software.__ See [NOTICE](./NOTICE) and [LICENSE](./LICENSE) for license information.
