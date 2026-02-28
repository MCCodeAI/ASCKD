




WMX3 User Manual: IOApi.h File Reference










| Logo | WMX3 User Manual  3.6u1 |
| --- | --- |







[Classes](#nested-classes) |
[Variables](#var-members) 
IOApi.h File Reference 

| Classes | |
| --- | --- |
| class | [IOErrorCode](classwmx3_api_1_1_i_o_error_code.html) |
|  | This enumerator class enumerates the WMX3 I/O library error codes. [More...](classwmx3_api_1_1_i_o_error_code.html#details) |
|  | |
| class | [IoLogInput](classwmx3_api_1_1_io_log_input.html) |
|  | This class specifies the log data to be collected by the Io module. [More...](classwmx3_api_1_1_io_log_input.html#details) |
|  | |
| class | [IoLogOutput](classwmx3_api_1_1_io_log_output.html) |
|  | This class contains data of the IO module that has been logged using the memory log operation. This class contains data over multiple cycles. [More...](classwmx3_api_1_1_io_log_output.html#details) |
|  | |
| class | [IoEventInput](classwmx3_api_1_1_io_event_input.html) |
|  | This class defines event input functions that can be processed by the Io module. Also see [I/O Inputs](_w_m_x_d_o_c__f_u_n_c__e_v_t__i_n_p_u_t__i_o.html). [More...](classwmx3_api_1_1_io_event_input.html#details) |
|  | |
| union | [IoEventInput::InputFunctionArguments](unionwmx3_api_1_1_io_event_input_1_1_input_function_arguments.html) |
|  | This union defines the structs containing arguments for each input function. [More...](unionwmx3_api_1_1_io_event_input_1_1_input_function_arguments.html#details) |
|  | |
| struct | [IoEventInput::InputFunctionArguments::IOBit](structwmx3_api_1_1_io_event_input_1_1_input_function_arguments_1_1_i_o_bit.html) |
|  | This structure contains arguments for the [IOBit](classwmx3_api_1_1_io_event_input.html#aa98cff7940af125e0c4388da928f6c2aa270abbe54a7b48da979efa93ee0208c1) input function. [More...](structwmx3_api_1_1_io_event_input_1_1_input_function_arguments_1_1_i_o_bit.html#details) |
|  | |
| struct | [IoEventInput::InputFunctionArguments::NotIOBit](structwmx3_api_1_1_io_event_input_1_1_input_function_arguments_1_1_not_i_o_bit.html) |
|  | This structure contains arguments for the [NotIOBit](classwmx3_api_1_1_io_event_input.html#aa98cff7940af125e0c4388da928f6c2aa8ad6b0145c24b702bf380feb73b9f465) input function. [More...](structwmx3_api_1_1_io_event_input_1_1_input_function_arguments_1_1_not_i_o_bit.html#details) |
|  | |
| struct | [IoEventInput::InputFunctionArguments::OrIOBit](structwmx3_api_1_1_io_event_input_1_1_input_function_arguments_1_1_or_i_o_bit.html) |
|  | This structure contains arguments for the [OrIOBit](classwmx3_api_1_1_io_event_input.html#aa98cff7940af125e0c4388da928f6c2aaf883071f860340d2d201f5339a1ff3c5) input function. [More...](structwmx3_api_1_1_io_event_input_1_1_input_function_arguments_1_1_or_i_o_bit.html#details) |
|  | |
| struct | [IoEventInput::InputFunctionArguments::AndIOBit](structwmx3_api_1_1_io_event_input_1_1_input_function_arguments_1_1_and_i_o_bit.html) |
|  | This structure contains arguments for the [AndIOBit](classwmx3_api_1_1_io_event_input.html#aa98cff7940af125e0c4388da928f6c2aa72ac88d695e943e684fa6fa72c209387) input function. [More...](structwmx3_api_1_1_io_event_input_1_1_input_function_arguments_1_1_and_i_o_bit.html#details) |
|  | |
| struct | [IoEventInput::InputFunctionArguments::XorIOBit](structwmx3_api_1_1_io_event_input_1_1_input_function_arguments_1_1_xor_i_o_bit.html) |
|  | This structure contains arguments for the [XorIOBit](classwmx3_api_1_1_io_event_input.html#aa98cff7940af125e0c4388da928f6c2aa528151ad8fcf3cbb9a1252ae258cdc16) input function. [More...](structwmx3_api_1_1_io_event_input_1_1_input_function_arguments_1_1_xor_i_o_bit.html#details) |
|  | |
| struct | [IoEventInput::InputFunctionArguments::NandIOBit](structwmx3_api_1_1_io_event_input_1_1_input_function_arguments_1_1_nand_i_o_bit.html) |
|  | This structure contains arguments for the [NandIOBit](classwmx3_api_1_1_io_event_input.html#aa98cff7940af125e0c4388da928f6c2aa9b04f9aedf0ba5c6b80fa1ad9e6da1d3) input function. [More...](structwmx3_api_1_1_io_event_input_1_1_input_function_arguments_1_1_nand_i_o_bit.html#details) |
|  | |
| struct | [IoEventInput::InputFunctionArguments::NorIOBit](structwmx3_api_1_1_io_event_input_1_1_input_function_arguments_1_1_nor_i_o_bit.html) |
|  | This structure contains arguments for the [NorIOBit](classwmx3_api_1_1_io_event_input.html#aa98cff7940af125e0c4388da928f6c2aa224456752f81f030a2aeacdcafc0e97c) input function. [More...](structwmx3_api_1_1_io_event_input_1_1_input_function_arguments_1_1_nor_i_o_bit.html#details) |
|  | |
| struct | [IoEventInput::InputFunctionArguments::XnorIOBit](structwmx3_api_1_1_io_event_input_1_1_input_function_arguments_1_1_xnor_i_o_bit.html) |
|  | This structure contains arguments for the [XnorIOBit](classwmx3_api_1_1_io_event_input.html#aa98cff7940af125e0c4388da928f6c2aa5d89f8ac0ee2eb803c7ce81402a59abb) input function. [More...](structwmx3_api_1_1_io_event_input_1_1_input_function_arguments_1_1_xnor_i_o_bit.html#details) |
|  | |
| struct | [IoEventInput::InputFunctionArguments::DelayIOBit](structwmx3_api_1_1_io_event_input_1_1_input_function_arguments_1_1_delay_i_o_bit.html) |
|  | This structure contains arguments for the [DelayIOBit](classwmx3_api_1_1_io_event_input.html#aa98cff7940af125e0c4388da928f6c2aac74bb7b5d4cffb8f633752a7e3396adb) input function. [More...](structwmx3_api_1_1_io_event_input_1_1_input_function_arguments_1_1_delay_i_o_bit.html#details) |
|  | |
| struct | [IoEventInput::InputFunctionArguments::EqualIOBytes](structwmx3_api_1_1_io_event_input_1_1_input_function_arguments_1_1_equal_i_o_bytes.html) |
|  | This structure contains arguments for the [EqualIOBytes](classwmx3_api_1_1_io_event_input.html#aa98cff7940af125e0c4388da928f6c2aa0377f5a4314d4111280034914873458c) input function. [More...](structwmx3_api_1_1_io_event_input_1_1_input_function_arguments_1_1_equal_i_o_bytes.html#details) |
|  | |
| struct | [IoEventInput::InputFunctionArguments::GreaterIOBytes](structwmx3_api_1_1_io_event_input_1_1_input_function_arguments_1_1_greater_i_o_bytes.html) |
|  | This structure contains arguments for the [GreaterIOBytes](classwmx3_api_1_1_io_event_input.html#aa98cff7940af125e0c4388da928f6c2aaf8f544a71ea77b5be1610a6f28b4eb93) input function. [More...](structwmx3_api_1_1_io_event_input_1_1_input_function_arguments_1_1_greater_i_o_bytes.html#details) |
|  | |
| struct | [IoEventInput::InputFunctionArguments::LessIOBytes](structwmx3_api_1_1_io_event_input_1_1_input_function_arguments_1_1_less_i_o_bytes.html) |
|  | This structure contains arguments for the [LessIOBytes](classwmx3_api_1_1_io_event_input.html#aa98cff7940af125e0c4388da928f6c2aab8e83678c490fd2d1b1156604de243e6) input function. [More...](structwmx3_api_1_1_io_event_input_1_1_input_function_arguments_1_1_less_i_o_bytes.html#details) |
|  | |
| class | [IoEventOutput](classwmx3_api_1_1_io_event_output.html) |
|  | This class defines event output functions that can be processed by the Io module. Also see [I/O Outputs](_w_m_x_d_o_c__f_u_n_c__e_v_t__o_u_t_p_u_t__i_o.html). [More...](classwmx3_api_1_1_io_event_output.html#details) |
|  | |
| union | [IoEventOutput::OutputFunctionArguments](unionwmx3_api_1_1_io_event_output_1_1_output_function_arguments.html) |
|  | This union defines the structs containing arguments for each output function. [More...](unionwmx3_api_1_1_io_event_output_1_1_output_function_arguments.html#details) |
|  | |
| struct | [IoEventOutput::OutputFunctionArguments::SetIOOutBit](structwmx3_api_1_1_io_event_output_1_1_output_function_arguments_1_1_set_i_o_out_bit.html) |
|  | This structure contains arguments for the [SetIOOutBit](classwmx3_api_1_1_io_event_output.html#a1d942dc6f7f93d498db989760b5287cfa38bfd384d3b42e08b1d69d5c1767cd07) output function. [More...](structwmx3_api_1_1_io_event_output_1_1_output_function_arguments_1_1_set_i_o_out_bit.html#details) |
|  | |
| class | [Io](classwmx3_api_1_1_io.html) |
|  | **This class contains I/O functions.**  [More...](classwmx3_api_1_1_io.html#details) |
|  | |

| Variables | |
| --- | --- |
| static const int | [maxIoLogAddressSize](namespacewmx3_api_1_1constants.html#a651cb70778c0abbf96c27b10e309e33e) = 256 |
|  | The maximum number of contiguous segments of the I/O space for which log data can be collected at one time (also see [I/O Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__i_o.html)). |
|  | |
| static const int | [maxIoLogFormatSize](namespacewmx3_api_1_1constants.html#a78b41431953d51c5506a295a4eeff144) = 100 |
|  | The maximum number of contiguous segments of the I/O space for which formatted log data can be collected at one time (also see [I/O Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__i_o.html)). |
|  | |
| static const int | [maxLogOutputIoInputByteSize](namespacewmx3_api_1_1constants.html#af4d8f6d674b60c64a89199f7ca99028d) = 128 |
|  | The maximum number of I/O input bytes that can be retrieved at one time using a derived class of [LogOutput](classwmx3_api_1_1_log_output.html) class. A byte is fully counted toward this limit even if only one bit of the byte is logged (also see [I/O Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__i_o.html)). |
|  | |
| static const int | [maxLogOutputIoOutputByteSize](namespacewmx3_api_1_1constants.html#a2a880123ed701e79557caba828db6ca3) = 128 |
|  | The maximum number of I/O output bytes that can be retrieved at one time using a derived class of [LogOutput](classwmx3_api_1_1_log_output.html) class. A byte is fully counted toward this limit even if only one bit of the byte is logged (also see [I/O Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__i_o.html)). |
|  | |




* [common](dir_bdd9a5d540de89e9fe90efdfc6973a4f.html)
* [include](dir_11fbc4217d50ab21044e5ad6614aede5.html)
* [IOApi.h](_i_o_api_8h.html)



