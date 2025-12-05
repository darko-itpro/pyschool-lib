# Installing the dependency

## Get the latest version

Get (download) the `.whl` file for the latest release from 
[the releases page](https://github.com/darko-itpro/pyschool-lib/releases).

To make things easier later on, move the file to the project directory

## Install the dependency

The installation will be done via the command prompt (Terminal, Dos, PowerShell).

If necessary, make sure that the virtual env is enabled.

=== "Standard method"

    The command to execute should look like this:
    ```
    pip install pyflix-0.8.0-py3-none-any.whl
    ```

    Adapt the name of the file accordingly to the version number.

=== "With uv"

    If you are using uv, you can install the dependency with:
    ```
    uv add pyflix-0.8.0-py3-none-any.whl
    ```

    Adapt the name of the file accordingly to the version number.

