"""
A wrapper for InfluxDB that utilises existing models for ease of use
"""
import time
import logging

from django.conf import settings
from influxdb import InfluxDBClient

logger = logging.getLogger(__name__)

client = InfluxDBClient(
    settings.INFLUX['HOST'],
    settings.INFLUX['PORT'],
    settings.INFLUX['USER'],
    settings.INFLUX['PASSWORD'],
    settings.INFLUX['DATABASE']
)
class InfluxWrapper:

    def get_timeseries(self, device, wns=None, start=None, end=None, resolution='1h'):
        if start is None:
            raise KeyError('`start` cannot be None')
        if end is None:
            raise KeyError('`end` cannot be None')
        # Query database
        _start = time.time()
        result = client.query(
            # f"SELECT value FROM {wns} WHERE time > '{start}' AND time < '{end}' AND device =~ /{device}/"
            f"SELECT mean(value) FROM {device} WHERE time > '{start}' AND time < '{end}' GROUP BY time({resolution})",
        )
        _end = time.time()
        logger.info('Timeserie retrieval took %f seconds', _end-_start)
        return result

