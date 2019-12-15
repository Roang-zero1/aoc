# Advent of Code 2019

## Processor

The processor has a logger that can be controlled through a `processor_logger.json` with the following format:

```json
{
    "all": false,
    "functions": ["continue_operation"]
}
```

### Logger configuration

-   all: Show debug output for all functions
-   functions: Show debug output for listed functions
