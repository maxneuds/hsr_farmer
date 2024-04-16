```
Traceback (most recent call last):
  File "/home/max/dev/hsr_farmer/src/main.py", line 77, in <module>
    
  File "/home/max/.pyenv/versions/3.12.1/lib/python3.12/asyncio/runners.py", line 194, in run
    return runner.run(main)
           ^^^^^^^^^^^^^^^^
  File "/home/max/.pyenv/versions/3.12.1/lib/python3.12/asyncio/runners.py", line 118, in run
    return self._loop.run_until_complete(task)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/max/.pyenv/versions/3.12.1/lib/python3.12/asyncio/base_events.py", line 684, in run_until_complete
    return future.result()
           ^^^^^^^^^^^^^^^
  File "/home/max/dev/hsr_farmer/src/main.py", line 53, in main
    await penacony.farm_clock_studios_theme_park() # (7648/7648) 231764
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/max/dev/hsr_farmer/src/farmer/penacony.py", line 105, in farm_clock_studios_theme_park
    await self.clock_studios_theme_park.path_8()
  File "/home/max/dev/hsr_farmer/src/worlds/penacony.py", line 1102, in path_8
    await self.bot.attack_technique(4)
  File "/home/max/dev/hsr_farmer/src/automation/bot.py", line 321, in attack_technique
    await self.action_technique()
  File "/home/max/dev/hsr_farmer/src/automation/bot.py", line 315, in action_technique
    await self.dev.shell(f'input tap {self.xy.technique[0]} {self.xy.technique[1]}')
  File "/home/max/.cache/pypoetry/virtualenvs/hsr-farmer-5OLGoxZI-py3.12/lib/python3.12/site-packages/ppadb/command/transport_async/__init__.py", line 14, in shell
    conn = await self.create_connection(timeout=timeout)
           ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/max/.cache/pypoetry/virtualenvs/hsr-farmer-5OLGoxZI-py3.12/lib/python3.12/site-packages/ppadb/device_async.py", line 35, in create_connection
    await self.transport(conn)
  File "/home/max/.cache/pypoetry/virtualenvs/hsr-farmer-5OLGoxZI-py3.12/lib/python3.12/site-packages/ppadb/command/transport_async/__init__.py", line 9, in transport
    await connection.send(cmd)
  File "/home/max/.cache/pypoetry/virtualenvs/hsr-farmer-5OLGoxZI-py3.12/lib/python3.12/site-packages/ppadb/connection_async.py", line 73, in send
    return await self._check_status()
           ^^^^^^^^^^^^^^^^^^^^^^^^^^
  File "/home/max/.cache/pypoetry/virtualenvs/hsr-farmer-5OLGoxZI-py3.12/lib/python3.12/site-packages/ppadb/connection_async.py", line 79, in _check_status
    raise RuntimeError("ERROR: {} {}".format(repr(recv), error))
RuntimeError: ERROR: 'FAIL' 000edevice offline
```