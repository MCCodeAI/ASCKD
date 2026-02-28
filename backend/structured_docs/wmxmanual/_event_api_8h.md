




WMX3 User Manual: EventApi.h File Reference










| Logo | WMX3 User Manual  3.6u1 |
| --- | --- |







[Classes](#nested-classes) |
[Variables](#var-members) 
EventApi.h File Reference 

| Classes | |
| --- | --- |
| class | [EventErrorCode](classwmx3_api_1_1_event_error_code.html) |
|  | This enumerator class enumerates the WMX3 event library error codes. [More...](classwmx3_api_1_1_event_error_code.html#details) |
|  | |
| class | [EventOption](classwmx3_api_1_1_event_option.html) |
|  | This class contains the options of an event. [More...](classwmx3_api_1_1_event_option.html#details) |
|  | |
| class | [CustomEventOption](classwmx3_api_1_1_custom_event_option.html) |
|  | Reserved. [More...](classwmx3_api_1_1_custom_event_option.html#details) |
|  | |
| class | [AllEventID](classwmx3_api_1_1_all_event_i_d.html) |
|  | This class contains the event ID numbers of all defined events. [More...](classwmx3_api_1_1_all_event_i_d.html#details) |
|  | |
| class | [EventApiEventInput](classwmx3_api_1_1_event_api_event_input.html) |
|  | This class defines event input functions that can be processed by the Event module. Also see [Event Inputs](_w_m_x_d_o_c__f_u_n_c__e_v_t__i_n_p_u_t__e_v_e_n_t.html). [More...](classwmx3_api_1_1_event_api_event_input.html#details) |
|  | |
| union | [EventApiEventInput::InputFunctionArguments](unionwmx3_api_1_1_event_api_event_input_1_1_input_function_arguments.html) |
|  | This union defines the structs containing arguments for each input function. [More...](unionwmx3_api_1_1_event_api_event_input_1_1_input_function_arguments.html#details) |
|  | |
| struct | [EventApiEventInput::InputFunctionArguments::None](structwmx3_api_1_1_event_api_event_input_1_1_input_function_arguments_1_1_none.html) |
|  | This structure contains arguments for the [None](classwmx3_api_1_1_event_api_event_input.html#aeba49bedcd09d1a190fd4f3d92c34d77ac9d3e887722f2bc482bcca9d41c512af) input function. [More...](structwmx3_api_1_1_event_api_event_input_1_1_input_function_arguments_1_1_none.html#details) |
|  | |
| struct | [EventApiEventInput::InputFunctionArguments::AnotherEvent](structwmx3_api_1_1_event_api_event_input_1_1_input_function_arguments_1_1_another_event.html) |
|  | This structure contains arguments for the [AnotherEvent](classwmx3_api_1_1_event_api_event_input.html#aeba49bedcd09d1a190fd4f3d92c34d77a8ab51f5e6e0017c883128df5f86214fc) input function. [More...](structwmx3_api_1_1_event_api_event_input_1_1_input_function_arguments_1_1_another_event.html#details) |
|  | |
| struct | [EventApiEventInput::InputFunctionArguments::DelayAnotherEvent](structwmx3_api_1_1_event_api_event_input_1_1_input_function_arguments_1_1_delay_another_event.html) |
|  | This structure contains arguments for the [DelayAnotherEvent](classwmx3_api_1_1_event_api_event_input.html#aeba49bedcd09d1a190fd4f3d92c34d77a7cf28eec2ec8d20ed6d4c98ac3f336f9) input function. [More...](structwmx3_api_1_1_event_api_event_input_1_1_input_function_arguments_1_1_delay_another_event.html#details) |
|  | |
| struct | [EventApiEventInput::InputFunctionArguments::OrEvent](structwmx3_api_1_1_event_api_event_input_1_1_input_function_arguments_1_1_or_event.html) |
|  | This structure contains arguments for the [OrEvent](classwmx3_api_1_1_event_api_event_input.html#aeba49bedcd09d1a190fd4f3d92c34d77a48e7d3b303a3071d90c04d3e075a7331) input function. [More...](structwmx3_api_1_1_event_api_event_input_1_1_input_function_arguments_1_1_or_event.html#details) |
|  | |
| struct | [EventApiEventInput::InputFunctionArguments::AndEvent](structwmx3_api_1_1_event_api_event_input_1_1_input_function_arguments_1_1_and_event.html) |
|  | This structure contains arguments for the [AndEvent](classwmx3_api_1_1_event_api_event_input.html#aeba49bedcd09d1a190fd4f3d92c34d77a134fffb4f6bacd20e6053251e8b6aadf) input function. [More...](structwmx3_api_1_1_event_api_event_input_1_1_input_function_arguments_1_1_and_event.html#details) |
|  | |
| struct | [EventApiEventInput::InputFunctionArguments::XorEvent](structwmx3_api_1_1_event_api_event_input_1_1_input_function_arguments_1_1_xor_event.html) |
|  | This structure contains arguments for the [XorEvent](classwmx3_api_1_1_event_api_event_input.html#aeba49bedcd09d1a190fd4f3d92c34d77aec3d559f91705cdca5d356514d00c5d2) input function. [More...](structwmx3_api_1_1_event_api_event_input_1_1_input_function_arguments_1_1_xor_event.html#details) |
|  | |
| struct | [EventApiEventInput::InputFunctionArguments::DeviceCloseEvent](structwmx3_api_1_1_event_api_event_input_1_1_input_function_arguments_1_1_device_close_event.html) |
|  | This structure contains arguments for the [DeviceCloseEvent](classwmx3_api_1_1_event_api_event_input.html#aeba49bedcd09d1a190fd4f3d92c34d77adcdbd8e451e997953a8dfb49d45688c9) input function. [More...](structwmx3_api_1_1_event_api_event_input_1_1_input_function_arguments_1_1_device_close_event.html#details) |
|  | |
| struct | [EventApiEventInput::InputFunctionArguments::DeviceTimeoutEvent](structwmx3_api_1_1_event_api_event_input_1_1_input_function_arguments_1_1_device_timeout_event.html) |
|  | This structure contains arguments for the [DeviceTimeoutEvent](classwmx3_api_1_1_event_api_event_input.html#aeba49bedcd09d1a190fd4f3d92c34d77a8961777c17d9684f091f4a09bf3adaf1) input function. [More...](structwmx3_api_1_1_event_api_event_input_1_1_input_function_arguments_1_1_device_timeout_event.html#details) |
|  | |
| class | [EventApiEventOutput](classwmx3_api_1_1_event_api_event_output.html) |
|  | This class defines event output functions that can be processed by the Event module. Also see [Event Outputs](_w_m_x_d_o_c__f_u_n_c__e_v_t__o_u_t_p_u_t__e_v_e_n_t.html). [More...](classwmx3_api_1_1_event_api_event_output.html#details) |
|  | |
| union | [EventApiEventOutput::OutputFunctionArguments](unionwmx3_api_1_1_event_api_event_output_1_1_output_function_arguments.html) |
|  | This union defines the structs containing arguments for each output function. [More...](unionwmx3_api_1_1_event_api_event_output_1_1_output_function_arguments.html#details) |
|  | |
| struct | [EventApiEventOutput::OutputFunctionArguments::None](structwmx3_api_1_1_event_api_event_output_1_1_output_function_arguments_1_1_none.html) |
|  | This structure contains arguments for the [None](classwmx3_api_1_1_event_api_event_output.html#ab5e5cca1e76aa15874cbec1bcf832a8aac9d3e887722f2bc482bcca9d41c512af) output function. [More...](structwmx3_api_1_1_event_api_event_output_1_1_output_function_arguments_1_1_none.html#details) |
|  | |
| struct | [EventApiEventOutput::OutputFunctionArguments::EnableAnotherEvent](structwmx3_api_1_1_event_api_event_output_1_1_output_function_arguments_1_1_enable_another_event.html) |
|  | This structure contains arguments for the [EnableAnotherEvent](classwmx3_api_1_1_event_api_event_output.html#ab5e5cca1e76aa15874cbec1bcf832a8aaf072e7339a53c9ecc88921a995497ad2) output function. [More...](structwmx3_api_1_1_event_api_event_output_1_1_output_function_arguments_1_1_enable_another_event.html#details) |
|  | |
| class | [EventControl](classwmx3_api_1_1_event_control.html) |
|  | **This class contains event control functions.**  [More...](classwmx3_api_1_1_event_control.html#details) |
|  | |
| class | [EventControl::EventInputFunction](classwmx3_api_1_1_event_control_1_1_event_input_function.html) |
|  | This enumerator class enumerates the input functions of events. The input function determines the condition at which the event is triggered. ***This class is deprecated and will be removed in a future version. Use the [EventInput](classwmx3_api_1_1_event_input.html) class and its inherited classes instead.*** [More...](classwmx3_api_1_1_event_control_1_1_event_input_function.html#details) |
|  | |
| class | [EventControl::EventOutputFunction](classwmx3_api_1_1_event_control_1_1_event_output_function.html) |
|  | This enumerator class enumerates the output functions of events. The output function determines the action that is executed when the event is triggered. ***This class is deprecated and will be removed in a future version. Use the [EventOutput](classwmx3_api_1_1_event_output.html) class and its inherited classes instead.*** [More...](classwmx3_api_1_1_event_control_1_1_event_output_function.html#details) |
|  | |
| class | [EventControl::Event](classwmx3_api_1_1_event_control_1_1_event.html) |
|  | This class defines an event. ***This class is deprecated and will be removed in a future version. Use the [EventInput](classwmx3_api_1_1_event_input.html) and [EventOutput](classwmx3_api_1_1_event_output.html) classes and their inherited classes instead.*** [More...](classwmx3_api_1_1_event_control_1_1_event.html#details) |
|  | |
| union | [EventControl::Event::InputFunctionArguments](unionwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments.html) |
|  | This union defines the structs containing arguments for each input function type. [More...](unionwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::None](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_none.html) |
|  | This structure contains arguments for the [None](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937bac9d3e887722f2bc482bcca9d41c512af) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_none.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::IOBit](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_i_o_bit.html) |
|  | This structure contains arguments for the [IOBit](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba270abbe54a7b48da979efa93ee0208c1) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_i_o_bit.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::NotIOBit](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_not_i_o_bit.html) |
|  | This structure contains arguments for the [NotIOBit](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba8ad6b0145c24b702bf380feb73b9f465) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_not_i_o_bit.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::OrIOBit](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_or_i_o_bit.html) |
|  | This structure contains arguments for the [OrIOBit](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937baf883071f860340d2d201f5339a1ff3c5) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_or_i_o_bit.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::AndIOBit](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_and_i_o_bit.html) |
|  | This structure contains arguments for the [AndIOBit](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba72ac88d695e943e684fa6fa72c209387) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_and_i_o_bit.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::XorIOBit](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_xor_i_o_bit.html) |
|  | This structure contains arguments for the [XorIOBit](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba528151ad8fcf3cbb9a1252ae258cdc16) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_xor_i_o_bit.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::NandIOBit](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_nand_i_o_bit.html) |
|  | This structure contains arguments for the [NandIOBit](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba9b04f9aedf0ba5c6b80fa1ad9e6da1d3) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_nand_i_o_bit.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::NorIOBit](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_nor_i_o_bit.html) |
|  | This structure contains arguments for the [NorIOBit](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba224456752f81f030a2aeacdcafc0e97c) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_nor_i_o_bit.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::XnorIOBit](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_xnor_i_o_bit.html) |
|  | This structure contains arguments for the [XnorIOBit](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba5d89f8ac0ee2eb803c7ce81402a59abb) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_xnor_i_o_bit.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::DelayIOBit](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_delay_i_o_bit.html) |
|  | This structure contains arguments for the [DelayIOBit](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937bac74bb7b5d4cffb8f633752a7e3396adb) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_delay_i_o_bit.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::MBit](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_m_bit.html) |
|  | This structure contains arguments for the [MBit](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba0ab601084c8f52c8a333ecc5d4015a0b) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_m_bit.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::NotMBit](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_not_m_bit.html) |
|  | This structure contains arguments for the [NotMBit](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba7cbd13c1a3dddf5a967b518417215bb6) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_not_m_bit.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::OrMBit](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_or_m_bit.html) |
|  | This structure contains arguments for the [OrMBit](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba9e1a292bd218ff60a8c200a7fadb3b9e) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_or_m_bit.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::AndMBit](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_and_m_bit.html) |
|  | This structure contains arguments for the [AndMBit](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937badb86852930a110c737e88b8337cef27a) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_and_m_bit.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::XorMBit](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_xor_m_bit.html) |
|  | This structure contains arguments for the [XorMBit](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba2a1e17427bff1fa1565409e8e1766f50) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_xor_m_bit.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::NandMBit](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_nand_m_bit.html) |
|  | This structure contains arguments for the [NandMBit](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba4f110674dc04b7be5b000e6b908e3d9a) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_nand_m_bit.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::NorMBit](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_nor_m_bit.html) |
|  | This structure contains arguments for the [NorMBit](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937bacef6bdfa501c846bf3f3b752df0cedf1) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_nor_m_bit.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::XnorMBit](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_xnor_m_bit.html) |
|  | This structure contains arguments for the [XnorMBit](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937baa9be708909be138803ea54f31d387a0e) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_xnor_m_bit.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::DelayMBit](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_delay_m_bit.html) |
|  | This structure contains arguments for the [DelayMBit](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba60da9b59c124e4dc575982d0dbc0fe27) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_delay_m_bit.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::AnotherEvent](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_another_event.html) |
|  | This structure contains arguments for the [AnotherEvent](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba8ab51f5e6e0017c883128df5f86214fc) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_another_event.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::DelayAnotherEvent](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_delay_another_event.html) |
|  | This structure contains arguments for the [DelayAnotherEvent](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba7cf28eec2ec8d20ed6d4c98ac3f336f9) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_delay_another_event.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::EqualPos](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_equal_pos.html) |
|  | This structure contains arguments for the [EqualPos](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937baa74e965750aea4a17887734138db9f72) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_equal_pos.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::GreaterPos](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_greater_pos.html) |
|  | This structure contains arguments for the [GreaterPos](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937bad173a0feea690d3d9ff83bca77091d48) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_greater_pos.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::LessPos](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_less_pos.html) |
|  | This structure contains arguments for the [LessPos](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937baa6ec394263a51fb5805253067461ef7c) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_less_pos.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::EqualVelocity](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_equal_velocity.html) |
|  | This structure contains arguments for the [EqualVelocity](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba333986b493ef74a2fb4427ea432fc7d7) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_equal_velocity.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::GreaterVelocity](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_greater_velocity.html) |
|  | This structure contains arguments for the [GreaterVelocity](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba0a48cf3780ada331be8dede39292293e) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_greater_velocity.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::LessVelocity](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_less_velocity.html) |
|  | This structure contains arguments for the [LessVelocity](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba85c0980027b4f6aeec9a726c242d1e7b) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_less_velocity.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::EqualTrq](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_equal_trq.html) |
|  | This structure contains arguments for the [EqualTrq](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba56ac11967b99ce392b579000835ad371) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_equal_trq.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::GreaterTrq](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_greater_trq.html) |
|  | This structure contains arguments for the [GreaterTrq](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba9bc04c8f39f9830cc93777c11248174d) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_greater_trq.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::LessTrq](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_less_trq.html) |
|  | This structure contains arguments for the [LessTrq](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937babad8daa1c1f20bd55c3e35c28b46ee46) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_less_trq.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::OpState](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_op_state.html) |
|  | This structure contains arguments for the [OpState](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba90c3fc693a5277bbb66630a5d61bab55) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_op_state.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::PosSET](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_pos_s_e_t.html) |
|  | This structure contains arguments for the [PosSET](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937baef9b32afb2093d9e96b67fd6d7761a4b) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_pos_s_e_t.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::DelayedPosSET](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_delayed_pos_s_e_t.html) |
|  | This structure contains arguments for the [DelayedPosSET](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba411c94871e83f4cb75b027da2018dbc1) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_delayed_pos_s_e_t.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::CommandDistributedEnd](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_command_distributed_end.html) |
|  | This structure contains arguments for the [CommandDistributedEnd](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba1179923d7367553b23d1be266bf1d034) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_command_distributed_end.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::RemainingTime](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_remaining_time.html) |
|  | This structure contains arguments for the [RemainingTime](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba6d98b4ec267acd26c88913ff1c4ed933) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_remaining_time.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::RemainingDistance](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_remaining_distance.html) |
|  | This structure contains arguments for the [RemainingDistance](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba1e15f75157d369a00339df83d8755b18) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_remaining_distance.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::CompletedTime](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_completed_time.html) |
|  | This structure contains arguments for the [CompletedTime](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba2bbe1542a19bb1f21701568ac8c8ee6c) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_completed_time.html#details) |
|  | |
| struct | [EventControl::Event::InputFunctionArguments::CompletedDistance](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_completed_distance.html) |
|  | This structure contains arguments for the [CompletedDistance](classwmx3_api_1_1_event_control_1_1_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba08dadca5a9f905205baf89e6d9e0cc46) input function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_input_function_arguments_1_1_completed_distance.html#details) |
|  | |
| union | [EventControl::Event::OutputFunctionArguments](unionwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments.html) |
|  | This union defines the structs containing arguments for each output function type. [More...](unionwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments.html#details) |
|  | |
| struct | [EventControl::Event::OutputFunctionArguments::None](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_none.html) |
|  | This structure contains arguments for the [None](classwmx3_api_1_1_event_control_1_1_event_output_function.html#adf1f3edb9115acb0a1e04209b7a9937bac9d3e887722f2bc482bcca9d41c512af) output function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_none.html#details) |
|  | |
| struct | [EventControl::Event::OutputFunctionArguments::SetIOOutBit](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_set_i_o_out_bit.html) |
|  | This structure contains arguments for the [SetIOOutBit](classwmx3_api_1_1_event_control_1_1_event_output_function.html#adf1f3edb9115acb0a1e04209b7a9937ba38bfd384d3b42e08b1d69d5c1767cd07) output function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_set_i_o_out_bit.html#details) |
|  | |
| struct | [EventControl::Event::OutputFunctionArguments::SetMBit](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_set_m_bit.html) |
|  | This structure contains arguments for the [SetMBit](classwmx3_api_1_1_event_control_1_1_event_output_function.html#adf1f3edb9115acb0a1e04209b7a9937baeaba287217a5f31de56e6bed50cf5e24) output function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_set_m_bit.html#details) |
|  | |
| struct | [EventControl::Event::OutputFunctionArguments::EnableAnotherEvent](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_enable_another_event.html) |
|  | This structure contains arguments for the [EnableAnotherEvent](classwmx3_api_1_1_event_control_1_1_event_output_function.html#adf1f3edb9115acb0a1e04209b7a9937baf072e7339a53c9ecc88921a995497ad2) output function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_enable_another_event.html#details) |
|  | |
| struct | [EventControl::Event::OutputFunctionArguments::StopSingleAxis](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_stop_single_axis.html) |
|  | This structure contains arguments for the [StopSingleAxis](classwmx3_api_1_1_event_control_1_1_event_output_function.html#adf1f3edb9115acb0a1e04209b7a9937ba098a1aa6b576f16a4016ccc4d51a12bd) output function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_stop_single_axis.html#details) |
|  | |
| struct | [EventControl::Event::OutputFunctionArguments::StartSinglePos](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_start_single_pos.html) |
|  | This structure contains arguments for the [StartSinglePos](classwmx3_api_1_1_event_control_1_1_event_output_function.html#adf1f3edb9115acb0a1e04209b7a9937ba75175f60bff0c6df77c3478c44c7f52f) output function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_start_single_pos.html#details) |
|  | |
| struct | [EventControl::Event::OutputFunctionArguments::StartSingleMov](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_start_single_mov.html) |
|  | This structure contains arguments for the [StartSingleMov](classwmx3_api_1_1_event_control_1_1_event_output_function.html#adf1f3edb9115acb0a1e04209b7a9937bac2a14e0c5efd52edc86f2d27b6429425) output function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_start_single_mov.html#details) |
|  | |
| struct | [EventControl::Event::OutputFunctionArguments::StartMultiplePos](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_start_multiple_pos.html) |
|  | This structure contains arguments for the [StartMultiplePos](classwmx3_api_1_1_event_control_1_1_event_output_function.html#adf1f3edb9115acb0a1e04209b7a9937ba1261779a698bdf10d88e5e45d66cad87) output function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_start_multiple_pos.html#details) |
|  | |
| struct | [EventControl::Event::OutputFunctionArguments::StartMultipleMov](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_start_multiple_mov.html) |
|  | This structure contains arguments for the [StartMultipleMov](classwmx3_api_1_1_event_control_1_1_event_output_function.html#adf1f3edb9115acb0a1e04209b7a9937bad36a9a1c4ec8e3bc45fc13a66ecdb215) output function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_start_multiple_mov.html#details) |
|  | |
| struct | [EventControl::Event::OutputFunctionArguments::LinearIntplPos](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_linear_intpl_pos.html) |
|  | This structure contains arguments for the [LinearIntplPos](classwmx3_api_1_1_event_control_1_1_event_output_function.html#adf1f3edb9115acb0a1e04209b7a9937ba9ecb85308f580ea2185e6a4924e1d996) output function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_linear_intpl_pos.html#details) |
|  | |
| struct | [EventControl::Event::OutputFunctionArguments::LinearIntplMov](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_linear_intpl_mov.html) |
|  | This structure contains arguments for the [LinearIntplMov](classwmx3_api_1_1_event_control_1_1_event_output_function.html#adf1f3edb9115acb0a1e04209b7a9937ba86d6f1841b30d73755ddacf379a01ca0) output function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_linear_intpl_mov.html#details) |
|  | |
| struct | [EventControl::Event::OutputFunctionArguments::StartAPIBuffer](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_start_a_p_i_buffer.html) |
|  | This structure contains arguments for the [StartAPIBuffer](classwmx3_api_1_1_event_control_1_1_event_output_function.html#adf1f3edb9115acb0a1e04209b7a9937ba1950aa875aa7bd72984a205756d3df22) output function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_start_a_p_i_buffer.html#details) |
|  | |
| struct | [EventControl::Event::OutputFunctionArguments::ExecQuickStopSingleAxis](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_exec_quick_stop_single_axis.html) |
|  | This structure contains arguments for the [ExecQuickStopSingleAxis](classwmx3_api_1_1_event_control_1_1_event_output_function.html#adf1f3edb9115acb0a1e04209b7a9937ba4b301f3ca674754f6faa98f5f3e55e4f) output function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_exec_quick_stop_single_axis.html#details) |
|  | |
| struct | [EventControl::Event::OutputFunctionArguments::OverrideVelSingleAxis](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_override_vel_single_axis.html) |
|  | This structure contains arguments for the [OverrideVelSingleAxis](classwmx3_api_1_1_event_control_1_1_event_output_function.html#adf1f3edb9115acb0a1e04209b7a9937ba861e30d6140e0c445e1474d327cfd470) output function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_override_vel_single_axis.html#details) |
|  | |
| struct | [EventControl::Event::OutputFunctionArguments::ExecEStop](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_exec_e_stop.html) |
|  | This structure contains arguments for the [ExecEStop](classwmx3_api_1_1_event_control_1_1_event_output_function.html#adf1f3edb9115acb0a1e04209b7a9937ba05cecfa312d63da0e710f9d3dd45e94d) output function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_exec_e_stop.html#details) |
|  | |
| struct | [EventControl::Event::OutputFunctionArguments::TriggerFlightRecorder](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_trigger_flight_recorder.html) |
|  | This structure contains arguments for the [TriggerFlightRecorder](classwmx3_api_1_1_event_control_1_1_event_output_function.html#adf1f3edb9115acb0a1e04209b7a9937bacbc0b53bc0493d341e05f5864d6f8349) output function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_trigger_flight_recorder.html#details) |
|  | |
| struct | [EventControl::Event::OutputFunctionArguments::ResetFlightRecorder](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_reset_flight_recorder.html) |
|  | This structure contains arguments for the [ResetFlightRecorder](classwmx3_api_1_1_event_control_1_1_event_output_function.html#adf1f3edb9115acb0a1e04209b7a9937ba93b012037961793949c4dd5fb323f641) output function type. [More...](structwmx3_api_1_1_event_control_1_1_event_1_1_output_function_arguments_1_1_reset_flight_recorder.html#details) |
|  | |
| class | [EventControl::TouchProbeSource](classwmx3_api_1_1_event_control_1_1_touch_probe_source.html) |
|  | This enumerator class contains the source for a touch probe. [More...](classwmx3_api_1_1_event_control_1_1_touch_probe_source.html#details) |
|  | |
| class | [EventControl::TouchProbeMode](classwmx3_api_1_1_event_control_1_1_touch_probe_mode.html) |
|  | This enumerator class contains the operation mode of a touch probe. [More...](classwmx3_api_1_1_event_control_1_1_touch_probe_mode.html#details) |
|  | |
| class | [EventControl::HardwareTouchProbeStatus](classwmx3_api_1_1_event_control_1_1_hardware_touch_probe_status.html) |
|  | This class contains the status of a hardware touch probe channel. [More...](classwmx3_api_1_1_event_control_1_1_hardware_touch_probe_status.html#details) |
|  | |
| class | [EventControl::PSOOutputType](classwmx3_api_1_1_event_control_1_1_p_s_o_output_type.html) |
|  | This enumerator class contains the type of output for position synchronous output. [More...](classwmx3_api_1_1_event_control_1_1_p_s_o_output_type.html#details) |
|  | |
| class | [EventControl::PSOOutput](classwmx3_api_1_1_event_control_1_1_p_s_o_output.html) |
|  | This class describes the output for position synchronous output. [More...](classwmx3_api_1_1_event_control_1_1_p_s_o_output.html#details) |
|  | |
| class | [EventControl::PSOStatus](classwmx3_api_1_1_event_control_1_1_p_s_o_status.html) |
|  | This class contains the current status of a position synchronous output channel. [More...](classwmx3_api_1_1_event_control_1_1_p_s_o_status.html#details) |
|  | |
| class | [EventControl::PSOOption](classwmx3_api_1_1_event_control_1_1_p_s_o_option.html) |
|  | This class contains options for a position synchronous output channel. [More...](classwmx3_api_1_1_event_control_1_1_p_s_o_option.html#details) |
|  | |
| class | [EventControl::ComparatorSourceType](classwmx3_api_1_1_event_control_1_1_comparator_source_type.html) |
|  | This enumerator class enumerates the sources for comparisons. [More...](classwmx3_api_1_1_event_control_1_1_comparator_source_type.html#details) |
|  | |
| class | [EventControl::ComparatorSource](classwmx3_api_1_1_event_control_1_1_comparator_source.html) |
|  | This class contains data to perform a comparison. [More...](classwmx3_api_1_1_event_control_1_1_comparator_source.html#details) |
|  | |
| class | [EventControl::PlannedVelocityData](classwmx3_api_1_1_event_control_1_1_planned_velocity_data.html) |
|  | This class contains a planned velocity override data point. [More...](classwmx3_api_1_1_event_control_1_1_planned_velocity_data.html#details) |
|  | |
| class | [EventControl::PlannedVelocityStatus](classwmx3_api_1_1_event_control_1_1_planned_velocity_status.html) |
|  | This class contains the current status of a planned velocity override channel. [More...](classwmx3_api_1_1_event_control_1_1_planned_velocity_status.html#details) |
|  | |
| class | [EventControl::ComparisonType](classwmx3_api_1_1_event_control_1_1_comparison_type.html) |
|  | This enumerator class enumerates types of comparisons. Comparisons are used to define conditions for certain functions. [More...](classwmx3_api_1_1_event_control_1_1_comparison_type.html#details) |
|  | |

| Variables | |
| --- | --- |
| static const int | [maxEvents](namespacewmx3_api_1_1constants.html#ae4164f312fb006f4fc762ea42ee54065) = 512 |
|  | The maximum number of events that may be defined (also see [Event Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__e_v_e_n_t.html)). |
|  | |
| static const int | [maxBitArray](namespacewmx3_api_1_1constants.html#a59ff8e25059b92dece898b480791f98f) = 1024 |
|  | The maximum byte size of the bit array used for event execution (also see [Event Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__e_v_e_n_t.html)). |
|  | |
| static const int | [maxHardwareTouchProbeLatchedValues](namespacewmx3_api_1_1constants.html#a3b38dadda696bcca4ac38f9bac14b554) = 256 |
|  | The maximum number of latched values per hardware touch probe (also see [Event Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__e_v_e_n_t.html)). |
|  | |
| static const int | [maxTouchprobeChannel](namespacewmx3_api_1_1constants.html#ac4fcf064e84b8422400be5f636690d96) = 64 |
|  | The maximum number of software touch probe channels (also see [Event Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__e_v_e_n_t.html)). |
|  | |
| static const int | [maxPsoChannel](namespacewmx3_api_1_1constants.html#af3afbc4b21fdf520c99f9145b114a73d) = 64 |
|  | The maximum number of position synchronous output channels (also see [Event Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__e_v_e_n_t.html)). |
|  | |
| static const int | [maxPsoData](namespacewmx3_api_1_1constants.html#aadc1fec3e75c16e3043985c6411d7d67) = 128 |
|  | The maximum number of position synchronous output data points per channel (also see [Event Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__e_v_e_n_t.html)). |
|  | |
| static const int | [maxPsoIoEncSize](namespacewmx3_api_1_1constants.html#a6de5963b659f756be624209783210c81) = 4 |
|  | The maximum number of bytes in the I/O encoder for positional synchronous output (also see [Event Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__e_v_e_n_t.html)). |
|  | |
| static const int | [maxPveloChannel](namespacewmx3_api_1_1constants.html#a01c534fb0fd9b590577de7ffa3f118ae) = 64 |
|  | The maximum number of planned velocity override channels (also see [Event Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__e_v_e_n_t.html)). |
|  | |
| static const int | [maxPveloData](namespacewmx3_api_1_1constants.html#ac66aca600b8c52b4a443b3b8bdb73c3b) = 20 |
|  | The maximum number of planned velocity override data points per channel (also see [Event Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__e_v_e_n_t.html)). |
|  | |
| static const int | [maxPveloIoEncSize](namespacewmx3_api_1_1constants.html#a9e9c2d8bd423a2deee6d77fe80f875cf) = 4 |
|  | The maximum number of bytes in the I/O encoder for planned velocity override (also see [Event Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__e_v_e_n_t.html)). |
|  | |
| static const int | [maxEventInputDataSize](namespacewmx3_api_1_1constants.html#a13fd315a3812a254b6e44b9356861dc7) = 8192 |
|  | The maximum size of the input data for an event in bytes (also see [Event Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__e_v_e_n_t.html)). |
|  | |
| static const int | [maxEventOutputDataSize](namespacewmx3_api_1_1constants.html#ae3834eb04c4346f3c336914957ba40c8) = 8192 |
|  | The maximum size of the output data for an event in bytes (also see [Event Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__e_v_e_n_t.html)). |
|  | |
| static const int | [maxEventConfigureOfModuleDataSize](namespacewmx3_api_1_1constants.html#a3f698cc20d3f82aa656a3a645c44ed8d) = 8192 |
|  | Reserved (also see [Event Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__e_v_e_n_t.html)). |
|  | |




* [common](dir_bdd9a5d540de89e9fe90efdfc6973a4f.html)
* [include](dir_11fbc4217d50ab21044e5ad6614aede5.html)
* [EventApi.h](_event_api_8h.html)



