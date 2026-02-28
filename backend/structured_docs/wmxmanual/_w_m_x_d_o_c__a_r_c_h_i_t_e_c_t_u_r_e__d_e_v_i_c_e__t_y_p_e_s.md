




WMX3 User Manual: Device Types










| Logo | WMX3 User Manual  3.6u1 |
| --- | --- |







Device Types  

The device type of a device determines several characteristics of the device.

The device type is specified as an argument to the [CreateDevice](classwmx3_api_1_1_w_m_x3_api.html#acdf68c4d0df80ffe358ab80410053301) function when creating the device. The device types are enumerated in the [DeviceType](classwmx3_api_1_1_device_type.html) enumerator.

When the device type is not specified, a device of the [Normal](classwmx3_api_1_1_device_type.html#adf1f3edb9115acb0a1e04209b7a9937bae40ff47c3f7f24f01e4035eed7b6a19d) device type will be created. Most user applications should only use the [Normal](classwmx3_api_1_1_device_type.html#adf1f3edb9115acb0a1e04209b7a9937bae40ff47c3f7f24f01e4035eed7b6a19d) device type.

The four kinds of devices are listed in the following table.

| Device Type | Low Priority | ExitWOCnt |
| --- | --- | --- |
| [Normal](classwmx3_api_1_1_device_type.html#adf1f3edb9115acb0a1e04209b7a9937bae40ff47c3f7f24f01e4035eed7b6a19d) | No | No |
| [DeviceTypeLowPriority](classwmx3_api_1_1_device_type.html#adf1f3edb9115acb0a1e04209b7a9937bae7b05679d35c8994311a08a35598fd6b) | Yes | No |
| [DeviceTypeExitWOCnt](classwmx3_api_1_1_device_type.html#adf1f3edb9115acb0a1e04209b7a9937ba70d89afb87e05ef19b6abc13a0e3e12d) | No | Yes |
| [DeviceTypeLowpriorityExitWOCnt](classwmx3_api_1_1_device_type.html#adf1f3edb9115acb0a1e04209b7a9937bae096d01b4b893a2a44d016d3b4318666) | Yes | Yes |

There is a dedicated API process thread for each normal (non-low priority) device. The command processing and response are very fast for normal devices. As long as a CPU core allocated to the real time operating system is available, API function calls are immediately processed and the response is returned. In the case of [Function Calls That Are Blocking](_w_m_x_d_o_c__a_r_c_h_i_t_e_c_t_u_r_e__b_l_k.html), the response may be delayed until the end of the next communication cycle.

For low priority devices, commands are processed one by one after the system process is finished at the end of each communication cycle. If there is a command already being processed, commands from other low priority devices must wait. Low priority devices are only used for tasks which do not require fast response times.

Whenever a device is closed with the [CloseDevice](classwmx3_api_1_1_w_m_x3_api.html#a8981447f9e6d6cff79ca79bede6e647b) function, the engine checks for the number of remaining devices. When there are no remaining devices, the engine will exit. Device types labeled "ExitWOCnt" are not counted when checking for the number of remaining devices. When the engine exits with "ExitWOCnt" devices remaining, API functions that are subsequently called through these devices will return the [IMLibIsNotRunning](classwmx3_api_1_1_error_code.html#ac36f475ca5b446f4fde4c9b90bec77c8a5b9326e1c050de806ca54458de9b4647) error.








