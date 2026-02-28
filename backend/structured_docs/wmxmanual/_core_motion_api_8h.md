




WMX3 User Manual: CoreMotionApi.h File Reference










| Logo | WMX3 User Manual  3.6u1 |
| --- | --- |







[Classes](#nested-classes) |
[Variables](#var-members) 
CoreMotionApi.h File Reference 

| Classes | |
| --- | --- |
| class | [CoreMotionErrorCode](classwmx3_api_1_1_core_motion_error_code.html) |
|  | This enumerator class enumerates the WMX3 core motion library error codes. [More...](classwmx3_api_1_1_core_motion_error_code.html#details) |
|  | |
| class | [CoreMotionAxisLogInput](classwmx3_api_1_1_core_motion_axis_log_input.html) |
|  | This class contains the types of log data that may be collected for each axis by the CoreMotion module. [More...](classwmx3_api_1_1_core_motion_axis_log_input.html#details) |
|  | |
| class | [CoreMotionLogInput](classwmx3_api_1_1_core_motion_log_input.html) |
|  | This class specifies the log data to be collected by the CoreMotion module. [More...](classwmx3_api_1_1_core_motion_log_input.html#details) |
|  | |
| class | [CoreMotionAxisLogOutput](classwmx3_api_1_1_core_motion_axis_log_output.html) |
|  | This class contains data of the CoreMotion module that has been logged using the memory log operation. This class contains data for one cycle. [More...](classwmx3_api_1_1_core_motion_axis_log_output.html#details) |
|  | |
| class | [CoreMotionLogOutput](classwmx3_api_1_1_core_motion_log_output.html) |
|  | This class contains data of the CoreMotion module that has been logged using the memory log operation. This class contains data over multiple cycles. [More...](classwmx3_api_1_1_core_motion_log_output.html#details) |
|  | |
| class | [CoreMotionEventInput](classwmx3_api_1_1_core_motion_event_input.html) |
|  | This class defines event input functions that can be processed by the CoreMotion module. Also see [Core Motion Inputs](_w_m_x_d_o_c__f_u_n_c__e_v_t__i_n_p_u_t__c_o_r_e_m_o_t_i_o_n.html). [More...](classwmx3_api_1_1_core_motion_event_input.html#details) |
|  | |
| union | [CoreMotionEventInput::InputFunctionArguments](unionwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments.html) |
|  | This union defines the structs containing arguments for each input function. [More...](unionwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments.html#details) |
|  | |
| struct | [CoreMotionEventInput::InputFunctionArguments::EqualPos](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_equal_pos.html) |
|  | This structure contains arguments for the [EqualPos](classwmx3_api_1_1_core_motion_event_input.html#a23f807ff799eb5f8dcd4d8e8c048e463aa74e965750aea4a17887734138db9f72) input function. [More...](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_equal_pos.html#details) |
|  | |
| struct | [CoreMotionEventInput::InputFunctionArguments::GreaterPos](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_greater_pos.html) |
|  | This structure contains arguments for the [GreaterPos](classwmx3_api_1_1_core_motion_event_input.html#a23f807ff799eb5f8dcd4d8e8c048e463ad173a0feea690d3d9ff83bca77091d48) input function. [More...](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_greater_pos.html#details) |
|  | |
| struct | [CoreMotionEventInput::InputFunctionArguments::LessPos](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_less_pos.html) |
|  | This structure contains arguments for the [LessPos](classwmx3_api_1_1_core_motion_event_input.html#a23f807ff799eb5f8dcd4d8e8c048e463aa6ec394263a51fb5805253067461ef7c) input function. [More...](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_less_pos.html#details) |
|  | |
| struct | [CoreMotionEventInput::InputFunctionArguments::EqualVelocity](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_equal_velocity.html) |
|  | This structure contains arguments for the [EqualVelocity](classwmx3_api_1_1_core_motion_event_input.html#a23f807ff799eb5f8dcd4d8e8c048e463a333986b493ef74a2fb4427ea432fc7d7) input function. [More...](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_equal_velocity.html#details) |
|  | |
| struct | [CoreMotionEventInput::InputFunctionArguments::GreaterVelocity](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_greater_velocity.html) |
|  | This structure contains arguments for the [GreaterVelocity](classwmx3_api_1_1_core_motion_event_input.html#a23f807ff799eb5f8dcd4d8e8c048e463a0a48cf3780ada331be8dede39292293e) input function. [More...](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_greater_velocity.html#details) |
|  | |
| struct | [CoreMotionEventInput::InputFunctionArguments::LessVelocity](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_less_velocity.html) |
|  | This structure contains arguments for the [LessVelocity](classwmx3_api_1_1_core_motion_event_input.html#a23f807ff799eb5f8dcd4d8e8c048e463a85c0980027b4f6aeec9a726c242d1e7b) input function. [More...](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_less_velocity.html#details) |
|  | |
| struct | [CoreMotionEventInput::InputFunctionArguments::EqualTrq](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_equal_trq.html) |
|  | This structure contains arguments for the [EqualTrq](classwmx3_api_1_1_core_motion_event_input.html#a23f807ff799eb5f8dcd4d8e8c048e463a56ac11967b99ce392b579000835ad371) input function. [More...](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_equal_trq.html#details) |
|  | |
| struct | [CoreMotionEventInput::InputFunctionArguments::GreaterTrq](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_greater_trq.html) |
|  | This structure contains arguments for the [GreaterTrq](classwmx3_api_1_1_core_motion_event_input.html#a23f807ff799eb5f8dcd4d8e8c048e463a9bc04c8f39f9830cc93777c11248174d) input function. [More...](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_greater_trq.html#details) |
|  | |
| struct | [CoreMotionEventInput::InputFunctionArguments::LessTrq](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_less_trq.html) |
|  | This structure contains arguments for the [LessTrq](classwmx3_api_1_1_core_motion_event_input.html#a23f807ff799eb5f8dcd4d8e8c048e463abad8daa1c1f20bd55c3e35c28b46ee46) input function. [More...](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_less_trq.html#details) |
|  | |
| struct | [CoreMotionEventInput::InputFunctionArguments::OpState](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_op_state.html) |
|  | This structure contains arguments for the [OpState](classwmx3_api_1_1_core_motion_event_input.html#a23f807ff799eb5f8dcd4d8e8c048e463a90c3fc693a5277bbb66630a5d61bab55) input function. [More...](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_op_state.html#details) |
|  | |
| struct | [CoreMotionEventInput::InputFunctionArguments::AxisCmdMode](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_axis_cmd_mode.html) |
|  | This structure contains arguments for the [AxisCmdMode](classwmx3_api_1_1_core_motion_event_input.html#a23f807ff799eb5f8dcd4d8e8c048e463abe977921a327e2e7c6e0461ec8ab09ec) input function. [More...](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_axis_cmd_mode.html#details) |
|  | |
| struct | [CoreMotionEventInput::InputFunctionArguments::InPos](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_in_pos.html) |
|  | This structure contains arguments for the [InPos](classwmx3_api_1_1_core_motion_event_input.html#a23f807ff799eb5f8dcd4d8e8c048e463a2401e17ee947b291eca39634077a3cbd) input function. [More...](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_in_pos.html#details) |
|  | |
| struct | [CoreMotionEventInput::InputFunctionArguments::PosSET](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_pos_s_e_t.html) |
|  | This structure contains arguments for the [PosSET](classwmx3_api_1_1_core_motion_event_input.html#a23f807ff799eb5f8dcd4d8e8c048e463aef9b32afb2093d9e96b67fd6d7761a4b) input function. [More...](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_pos_s_e_t.html#details) |
|  | |
| struct | [CoreMotionEventInput::InputFunctionArguments::DelayedPosSET](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_delayed_pos_s_e_t.html) |
|  | This structure contains arguments for the [DelayedPosSET](classwmx3_api_1_1_core_motion_event_input.html#a23f807ff799eb5f8dcd4d8e8c048e463a411c94871e83f4cb75b027da2018dbc1) input function. [More...](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_delayed_pos_s_e_t.html#details) |
|  | |
| struct | [CoreMotionEventInput::InputFunctionArguments::CommandDistributedEnd](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_command_distributed_end.html) |
|  | This structure contains arguments for the [CommandDistributedEnd](classwmx3_api_1_1_core_motion_event_input.html#a23f807ff799eb5f8dcd4d8e8c048e463a1179923d7367553b23d1be266bf1d034) input function. [More...](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_command_distributed_end.html#details) |
|  | |
| struct | [CoreMotionEventInput::InputFunctionArguments::RemainingTime](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_remaining_time.html) |
|  | This structure contains arguments for the [RemainingTime](classwmx3_api_1_1_core_motion_event_input.html#a23f807ff799eb5f8dcd4d8e8c048e463a6d98b4ec267acd26c88913ff1c4ed933) input function. [More...](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_remaining_time.html#details) |
|  | |
| struct | [CoreMotionEventInput::InputFunctionArguments::RemainingDistance](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_remaining_distance.html) |
|  | This structure contains arguments for the [RemainingDistance](classwmx3_api_1_1_core_motion_event_input.html#a23f807ff799eb5f8dcd4d8e8c048e463a1e15f75157d369a00339df83d8755b18) input function. [More...](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_remaining_distance.html#details) |
|  | |
| struct | [CoreMotionEventInput::InputFunctionArguments::CompletedTime](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_completed_time.html) |
|  | This structure contains arguments for the [CompletedTime](classwmx3_api_1_1_core_motion_event_input.html#a23f807ff799eb5f8dcd4d8e8c048e463a2bbe1542a19bb1f21701568ac8c8ee6c) input function. [More...](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_completed_time.html#details) |
|  | |
| struct | [CoreMotionEventInput::InputFunctionArguments::CompletedDistance](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_completed_distance.html) |
|  | This structure contains arguments for the [CompletedDistance](classwmx3_api_1_1_core_motion_event_input.html#a23f807ff799eb5f8dcd4d8e8c048e463a08dadca5a9f905205baf89e6d9e0cc46) input function. [More...](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_completed_distance.html#details) |
|  | |
| struct | [CoreMotionEventInput::InputFunctionArguments::DistanceToTarget](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_distance_to_target.html) |
|  | This structure contains arguments for the [DistanceToTarget](classwmx3_api_1_1_core_motion_event_input.html#a23f807ff799eb5f8dcd4d8e8c048e463a918dda064a0ddaa8373a0ac648d8a7ee) input function. [More...](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_distance_to_target.html#details) |
|  | |
| struct | [CoreMotionEventInput::InputFunctionArguments::GreaterPositionError](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_greater_position_error.html) |
|  | This structure contains arguments for the [GreaterPositionError](classwmx3_api_1_1_core_motion_event_input.html#a23f807ff799eb5f8dcd4d8e8c048e463a23ea6ecfd4b868c614f898be23ad8acd) input function. [More...](structwmx3_api_1_1_core_motion_event_input_1_1_input_function_arguments_1_1_greater_position_error.html#details) |
|  | |
| class | [CoreMotionEventOutput](classwmx3_api_1_1_core_motion_event_output.html) |
|  | This class defines event output functions that can be processed by the CoreMotion module. Also see [Core Motion Outputs](_w_m_x_d_o_c__f_u_n_c__e_v_t__o_u_t_p_u_t__c_o_r_e_m_o_t_i_o_n.html). [More...](classwmx3_api_1_1_core_motion_event_output.html#details) |
|  | |
| union | [CoreMotionEventOutput::OutputFunctionArguments](unionwmx3_api_1_1_core_motion_event_output_1_1_output_function_arguments.html) |
|  | This union defines the structs containing arguments for each output function. [More...](unionwmx3_api_1_1_core_motion_event_output_1_1_output_function_arguments.html#details) |
|  | |
| struct | [CoreMotionEventOutput::OutputFunctionArguments::StopSingleAxis](structwmx3_api_1_1_core_motion_event_output_1_1_output_function_arguments_1_1_stop_single_axis.html) |
|  | This structure contains arguments for the [StopSingleAxis](classwmx3_api_1_1_core_motion_event_output.html#a08ca76fe67bbf6cbe849fde8d06df051a098a1aa6b576f16a4016ccc4d51a12bd) output function. [More...](structwmx3_api_1_1_core_motion_event_output_1_1_output_function_arguments_1_1_stop_single_axis.html#details) |
|  | |
| struct | [CoreMotionEventOutput::OutputFunctionArguments::StartSinglePos](structwmx3_api_1_1_core_motion_event_output_1_1_output_function_arguments_1_1_start_single_pos.html) |
|  | This structure contains arguments for the [StartSinglePos](classwmx3_api_1_1_core_motion_event_output.html#a08ca76fe67bbf6cbe849fde8d06df051a75175f60bff0c6df77c3478c44c7f52f) output function. [More...](structwmx3_api_1_1_core_motion_event_output_1_1_output_function_arguments_1_1_start_single_pos.html#details) |
|  | |
| struct | [CoreMotionEventOutput::OutputFunctionArguments::StartSingleMov](structwmx3_api_1_1_core_motion_event_output_1_1_output_function_arguments_1_1_start_single_mov.html) |
|  | This structure contains arguments for the [StartSingleMov](classwmx3_api_1_1_core_motion_event_output.html#a08ca76fe67bbf6cbe849fde8d06df051ac2a14e0c5efd52edc86f2d27b6429425) output function. [More...](structwmx3_api_1_1_core_motion_event_output_1_1_output_function_arguments_1_1_start_single_mov.html#details) |
|  | |
| struct | [CoreMotionEventOutput::OutputFunctionArguments::StartMultiplePos](structwmx3_api_1_1_core_motion_event_output_1_1_output_function_arguments_1_1_start_multiple_pos.html) |
|  | This structure contains arguments for the [StartMultiplePos](classwmx3_api_1_1_core_motion_event_output.html#a08ca76fe67bbf6cbe849fde8d06df051a1261779a698bdf10d88e5e45d66cad87) output function. [More...](structwmx3_api_1_1_core_motion_event_output_1_1_output_function_arguments_1_1_start_multiple_pos.html#details) |
|  | |
| struct | [CoreMotionEventOutput::OutputFunctionArguments::StartMultipleMov](structwmx3_api_1_1_core_motion_event_output_1_1_output_function_arguments_1_1_start_multiple_mov.html) |
|  | This structure contains arguments for the [StartMultipleMov](classwmx3_api_1_1_core_motion_event_output.html#a08ca76fe67bbf6cbe849fde8d06df051ad36a9a1c4ec8e3bc45fc13a66ecdb215) output function. [More...](structwmx3_api_1_1_core_motion_event_output_1_1_output_function_arguments_1_1_start_multiple_mov.html#details) |
|  | |
| struct | [CoreMotionEventOutput::OutputFunctionArguments::LinearIntplPos](structwmx3_api_1_1_core_motion_event_output_1_1_output_function_arguments_1_1_linear_intpl_pos.html) |
|  | This structure contains arguments for the [LinearIntplPos](classwmx3_api_1_1_core_motion_event_output.html#a08ca76fe67bbf6cbe849fde8d06df051a9ecb85308f580ea2185e6a4924e1d996) output function. [More...](structwmx3_api_1_1_core_motion_event_output_1_1_output_function_arguments_1_1_linear_intpl_pos.html#details) |
|  | |
| struct | [CoreMotionEventOutput::OutputFunctionArguments::LinearIntplMov](structwmx3_api_1_1_core_motion_event_output_1_1_output_function_arguments_1_1_linear_intpl_mov.html) |
|  | This structure contains arguments for the [LinearIntplMov](classwmx3_api_1_1_core_motion_event_output.html#a08ca76fe67bbf6cbe849fde8d06df051a86d6f1841b30d73755ddacf379a01ca0) output function. [More...](structwmx3_api_1_1_core_motion_event_output_1_1_output_function_arguments_1_1_linear_intpl_mov.html#details) |
|  | |
| struct | [CoreMotionEventOutput::OutputFunctionArguments::ExecQuickStopSingleAxis](structwmx3_api_1_1_core_motion_event_output_1_1_output_function_arguments_1_1_exec_quick_stop_single_axis.html) |
|  | This structure contains arguments for the [ExecQuickStopSingleAxis](classwmx3_api_1_1_core_motion_event_output.html#a08ca76fe67bbf6cbe849fde8d06df051a4b301f3ca674754f6faa98f5f3e55e4f) output function. [More...](structwmx3_api_1_1_core_motion_event_output_1_1_output_function_arguments_1_1_exec_quick_stop_single_axis.html#details) |
|  | |
| struct | [CoreMotionEventOutput::OutputFunctionArguments::OverrideVelSingleAxis](structwmx3_api_1_1_core_motion_event_output_1_1_output_function_arguments_1_1_override_vel_single_axis.html) |
|  | This structure contains arguments for the [OverrideVelSingleAxis](classwmx3_api_1_1_core_motion_event_output.html#a08ca76fe67bbf6cbe849fde8d06df051a861e30d6140e0c445e1474d327cfd470) output function. [More...](structwmx3_api_1_1_core_motion_event_output_1_1_output_function_arguments_1_1_override_vel_single_axis.html#details) |
|  | |
| struct | [CoreMotionEventOutput::OutputFunctionArguments::ExecEStop](structwmx3_api_1_1_core_motion_event_output_1_1_output_function_arguments_1_1_exec_e_stop.html) |
|  | This structure contains arguments for the [ExecEStop](classwmx3_api_1_1_core_motion_event_output.html#a08ca76fe67bbf6cbe849fde8d06df051a05cecfa312d63da0e710f9d3dd45e94d) output function. [More...](structwmx3_api_1_1_core_motion_event_output_1_1_output_function_arguments_1_1_exec_e_stop.html#details) |
|  | |
| struct | [CoreMotionEventOutput::OutputFunctionArguments::TriggerFlightRecorder](structwmx3_api_1_1_core_motion_event_output_1_1_output_function_arguments_1_1_trigger_flight_recorder.html) |
|  | This structure contains arguments for the [TriggerFlightRecorder](classwmx3_api_1_1_core_motion_event_output.html#a08ca76fe67bbf6cbe849fde8d06df051acbc0b53bc0493d341e05f5864d6f8349) output function. [More...](structwmx3_api_1_1_core_motion_event_output_1_1_output_function_arguments_1_1_trigger_flight_recorder.html#details) |
|  | |
| struct | [CoreMotionEventOutput::OutputFunctionArguments::ResetFlightRecorder](structwmx3_api_1_1_core_motion_event_output_1_1_output_function_arguments_1_1_reset_flight_recorder.html) |
|  | This structure contains arguments for the [ResetFlightRecorder](classwmx3_api_1_1_core_motion_event_output.html#a08ca76fe67bbf6cbe849fde8d06df051a93b012037961793949c4dd5fb323f641) output function. [More...](structwmx3_api_1_1_core_motion_event_output_1_1_output_function_arguments_1_1_reset_flight_recorder.html#details) |
|  | |
| class | [HomeState](classwmx3_api_1_1_home_state.html) |
|  | This enumerator class enumerates the homing states of axes executing homing. [More...](classwmx3_api_1_1_home_state.html#details) |
|  | |
| class | [HomeError](classwmx3_api_1_1_home_error.html) |
|  | This enumerator class enumerates the home errors encountered during homing. Also see [Home Error](_w_m_x_d_o_c__f_u_n_c__h_o_m__e_r_r_o_r.html). [More...](classwmx3_api_1_1_home_error.html#details) |
|  | |
| class | [AxisSyncMode](classwmx3_api_1_1_axis_sync_mode.html) |
|  | This enumerator class enumerates the sync control modes of an axis. [More...](classwmx3_api_1_1_axis_sync_mode.html#details) |
|  | |
| class | [AxisCompensation](classwmx3_api_1_1_axis_compensation.html) |
|  | This class describes the compensation values that are applied to an axis. [More...](classwmx3_api_1_1_axis_compensation.html#details) |
|  | |
| class | [AxisSupportedFunction](classwmx3_api_1_1_axis_supported_function.html) |
|  | This class describes the functions that are supported by an axis. [More...](classwmx3_api_1_1_axis_supported_function.html#details) |
|  | |
| class | [CoreMotionAxisStatus](classwmx3_api_1_1_core_motion_axis_status.html) |
|  | This class contains axis status data. See [Axis Status](_w_m_x_d_o_c__s_t_a_t_u_s__a_x_i_s.html) for a description of each status. [More...](classwmx3_api_1_1_core_motion_axis_status.html#details) |
|  | |
| class | [CoreMotionStatus](classwmx3_api_1_1_core_motion_status.html) |
|  | This class contains system status data. See [System Status](_w_m_x_d_o_c__s_t_a_t_u_s__s_y_s_t_e_m.html) for a description of each status. [More...](classwmx3_api_1_1_core_motion_status.html#details) |
|  | |
| class | [TriggerType](classwmx3_api_1_1_trigger_type.html) |
|  | This enumerator class enumerates the trigger types for triggered motion. [More...](classwmx3_api_1_1_trigger_type.html#details) |
|  | |
| class | [TriggerEventInputFunction](classwmx3_api_1_1_trigger_event_input_function.html) |
|  | This enumerator class enumerates the input functions (conditions) of trigger events. Also see [Input Functions](_w_m_x_d_o_c__f_u_n_c__t_r_g__e_v_e_n_t_s__i_n_p_u_t_f_u_n_c.html). [More...](classwmx3_api_1_1_trigger_event_input_function.html#details) |
|  | |
| class | [TriggerEventOutputFunction](classwmx3_api_1_1_trigger_event_output_function.html) |
|  | This enumerator class enumerates the output functions (actions) of trigger events. Also see [Output Functions](_w_m_x_d_o_c__f_u_n_c__t_r_g__e_v_e_n_t_s__o_u_t_p_u_t_f_u_n_c.html). [More...](classwmx3_api_1_1_trigger_event_output_function.html#details) |
|  | |
| class | [TriggerEvent](classwmx3_api_1_1_trigger_event.html) |
|  | This class describes an event used in trigger motion. [More...](classwmx3_api_1_1_trigger_event.html#details) |
|  | |
| union | [TriggerEvent::TriggerEventInputFunctionArguments](unionwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments.html) |
|  | This union defines the structs containing arguments for each input function type. [More...](unionwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::IOBit](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_i_o_bit.html) |
|  | This structure contains arguments for the [IOBit](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba270abbe54a7b48da979efa93ee0208c1) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_i_o_bit.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::NotIOBit](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_not_i_o_bit.html) |
|  | This structure contains arguments for the [NotIOBit](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba8ad6b0145c24b702bf380feb73b9f465) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_not_i_o_bit.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::OrIOBit](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_or_i_o_bit.html) |
|  | This structure contains arguments for the [OrIOBit](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937baf883071f860340d2d201f5339a1ff3c5) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_or_i_o_bit.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::AndIOBit](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_and_i_o_bit.html) |
|  | This structure contains arguments for the [AndIOBit](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba72ac88d695e943e684fa6fa72c209387) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_and_i_o_bit.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::XorIOBit](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_xor_i_o_bit.html) |
|  | This structure contains arguments for the [XorIOBit](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba528151ad8fcf3cbb9a1252ae258cdc16) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_xor_i_o_bit.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::NandIOBit](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_nand_i_o_bit.html) |
|  | This structure contains arguments for the [NandIOBit](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba9b04f9aedf0ba5c6b80fa1ad9e6da1d3) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_nand_i_o_bit.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::NorIOBit](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_nor_i_o_bit.html) |
|  | This structure contains arguments for the [NorIOBit](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba224456752f81f030a2aeacdcafc0e97c) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_nor_i_o_bit.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::XnorIOBit](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_xnor_i_o_bit.html) |
|  | This structure contains arguments for the [XnorIOBit](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba5d89f8ac0ee2eb803c7ce81402a59abb) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_xnor_i_o_bit.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::MBit](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_m_bit.html) |
|  | This structure contains arguments for the [MBit](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba0ab601084c8f52c8a333ecc5d4015a0b) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_m_bit.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::NotMBit](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_not_m_bit.html) |
|  | This structure contains arguments for the [NotMBit](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba7cbd13c1a3dddf5a967b518417215bb6) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_not_m_bit.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::OrMBit](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_or_m_bit.html) |
|  | This structure contains arguments for the [OrMBit](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba9e1a292bd218ff60a8c200a7fadb3b9e) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_or_m_bit.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::AndMBit](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_and_m_bit.html) |
|  | This structure contains arguments for the [AndMBit](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937badb86852930a110c737e88b8337cef27a) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_and_m_bit.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::XorMBit](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_xor_m_bit.html) |
|  | This structure contains arguments for the [XorMBit](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba2a1e17427bff1fa1565409e8e1766f50) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_xor_m_bit.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::NandMBit](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_nand_m_bit.html) |
|  | This structure contains arguments for the [NandMBit](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba4f110674dc04b7be5b000e6b908e3d9a) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_nand_m_bit.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::NorMBit](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_nor_m_bit.html) |
|  | This structure contains arguments for the [NorMBit](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937bacef6bdfa501c846bf3f3b752df0cedf1) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_nor_m_bit.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::XnorMBit](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_xnor_m_bit.html) |
|  | This structure contains arguments for the [XnorMBit](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937baa9be708909be138803ea54f31d387a0e) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_xnor_m_bit.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::Reg](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_reg.html) |
|  | This structure contains arguments for the [Reg](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937bafbf76e0af5b4d515f085475470a905d1) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_reg.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::NotReg](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_not_reg.html) |
|  | This structure contains arguments for the [NotReg](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba1c89172ddb1a3a2e8e7316b7f90e67d7) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_not_reg.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::OrReg](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_or_reg.html) |
|  | This structure contains arguments for the [OrReg](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba6dceb94310fc8d2e3687e9350e3882b9) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_or_reg.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::AndReg](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_and_reg.html) |
|  | This structure contains arguments for the [AndReg](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937baace884c4fac110529f06c62eac9aa4dc) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_and_reg.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::XorReg](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_xor_reg.html) |
|  | This structure contains arguments for the [XorReg](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937baa6e91c1155cc4cb1210760b43ec84981) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_xor_reg.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::NandReg](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_nand_reg.html) |
|  | This structure contains arguments for the [NandReg](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba8c4eacebb33caa1b1307074886ca4759) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_nand_reg.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::NorReg](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_nor_reg.html) |
|  | This structure contains arguments for the [NorReg](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba9311ee7f3e60dd739cd5091ca5273b09) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_nor_reg.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::XnorReg](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_xnor_reg.html) |
|  | This structure contains arguments for the [XnorReg](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba993a0714fc5093bf5b93bed5feee26f7) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_xnor_reg.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::EqualPos](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_equal_pos.html) |
|  | This structure contains arguments for the [EqualPos](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937baa74e965750aea4a17887734138db9f72) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_equal_pos.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::GreaterPos](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_greater_pos.html) |
|  | This structure contains arguments for the [GreaterPos](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937bad173a0feea690d3d9ff83bca77091d48) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_greater_pos.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::LessPos](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_less_pos.html) |
|  | This structure contains arguments for the [LessPos](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937baa6ec394263a51fb5805253067461ef7c) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_less_pos.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::EqualVelocity](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_equal_velocity.html) |
|  | This structure contains arguments for the [EqualVelocity](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba333986b493ef74a2fb4427ea432fc7d7) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_equal_velocity.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::GreaterVelocity](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_greater_velocity.html) |
|  | This structure contains arguments for the [GreaterVelocity](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba0a48cf3780ada331be8dede39292293e) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_greater_velocity.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::LessVelocity](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_less_velocity.html) |
|  | This structure contains arguments for the [LessVelocity](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba85c0980027b4f6aeec9a726c242d1e7b) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_less_velocity.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::EqualTrq](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_equal_trq.html) |
|  | This structure contains arguments for the [EqualTrq](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba56ac11967b99ce392b579000835ad371) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_equal_trq.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::GreaterTrq](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_greater_trq.html) |
|  | This structure contains arguments for the [GreaterTrq](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba9bc04c8f39f9830cc93777c11248174d) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_greater_trq.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::LessTrq](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_less_trq.html) |
|  | This structure contains arguments for the [LessTrq](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937babad8daa1c1f20bd55c3e35c28b46ee46) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_less_trq.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::RemainingTime](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_remaining_time.html) |
|  | This structure contains arguments for the [RemainingTime](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba6d98b4ec267acd26c88913ff1c4ed933) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_remaining_time.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::RemainingDistance](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_remaining_distance.html) |
|  | This structure contains arguments for the [RemainingDistance](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba1e15f75157d369a00339df83d8755b18) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_remaining_distance.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::SameTimeCompletion](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_same_time_completion.html) |
|  | This structure contains arguments for the [SameTimeCompletion](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba65bdad779518307b272778023ca62934) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_same_time_completion.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::CompletedTime](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_completed_time.html) |
|  | This structure contains arguments for the [CompletedTime](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba2bbe1542a19bb1f21701568ac8c8ee6c) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_completed_time.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::CompletedDistance](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_completed_distance.html) |
|  | This structure contains arguments for the [CompletedDistance](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba08dadca5a9f905205baf89e6d9e0cc46) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_completed_distance.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::StaggeredTimeCompletion](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_staggered_time_completion.html) |
|  | This structure contains arguments for the [StaggeredTimeCompletion](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937baed968d3231371cda04de7dd650cb0bb0) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_staggered_time_completion.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::StaggeredDistanceCompletion](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_staggered_distance_completion.html) |
|  | This structure contains arguments for the [StaggeredDistanceCompletion](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937bac1846af1bd9e2e66ba4a949f6f3d6f07) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_staggered_distance_completion.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::DistanceToTarget](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_distance_to_target.html) |
|  | This structure contains arguments for the [DistanceToTarget](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba918dda064a0ddaa8373a0ac648d8a7ee) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_distance_to_target.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::AxisIdle](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_axis_idle.html) |
|  | This structure contains arguments for the [AxisIdle](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba20ddc962ef9ee85c9c6f1a33fab8bee3) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_axis_idle.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventInputFunctionArguments::GreaterPositionError](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_greater_position_error.html) |
|  | This structure contains arguments for the [GreaterPositionError](classwmx3_api_1_1_trigger_event_input_function.html#adf1f3edb9115acb0a1e04209b7a9937ba23ea6ecfd4b868c614f898be23ad8acd) input function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_input_function_arguments_1_1_greater_position_error.html#details) |
|  | |
| union | [TriggerEvent::TriggerEventOutputFunctionArguments](unionwmx3_api_1_1_trigger_event_1_1_trigger_event_output_function_arguments.html) |
|  | This union defines the structs containing arguments for each output function type. [More...](unionwmx3_api_1_1_trigger_event_1_1_trigger_event_output_function_arguments.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventOutputFunctionArguments::TriggerMotion](structwmx3_api_1_1_trigger_event_1_1_trigger_event_output_function_arguments_1_1_trigger_motion.html) |
|  | This structure contains arguments for the [TriggerMotion](classwmx3_api_1_1_trigger_event_output_function.html#adf1f3edb9115acb0a1e04209b7a9937bac922c734dcb7e0b5d99fad03a3670a5c) output function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_output_function_arguments_1_1_trigger_motion.html#details) |
|  | |
| struct | [TriggerEvent::TriggerEventOutputFunctionArguments::SetReg](structwmx3_api_1_1_trigger_event_1_1_trigger_event_output_function_arguments_1_1_set_reg.html) |
|  | This structure contains arguments for the [SetReg](classwmx3_api_1_1_trigger_event_output_function.html#adf1f3edb9115acb0a1e04209b7a9937bae54497e099d40d2c8e7fea73edab0b0a) output function type. [More...](structwmx3_api_1_1_trigger_event_1_1_trigger_event_output_function_arguments_1_1_set_reg.html#details) |
|  | |
| class | [TriggerEvents](classwmx3_api_1_1_trigger_events.html) |
|  | This class contains a trigger consisting of multiple events that is used in trigger motion. [More...](classwmx3_api_1_1_trigger_events.html#details) |
|  | |
| class | [Trigger](classwmx3_api_1_1_trigger.html) |
|  | This class describes a basic trigger condition used for trigger motion. [More...](classwmx3_api_1_1_trigger.html#details) |
|  | |
| class | [AxisControl](classwmx3_api_1_1_axis_control.html) |
|  | **This class contains axis control functions.**  [More...](classwmx3_api_1_1_axis_control.html#details) |
|  | |
| class | [Config](classwmx3_api_1_1_config.html) |
|  | **This class contains configuration functions.**  [More...](classwmx3_api_1_1_config.html#details) |
|  | |
| class | [Config::VelocityMonitorSource](classwmx3_api_1_1_config_1_1_velocity_monitor_source.html) |
|  | This enumerator class specifies the source for the actual velocity status. [More...](classwmx3_api_1_1_config_1_1_velocity_monitor_source.html#details) |
|  | |
| class | [Config::FeedbackParam](classwmx3_api_1_1_config_1_1_feedback_param.html) |
|  | This class contains feedback parameters of an axis. See [Feedback Parameters](_w_m_x_d_o_c__p_a_r_a_m__f_e_e_d_b_a_c_k.html) for a description of each parameter. [More...](classwmx3_api_1_1_config_1_1_feedback_param.html#details) |
|  | |
| class | [Config::HomeDirection](classwmx3_api_1_1_config_1_1_home_direction.html) |
|  | This enumerator class enumerates the directions of homing. [More...](classwmx3_api_1_1_config_1_1_home_direction.html#details) |
|  | |
| class | [Config::HomeType](classwmx3_api_1_1_config_1_1_home_type.html) |
|  | This enumerator class enumerates the home types. The home type determines the method by which the axis searches for the home position. Also see [Homing](_w_m_x_d_o_c__f_u_n_c__h_o_m.html) for a more detailed description of each home type. [More...](classwmx3_api_1_1_config_1_1_home_type.html#details) |
|  | |
| class | [Config::HomeParam](classwmx3_api_1_1_config_1_1_home_param.html) |
|  | This class contains home parameters of an axis. See [Homing Parameters](_w_m_x_d_o_c__p_a_r_a_m__h_o_m_e.html) for a description of each parameter. [More...](classwmx3_api_1_1_config_1_1_home_param.html#details) |
|  | |
| class | [Config::LimitSwitchType](classwmx3_api_1_1_config_1_1_limit_switch_type.html) |
|  | This enumerator class enumerates the limit switch types. The limit switch type determines the action to take when the limit switch of an axis is triggered. [More...](classwmx3_api_1_1_config_1_1_limit_switch_type.html#details) |
|  | |
| class | [Config::LimitSwitchDirection](classwmx3_api_1_1_config_1_1_limit_switch_direction.html) |
|  | This enumerator class enumerates the limit switch directions. The limit switch direction indicates whether the limit switches are attached in the normal direction or the reverse direction. [More...](classwmx3_api_1_1_config_1_1_limit_switch_direction.html#details) |
|  | |
| class | [Config::LimitParam](classwmx3_api_1_1_config_1_1_limit_param.html) |
|  | This class contains limit parameters of an axis. See [Limit Parameters](_w_m_x_d_o_c__p_a_r_a_m__l_i_m_i_t.html) for a description of each parameter. [More...](classwmx3_api_1_1_config_1_1_limit_param.html#details) |
|  | |
| class | [Config::ProhibitOvertravelType](classwmx3_api_1_1_config_1_1_prohibit_overtravel_type.html) |
|  | This enumerator class enumerates the prohibit overtravel types. Depending on this parameter, profile parameters (such as velocity, deceleration, etc.) may be changed from the specified values to prevent overtravel beyond the target position. [More...](classwmx3_api_1_1_config_1_1_prohibit_overtravel_type.html#details) |
|  | |
| class | [Config::LinearIntplOverrideType](classwmx3_api_1_1_config_1_1_linear_intpl_override_type.html) |
|  | This enumerator class enumerates the linear interpolation override types. The linear interpolation override type determines the method by which a linear interpolation overrides another linear or circular interpolation. [More...](classwmx3_api_1_1_config_1_1_linear_intpl_override_type.html#details) |
|  | |
| class | [Config::LinearIntplProfileCalcMode](classwmx3_api_1_1_config_1_1_linear_intpl_profile_calc_mode.html) |
|  | This enumerator class enumerates the linear interpolation profile calculation modes. This parameter determines how the profile parameters (velocity, acceleration, etc.) for linear interpolation are calculated from the [maxVelocity](classwmx3_api_1_1_motion_1_1_linear_intpl_command.html#a447f9e0ed23818224aba299a3d29481c), [maxAcc](classwmx3_api_1_1_motion_1_1_linear_intpl_command.html#ae65d66f2dd9527ba97dfea9459b38bd6), [maxDec](classwmx3_api_1_1_motion_1_1_linear_intpl_command.html#a5dce78c6645ad0d7beb7ce2a21272444), [maxJerkAcc](classwmx3_api_1_1_motion_1_1_linear_intpl_command.html#a992660cd6fb56884f5c4c00cff50ee1f), and [maxJerkDec](classwmx3_api_1_1_motion_1_1_linear_intpl_command.html#a7b1aed34d76ee329a04fc4ba372764c9) specified for each interpolating axis. [More...](classwmx3_api_1_1_config_1_1_linear_intpl_profile_calc_mode.html#details) |
|  | |
| class | [Config::CircularIntplOverrideType](classwmx3_api_1_1_config_1_1_circular_intpl_override_type.html) |
|  | This enumerator class enumerates the circular interpolation override types. The circular interpolation override type determines the method by which a circular interpolation overrides another linear or circular interpolation. [More...](classwmx3_api_1_1_config_1_1_circular_intpl_override_type.html#details) |
|  | |
| class | [Config::MotionParam](classwmx3_api_1_1_config_1_1_motion_param.html) |
|  | This class contains motion parameters of an axis. See [Motion Parameters](_w_m_x_d_o_c__p_a_r_a_m__m_o_t_i_o_n.html) for a description of each parameter. [More...](classwmx3_api_1_1_config_1_1_motion_param.html#details) |
|  | |
| class | [Config::FollowingErrorAlarmType](classwmx3_api_1_1_config_1_1_following_error_alarm_type.html) |
|  | This enumerator class enumerates the actions to take when a following error alarm occurs (when the difference between the position command and feedback exceeds a set value). [More...](classwmx3_api_1_1_config_1_1_following_error_alarm_type.html#details) |
|  | |
| class | [Config::VelocityFollowingErrorAlarmType](classwmx3_api_1_1_config_1_1_velocity_following_error_alarm_type.html) |
|  | This enumerator class enumerates the actions to take when a velocity following error alarm occurs (when the difference between the velocity command and feedback exceeds a set value). [More...](classwmx3_api_1_1_config_1_1_velocity_following_error_alarm_type.html#details) |
|  | |
| class | [Config::AlarmParam](classwmx3_api_1_1_config_1_1_alarm_param.html) |
|  | This class contains alarm parameters of an axis. See [Alarm Parameters](_w_m_x_d_o_c__p_a_r_a_m__a_l_a_r_m.html) for a description of each parameter. [More...](classwmx3_api_1_1_config_1_1_alarm_param.html#details) |
|  | |
| class | [Config::SyncCompensationMode](classwmx3_api_1_1_config_1_1_sync_compensation_mode.html) |
|  | This enumerator class enumerates the sync compensation modes. The sync compensation mode determines any compensation to apply to improve the sync control between the master and slave axes. [More...](classwmx3_api_1_1_config_1_1_sync_compensation_mode.html#details) |
|  | |
| class | [Config::MasterDesyncType](classwmx3_api_1_1_config_1_1_master_desync_type.html) |
|  | This enumerator class enumerates the actions to take for the master axis when one of the slave axes becomes de-synchronized. [More...](classwmx3_api_1_1_config_1_1_master_desync_type.html#details) |
|  | |
| class | [Config::SlaveDesyncType](classwmx3_api_1_1_config_1_1_slave_desync_type.html) |
|  | This enumerator class enumerates the actions to take for the slave axis when the master axis becomes de-synchronized. [More...](classwmx3_api_1_1_config_1_1_slave_desync_type.html#details) |
|  | |
| class | [Config::SyncParam](classwmx3_api_1_1_config_1_1_sync_param.html) |
|  | This class contains sync parameters of an axis. See [Sync Parameters](_w_m_x_d_o_c__p_a_r_a_m__s_y_n_c.html) for a description of each parameter. [More...](classwmx3_api_1_1_config_1_1_sync_param.html#details) |
|  | |
| class | [Config::FlightRecorderParam](classwmx3_api_1_1_config_1_1_flight_recorder_param.html) |
|  | This class contains flight recorder parameters. See [Flight Recorder Parameters](_w_m_x_d_o_c__p_a_r_a_m__f_l_i_g_h_t__r_e_c_o_r_d_e_r.html) for a description of each parameter. [More...](classwmx3_api_1_1_config_1_1_flight_recorder_param.html#details) |
|  | |
| class | [Config::EStopSignalSource](classwmx3_api_1_1_config_1_1_e_stop_signal_source.html) |
|  | This enumerator class enumerates the sources of an emergency stop signal. [More...](classwmx3_api_1_1_config_1_1_e_stop_signal_source.html#details) |
|  | |
| class | [Config::EStopStatusSignalDestination](classwmx3_api_1_1_config_1_1_e_stop_status_signal_destination.html) |
|  | This enumerator class enumerates the destinations of an emergency stop status signal. [More...](classwmx3_api_1_1_config_1_1_e_stop_status_signal_destination.html#details) |
|  | |
| class | [Config::EStopLevel1Type](classwmx3_api_1_1_config_1_1_e_stop_level1_type.html) |
|  | This enumerator class enumerates the actions to take when a level 1 emergency stop is triggered. [More...](classwmx3_api_1_1_config_1_1_e_stop_level1_type.html#details) |
|  | |
| class | [Config::EmergencyStopParam](classwmx3_api_1_1_config_1_1_emergency_stop_param.html) |
|  | This class contains emergency stop parameters. See [Emergency Stop Parameters](_w_m_x_d_o_c__p_a_r_a_m__e_s_t_o_p.html) for a description of each parameter. [More...](classwmx3_api_1_1_config_1_1_emergency_stop_param.html#details) |
|  | |
| class | [Config::SystemParam](classwmx3_api_1_1_config_1_1_system_param.html) |
|  | This class contains system parameters for the entire system. See [Parameters](_w_m_x_d_o_c__p_a_r_a_m.html) for a description of each parameter. [More...](classwmx3_api_1_1_config_1_1_system_param.html#details) |
|  | |
| class | [Config::AxisParam](classwmx3_api_1_1_config_1_1_axis_param.html) |
|  | This class contains parameters specific to an axis. See [Axis Parameters](_w_m_x_d_o_c__p_a_r_a_m__a_x_i_s.html) for a description of each parameter. [More...](classwmx3_api_1_1_config_1_1_axis_param.html#details) |
|  | |
| class | [Sync](classwmx3_api_1_1_sync.html) |
|  | **This class contains sync functions.**  [More...](classwmx3_api_1_1_sync.html#details) |
|  | |
| class | [Sync::SyncOptions](classwmx3_api_1_1_sync_1_1_sync_options.html) |
|  | This class contains options for sync control. [More...](classwmx3_api_1_1_sync_1_1_sync_options.html#details) |
|  | |
| class | [Sync::SyncCombineOptions](classwmx3_api_1_1_sync_1_1_sync_combine_options.html) |
|  | This class contains options for combine sync control. [More...](classwmx3_api_1_1_sync_1_1_sync_combine_options.html#details) |
|  | |
| class | [Sync::SyncGroupStartupType](classwmx3_api_1_1_sync_1_1_sync_group_startup_type.html) |
|  | This enumerator class enumerates startup types for a sync group. [More...](classwmx3_api_1_1_sync_1_1_sync_group_startup_type.html#details) |
|  | |
| class | [Sync::SyncGroup](classwmx3_api_1_1_sync_1_1_sync_group.html) |
|  | This class contains settings for a sync group. [More...](classwmx3_api_1_1_sync_1_1_sync_group.html#details) |
|  | |
| class | [Sync::SyncGroupStatus](classwmx3_api_1_1_sync_1_1_sync_group_status.html) |
|  | This class contains the current status of a sync group channel. [More...](classwmx3_api_1_1_sync_1_1_sync_group_status.html#details) |
|  | |
| class | [Home](classwmx3_api_1_1_home.html) |
|  | **This class contains homing functions.**  [More...](classwmx3_api_1_1_home.html#details) |
|  | |
| class | [Home::AxisHomeData](classwmx3_api_1_1_home_1_1_axis_home_data.html) |
|  | This class contains homing related data for a single axis. [More...](classwmx3_api_1_1_home_1_1_axis_home_data.html#details) |
|  | |
| class | [Home::HomeData](classwmx3_api_1_1_home_1_1_home_data.html) |
|  | This class contains homing related data for all axes. [More...](classwmx3_api_1_1_home_1_1_home_data.html#details) |
|  | |
| class | [Velocity](classwmx3_api_1_1_velocity.html) |
|  | **This class contains velocity command functions.**  [More...](classwmx3_api_1_1_velocity.html#details) |
|  | |
| class | [Velocity::VelCommand](classwmx3_api_1_1_velocity_1_1_vel_command.html) |
|  | This class contains data for a velocity command. [More...](classwmx3_api_1_1_velocity_1_1_vel_command.html#details) |
|  | |
| class | [Velocity::TimedVelCommand](classwmx3_api_1_1_velocity_1_1_timed_vel_command.html) |
|  | This class contains data for a timed velocity command. [More...](classwmx3_api_1_1_velocity_1_1_timed_vel_command.html#details) |
|  | |
| class | [Velocity::TriggerVelCommand](classwmx3_api_1_1_velocity_1_1_trigger_vel_command.html) |
|  | This class contains data for a triggered velocity command. [More...](classwmx3_api_1_1_velocity_1_1_trigger_vel_command.html#details) |
|  | |
| class | [Velocity::TriggerTimedVelCommand](classwmx3_api_1_1_velocity_1_1_trigger_timed_vel_command.html) |
|  | This class contains data for a triggered timed velocity command. [More...](classwmx3_api_1_1_velocity_1_1_trigger_timed_vel_command.html#details) |
|  | |
| class | [Velocity::TimeCommand](classwmx3_api_1_1_velocity_1_1_time_command.html) |
|  | This class contains data for a time-based command. [More...](classwmx3_api_1_1_velocity_1_1_time_command.html#details) |
|  | |
| class | [Torque](classwmx3_api_1_1_torque.html) |
|  | **This class contains torque command functions.**  [More...](classwmx3_api_1_1_torque.html#details) |
|  | |
| class | [Torque::TrqCommand](classwmx3_api_1_1_torque_1_1_trq_command.html) |
|  | This class contains data for a torque command. [More...](classwmx3_api_1_1_torque_1_1_trq_command.html#details) |
|  | |
| class | [Torque::TriggerTrqCommand](classwmx3_api_1_1_torque_1_1_trigger_trq_command.html) |
|  | This class contains data for a triggered torque command. [More...](classwmx3_api_1_1_torque_1_1_trigger_trq_command.html#details) |
|  | |
| class | [Torque::RampTimeTrqCommand](classwmx3_api_1_1_torque_1_1_ramp_time_trq_command.html) |
|  | This class contains data for a ramp time torque command. [More...](classwmx3_api_1_1_torque_1_1_ramp_time_trq_command.html#details) |
|  | |
| class | [Torque::TriggerRampTimeTrqCommand](classwmx3_api_1_1_torque_1_1_trigger_ramp_time_trq_command.html) |
|  | This class contains data for a triggered ramp time torque command. [More...](classwmx3_api_1_1_torque_1_1_trigger_ramp_time_trq_command.html#details) |
|  | |
| class | [Torque::RampRateTrqCommand](classwmx3_api_1_1_torque_1_1_ramp_rate_trq_command.html) |
|  | This class contains data for a ramp rate torque command. [More...](classwmx3_api_1_1_torque_1_1_ramp_rate_trq_command.html#details) |
|  | |
| class | [Torque::TriggerRampRateTrqCommand](classwmx3_api_1_1_torque_1_1_trigger_ramp_rate_trq_command.html) |
|  | This class contains data for a triggered ramp rate torque command. [More...](classwmx3_api_1_1_torque_1_1_trigger_ramp_rate_trq_command.html#details) |
|  | |
| class | [Motion](classwmx3_api_1_1_motion.html) |
|  | **This class contains position command functions.**  [More...](classwmx3_api_1_1_motion.html#details) |
|  | |
| class | [Motion::PosCommand](classwmx3_api_1_1_motion_1_1_pos_command.html) |
|  | This class contains data for a position command. [More...](classwmx3_api_1_1_motion_1_1_pos_command.html#details) |
|  | |
| class | [Motion::TriggerPosCommand](classwmx3_api_1_1_motion_1_1_trigger_pos_command.html) |
|  | This class contains data for a triggered position command. [More...](classwmx3_api_1_1_motion_1_1_trigger_pos_command.html#details) |
|  | |
| class | [Motion::LinearIntplCommand](classwmx3_api_1_1_motion_1_1_linear_intpl_command.html) |
|  | This class contains data for a linear interpolation motion command. [More...](classwmx3_api_1_1_motion_1_1_linear_intpl_command.html#details) |
|  | |
| class | [Motion::CenterAndLengthCircularIntplCommand](classwmx3_api_1_1_motion_1_1_center_and_length_circular_intpl_command.html) |
|  | This class contains data for a circular interpolation motion command that is specified by the center position and arc length. [More...](classwmx3_api_1_1_motion_1_1_center_and_length_circular_intpl_command.html#details) |
|  | |
| class | [Motion::CenterAndEndCircularIntplCommand](classwmx3_api_1_1_motion_1_1_center_and_end_circular_intpl_command.html) |
|  | This class contains data for a circular interpolation motion command that is specified by the center and end positions. [More...](classwmx3_api_1_1_motion_1_1_center_and_end_circular_intpl_command.html#details) |
|  | |
| class | [Motion::ThroughAndEndCircularIntplCommand](classwmx3_api_1_1_motion_1_1_through_and_end_circular_intpl_command.html) |
|  | This class contains data for a circular interpolation motion command that is specified by the through and end positions. [More...](classwmx3_api_1_1_motion_1_1_through_and_end_circular_intpl_command.html#details) |
|  | |
| class | [Motion::LengthAndEndCircularIntplCommand](classwmx3_api_1_1_motion_1_1_length_and_end_circular_intpl_command.html) |
|  | This class contains data for a circular interpolation motion command that is specified by the end position and arc length. [More...](classwmx3_api_1_1_motion_1_1_length_and_end_circular_intpl_command.html#details) |
|  | |
| class | [Motion::RadiusAndEndCircularIntplCommand](classwmx3_api_1_1_motion_1_1_radius_and_end_circular_intpl_command.html) |
|  | This class contains data for a circular interpolation motion command that is specified by the end position and arc radius. [More...](classwmx3_api_1_1_motion_1_1_radius_and_end_circular_intpl_command.html#details) |
|  | |
| class | [Motion::ThroughAndEnd3DCircularIntplCommand](classwmx3_api_1_1_motion_1_1_through_and_end3_d_circular_intpl_command.html) |
|  | This class contains data for a three-dimensional circular interpolation motion command that is specified by the through and end positions. [More...](classwmx3_api_1_1_motion_1_1_through_and_end3_d_circular_intpl_command.html#details) |
|  | |
| class | [Motion::HelicalIntplProfileType](classwmx3_api_1_1_motion_1_1_helical_intpl_profile_type.html) |
|  | This enumerator class enumerates the types of ways to specify the profile for a helical interpolation. [More...](classwmx3_api_1_1_motion_1_1_helical_intpl_profile_type.html#details) |
|  | |
| class | [Motion::HelicalIntplCommand](classwmx3_api_1_1_motion_1_1_helical_intpl_command.html) |
|  | This class contains data for a helical interpolation motion command. A helical interpolation combines a circular interpolation with a linear interpolation so that the resulting motion is a three-dimensional helix. The helix is defined by the center position and arc length of the circular interpolation and the end position of the linear interpolation. The linear interpolation must be along only one axis, and the circular interpolation must be along two other axes. [More...](classwmx3_api_1_1_motion_1_1_helical_intpl_command.html#details) |
|  | |
| class | [Motion::JogCommand](classwmx3_api_1_1_motion_1_1_jog_command.html) |
|  | This class contains data for a jog command. [More...](classwmx3_api_1_1_motion_1_1_jog_command.html#details) |
|  | |
| class | [Motion::TimedJogCommand](classwmx3_api_1_1_motion_1_1_timed_jog_command.html) |
|  | This class contains data for a timed jog command. [More...](classwmx3_api_1_1_motion_1_1_timed_jog_command.html#details) |
|  | |
| class | [Motion::TriggerJogCommand](classwmx3_api_1_1_motion_1_1_trigger_jog_command.html) |
|  | This class contains data for a triggered jog command. [More...](classwmx3_api_1_1_motion_1_1_trigger_jog_command.html#details) |
|  | |
| class | [Motion::TriggerTimedJogCommand](classwmx3_api_1_1_motion_1_1_trigger_timed_jog_command.html) |
|  | This class contains data for a triggered timed jog command. [More...](classwmx3_api_1_1_motion_1_1_trigger_timed_jog_command.html#details) |
|  | |
| class | [Motion::PosToJogCommand](classwmx3_api_1_1_motion_1_1_pos_to_jog_command.html) |
|  | This class contains data for a position to jog command. [More...](classwmx3_api_1_1_motion_1_1_pos_to_jog_command.html#details) |
|  | |
| class | [Motion::StopCommand](classwmx3_api_1_1_motion_1_1_stop_command.html) |
|  | This class contains data for a stop command. [More...](classwmx3_api_1_1_motion_1_1_stop_command.html#details) |
|  | |
| class | [Motion::TimeCommand](classwmx3_api_1_1_motion_1_1_time_command.html) |
|  | This class contains data for a time-based command. [More...](classwmx3_api_1_1_motion_1_1_time_command.html#details) |
|  | |
| class | [Motion::SimulatePosCommand](classwmx3_api_1_1_motion_1_1_simulate_pos_command.html) |
|  | This class contains data for simulating a single axis position command. [More...](classwmx3_api_1_1_motion_1_1_simulate_pos_command.html#details) |
|  | |
| class | [Motion::SimulateLinearIntplCommand](classwmx3_api_1_1_motion_1_1_simulate_linear_intpl_command.html) |
|  | This class contains data for simulating a linear interpolation motion command. [More...](classwmx3_api_1_1_motion_1_1_simulate_linear_intpl_command.html#details) |
|  | |
| class | [Motion::WaitConditionType](classwmx3_api_1_1_motion_1_1_wait_condition_type.html) |
|  | This enumerator class enumerates the types of wait conditions. [More...](classwmx3_api_1_1_motion_1_1_wait_condition_type.html#details) |
|  | |
| class | [Motion::WaitCondition](classwmx3_api_1_1_motion_1_1_wait_condition.html) |
|  | This class describes a wait condition. [More...](classwmx3_api_1_1_motion_1_1_wait_condition.html#details) |
|  | |
| class | [Motion::PVTPoint](classwmx3_api_1_1_motion_1_1_p_v_t_point.html) |
|  | This class contains data for a PVT (Position-Velocity-Time) point. [More...](classwmx3_api_1_1_motion_1_1_p_v_t_point.html#details) |
|  | |
| class | [Motion::PVTCommand](classwmx3_api_1_1_motion_1_1_p_v_t_command.html) |
|  | This class contains data for a PVT (Position-Velocity-Time) command. [More...](classwmx3_api_1_1_motion_1_1_p_v_t_command.html#details) |
|  | |
| class | [Motion::PVTAdditionalCommand](classwmx3_api_1_1_motion_1_1_p_v_t_additional_command.html) |
|  | This class contains additional PVT (Position-Velocity-Time) point data. [More...](classwmx3_api_1_1_motion_1_1_p_v_t_additional_command.html#details) |
|  | |
| class | [Motion::PVTIntplCommand](classwmx3_api_1_1_motion_1_1_p_v_t_intpl_command.html) |
|  | This class contains data for a PVT (Position-Velocity-Time) interpolation command for multiple axes. [More...](classwmx3_api_1_1_motion_1_1_p_v_t_intpl_command.html#details) |
|  | |
| class | [Motion::PVTIntplAdditionalCommand](classwmx3_api_1_1_motion_1_1_p_v_t_intpl_additional_command.html) |
|  | This class contains data for additional PVT (Position-Velocity-Time) interpolation point data for multiple axes. [More...](classwmx3_api_1_1_motion_1_1_p_v_t_intpl_additional_command.html#details) |
|  | |
| class | [Motion::PTPoint](classwmx3_api_1_1_motion_1_1_p_t_point.html) |
|  | This class contains data for a PT (Position-Time) point. [More...](classwmx3_api_1_1_motion_1_1_p_t_point.html#details) |
|  | |
| class | [Motion::PTCommand](classwmx3_api_1_1_motion_1_1_p_t_command.html) |
|  | This class contains data for a PT (Position-Time) command. [More...](classwmx3_api_1_1_motion_1_1_p_t_command.html#details) |
|  | |
| class | [Motion::PTAdditionalCommand](classwmx3_api_1_1_motion_1_1_p_t_additional_command.html) |
|  | This class contains additional PT (Position-Time) point data. [More...](classwmx3_api_1_1_motion_1_1_p_t_additional_command.html#details) |
|  | |
| class | [Motion::VTPoint](classwmx3_api_1_1_motion_1_1_v_t_point.html) |
|  | This class contains data for a VT (Velocity-Time) point. [More...](classwmx3_api_1_1_motion_1_1_v_t_point.html#details) |
|  | |
| class | [Motion::VTCommand](classwmx3_api_1_1_motion_1_1_v_t_command.html) |
|  | This class contains data for a VT (Velocity-Time) command. [More...](classwmx3_api_1_1_motion_1_1_v_t_command.html#details) |
|  | |
| class | [Motion::VTAdditionalCommand](classwmx3_api_1_1_motion_1_1_v_t_additional_command.html) |
|  | This class contains additional VT (Velocity-Time) point data. [More...](classwmx3_api_1_1_motion_1_1_v_t_additional_command.html#details) |
|  | |
| class | [Motion::ATPoint](classwmx3_api_1_1_motion_1_1_a_t_point.html) |
|  | This class contains data for a AT (Acceleration-Time) point. [More...](classwmx3_api_1_1_motion_1_1_a_t_point.html#details) |
|  | |
| class | [Motion::ATCommand](classwmx3_api_1_1_motion_1_1_a_t_command.html) |
|  | This class contains data for a AT (Acceleration-Time) command. [More...](classwmx3_api_1_1_motion_1_1_a_t_command.html#details) |
|  | |
| class | [Motion::ATAdditionalCommand](classwmx3_api_1_1_motion_1_1_a_t_additional_command.html) |
|  | This class contains additional AT (Acceleration-Time) point data. [More...](classwmx3_api_1_1_motion_1_1_a_t_additional_command.html#details) |
|  | |
| class | [CoreMotion](classwmx3_api_1_1_core_motion.html) |
|  | **This class contains core motion functions.**  [More...](classwmx3_api_1_1_core_motion.html#details) |
|  | |

| Variables | |
| --- | --- |
| static const int | [maxFlightRecorderBufferSize](namespacewmx3_api_1_1constants.html#a3429df5dfb420e457c17f232a607d8b2) = 5000 |
|  | The maximum number of cycles of data in the flight recorder (also see [Core Motion Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__c_o_r_e_m_o_t_i_o_n.html)). |
|  | |
| static const int | [maxInPosChannel](namespacewmx3_api_1_1constants.html#a4e4ee1da1dbeb6a24dcf4eb062c6735c) = 5 |
|  | The maximum number of in position signals for each axis (also see [Core Motion Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__c_o_r_e_m_o_t_i_o_n.html)). |
|  | |
| static const int | [maxSyncGroup](namespacewmx3_api_1_1constants.html#a8ad307e0585800c6572e006e7d1eb285) = 64 |
|  | The maximum number of sync groups (also see [Core Motion Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__c_o_r_e_m_o_t_i_o_n.html)). |
|  | |
| static const int | [maxTriggerEvents](namespacewmx3_api_1_1constants.html#a69bb9998c555adc324bf7a7ca2f18d8f) = 8 |
|  | The maximum number of events per trigger motion that use trigger data (also see [Core Motion Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__c_o_r_e_m_o_t_i_o_n.html)). |
|  | |
| static const unsigned long long int | [maxProfileUnsignedInput](namespacewmx3_api_1_1constants.html#ac0a91dfa1015c7c6e5171e577138a987) = 274877906943ULL |
|  | The maximum input value for profile parameters such as velocity and acceleration (also see [Core Motion Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__c_o_r_e_m_o_t_i_o_n.html)). |
|  | |
| static const int | [maxPvtAppendPoints](namespacewmx3_api_1_1constants.html#abed8e080674ba0ad84562f5577d827ad) = 4096 |
|  | The maximum number of PVT points that may be appended to a PVT sequence with a single command (also see [Core Motion Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__c_o_r_e_m_o_t_i_o_n.html)). |
|  | |
| static const int | [maxPvtInterpolateAppendPoints](namespacewmx3_api_1_1constants.html#a54897d85e48262638854fe8996f01a07) = 2048 |
|  | The maximum number of PVT points that may be appended to a PVT interpolation sequence with a single command (also see [Core Motion Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__c_o_r_e_m_o_t_i_o_n.html)). |
|  | |
| static const int | [maxPvtInterpolateAxes](namespacewmx3_api_1_1constants.html#abf7f4061885ebb8c63e388f0ffceb20b) = 8 |
|  | The maximum number of axes that may be controlled by a PVT sequence (also see [Core Motion Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__c_o_r_e_m_o_t_i_o_n.html)). |
|  | |




* [common](dir_bdd9a5d540de89e9fe90efdfc6973a4f.html)
* [include](dir_11fbc4217d50ab21044e5ad6614aede5.html)
* [CoreMotionApi.h](_core_motion_api_8h.html)



