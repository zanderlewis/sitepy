# Using the custom logger

The custom logger built into `sitepy` gives a more flexable way to log.

Example Usage:

```python
logger = Logger('app.log', console_output=True, max_size=1024, backup_count=5)

logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')
```
