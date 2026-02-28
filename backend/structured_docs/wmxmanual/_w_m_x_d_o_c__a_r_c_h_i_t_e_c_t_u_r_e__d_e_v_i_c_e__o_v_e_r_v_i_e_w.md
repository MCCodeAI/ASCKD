




WMX3 User Manual: Overview










| Logo | WMX3 User Manual  3.6u1 |
| --- | --- |







Overview  

In WMX3, user applications communicate with the WMX3 engine and each module through **devices**. The API function [CreateDevice](classwmx3_api_1_1_w_m_x3_api.html#acdf68c4d0df80ffe358ab80410053301) is called to create a new device. Through the device, the command from an API is sent to the WMX3 engine and the processing result is received.

Depending on the command type, a command could be processed immediately by the API process thread or added to an API queue to wait to be processed by an execution thread. In the latter case, if the device needs the processing result before continuing execution, it will block until an execution thread finishes processing the command and returns the result. Otherwise, the device will continue execution and leave the execution threads to process the command. In this case, the error code will be put into an error log buffer so that it can be retrieved later.

The following diagram shows the flow of data between devices and API execution threads.

![](WMXDOC_FUNC_ARCHITECTURE_image2.png)








