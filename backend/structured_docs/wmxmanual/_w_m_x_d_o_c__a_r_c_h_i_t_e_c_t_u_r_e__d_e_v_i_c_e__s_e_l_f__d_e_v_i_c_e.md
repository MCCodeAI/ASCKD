




WMX3 User Manual: Self Devices










| Logo | WMX3 User Manual  3.6u1 |
| --- | --- |







Self Devices  

Module classes containing the API functions use the device created by the [WMX3Api](classwmx3_api_1_1_w_m_x3_api.html) object that is passed to the constructors of these classes. These classes can also be instantiated using the default constructor with no arguments. In this case, the class is instantiated with a self device.

The module classes of the standard modules are as follows.

| Module | Class |
| --- | --- |
| CoreMotion | [CoreMotion](classwmx3_api_1_1_core_motion.html) |
| Log | [Log](classwmx3_api_1_1_log.html) |
| ApiBuffer | [ApiBuffer](classwmx3_api_1_1_api_buffer.html) |
| CyclicBuffer | [CyclicBuffer](classwmx3_api_1_1_cyclic_buffer.html) |
| Compensation | [Compensation](classwmx3_api_1_1_compensation.html) |
| IO | [Io](classwmx3_api_1_1_io.html) |
| Event | [EventControl](classwmx3_api_1_1_event_control.html) |
| AdvancedMotion | [AdvancedMotion](classwmx3_api_1_1_advanced_motion.html) |
| UserMemory | [UserMemory](classwmx3_api_1_1_user_memory.html) |
| PMMotion | [PMMotion](classwmx3_api_1_1_p_m_motion.html) |

A self device is a device that is created in the constructor of a module class. The self device is not associated with a [WMX3Api](classwmx3_api_1_1_w_m_x3_api.html) object instantiated by the user. The self device cannot be accessed directly, but allows the module class to call API functions without passing in a [WMX3Api](classwmx3_api_1_1_w_m_x3_api.html) object to the constructor.

The self device is closed in the destructor of the module class.

A self device cannot be created if the engine is not running when the constructor is called. The engine must first be started by creating a normal device elsewhere or calling the [StartEngine](classwmx3_api_1_1_w_m_x3_api.html#a1c5d4ea51b8b20fcaea20d467e48c216) function. (The [StartEngine](classwmx3_api_1_1_w_m_x3_api.html#a1c5d4ea51b8b20fcaea20d467e48c216) function can be called without creating a device.)

To determine if a self device has been successfully created, call the [IsDeviceValid](classwmx3_api_1_1_core_motion.html#a34ea4027f0c49ec21d6c40544c3a4cb2) function of the module class (the previous link links to the function of the [CoreMotion](classwmx3_api_1_1_core_motion.html) module class) after the constructor is called. If this function returns TRUE, a self device has been successfully created.








