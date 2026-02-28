




WMX3 User Manual: Overview of the Architecture










| Logo | WMX3 User Manual  3.6u1 |
| --- | --- |







Overview of the Architecture  

WMX3 provides a flexible architecture in which it is easy to develop a new function or extend an existing function. All functions are implemented in rtdlls that can be loaded to use the contained functions.

Modules that will not be used can be disabled to save system resources.

Advantages of the WMX3 architecture include:

* Function improvements and issue fixes do not require a whole system update every time.

* Load a different platform module to change to a different communication protocol with no changes to the user application.

* Multiple platform modules can be loaded to implement hybrid communication protocols in the same system.

* Easy to implement specialized control functions by developing a user rtdll. WMX3 provides pre-defined interfaces which the developer can fill with their code, and the code will be executed by the system at the appropriate timing. The developer can focus on the important code without caring too much about system details. (The user rtdll development library is an optional component.)

* Modules can exchange data with other modules at high speed.

The following diagrams show the overall flow of data in the WMX3 architecture.

The case in which WMX3 is operated from a user application on the non real-time os and WMX3 engine runs on real-time os:

![](WMXDOC_FUNC_ARCHITECTURE_2_image0.png)

The case in which WMX3 is operated from a user application on the real-time os:

![](WMXDOC_FUNC_ARCHITECTURE_2_image1.png)

The case in which WMX3 is operated from a user application on the non real-time os and WMX3 engine does not run in real-time space:

![](WMXDOC_FUNC_ARCHITECTURE_2_image2.png)








