




WMX3 User Manual: ApiBufferApi.h File Reference










| Logo | WMX3 User Manual  3.6u1 |
| --- | --- |







[Classes](#nested-classes) |
[Variables](#var-members) 
ApiBufferApi.h File Reference 

| Classes | |
| --- | --- |
| class | [ApiBufferErrorCode](classwmx3_api_1_1_api_buffer_error_code.html) |
|  | This enumerator class enumerates the WMX3 API buffer library error codes. [More...](classwmx3_api_1_1_api_buffer_error_code.html#details) |
|  | |
| class | [ApiBufferConditionType](classwmx3_api_1_1_api_buffer_condition_type.html) |
|  | This enumerator class enumerates the condition types for flow conditions in the API buffer channel. Flow conditions can control the execution sequence of the API buffer. [More...](classwmx3_api_1_1_api_buffer_condition_type.html#details) |
|  | |
| class | [ApiBufferState](classwmx3_api_1_1_api_buffer_state.html) |
|  | This enumerator class enumerates the states of an API buffer channel. [More...](classwmx3_api_1_1_api_buffer_state.html#details) |
|  | |
| class | [ApiBufferCondition](classwmx3_api_1_1_api_buffer_condition.html) |
|  | This class contains a condition that is used to control the execution of an API buffer channel. [More...](classwmx3_api_1_1_api_buffer_condition.html#details) |
|  | |
| union | [ApiBufferCondition::ApiBufferConditionArguments](unionwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments.html) |
|  | This union defines the structs containing arguments for each API buffer condition type. [More...](unionwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments.html#details) |
|  | |
| struct | [ApiBufferCondition::ApiBufferConditionArguments::NeverTrue](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_never_true.html) |
|  | This structure contains arguments for the [NeverTrue](classwmx3_api_1_1_api_buffer_condition_type.html#adf1f3edb9115acb0a1e04209b7a9937badb8fd4d72b49911a5bfedc30d6c7f8f3) API buffer condition type. [More...](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_never_true.html#details) |
|  | |
| struct | [ApiBufferCondition::ApiBufferConditionArguments::AlwaysTrue](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_always_true.html) |
|  | This structure contains arguments for the [AlwaysTrue](classwmx3_api_1_1_api_buffer_condition_type.html#adf1f3edb9115acb0a1e04209b7a9937ba3af0b949af0d82cef0f51738c1068c60) API buffer condition type. [More...](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_always_true.html#details) |
|  | |
| struct | [ApiBufferCondition::ApiBufferConditionArguments::IOInput](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_i_o_input.html) |
|  | This structure contains arguments for the [IOInput](classwmx3_api_1_1_api_buffer_condition_type.html#adf1f3edb9115acb0a1e04209b7a9937ba1a397bd8242c450570d19c49d7e65ac4) API buffer condition type. [More...](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_i_o_input.html#details) |
|  | |
| struct | [ApiBufferCondition::ApiBufferConditionArguments::IOOutput](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_i_o_output.html) |
|  | This structure contains arguments for the [IOOutput](classwmx3_api_1_1_api_buffer_condition_type.html#adf1f3edb9115acb0a1e04209b7a9937ba99c3f863a5614eba616b1ad386aa748e) API buffer condition type. [More...](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_i_o_output.html#details) |
|  | |
| struct | [ApiBufferCondition::ApiBufferConditionArguments::UserMemory](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_user_memory.html) |
|  | This structure contains arguments for the [UserMemory](classwmx3_api_1_1_api_buffer_condition_type.html#adf1f3edb9115acb0a1e04209b7a9937bae14886444e89e61c321f852abcba9107) API buffer condition type. [More...](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_user_memory.html#details) |
|  | |
| struct | [ApiBufferCondition::ApiBufferConditionArguments::MinimumTrq](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_minimum_trq.html) |
|  | This structure contains arguments for the [MinimumTrq](classwmx3_api_1_1_api_buffer_condition_type.html#adf1f3edb9115acb0a1e04209b7a9937ba1eb857e9a7ac19a79a189d39918148a7) API buffer condition type. [More...](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_minimum_trq.html#details) |
|  | |
| struct | [ApiBufferCondition::ApiBufferConditionArguments::OpState](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_op_state.html) |
|  | This structure contains arguments for the [OpState](classwmx3_api_1_1_api_buffer_condition_type.html#adf1f3edb9115acb0a1e04209b7a9937ba90c3fc693a5277bbb66630a5d61bab55) API buffer condition type. [More...](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_op_state.html#details) |
|  | |
| struct | [ApiBufferCondition::ApiBufferConditionArguments::AxisCmdMode](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_axis_cmd_mode.html) |
|  | This structure contains arguments for the [AxisCmdMode](classwmx3_api_1_1_api_buffer_condition_type.html#adf1f3edb9115acb0a1e04209b7a9937babe977921a327e2e7c6e0461ec8ab09ec) API buffer condition type. [More...](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_axis_cmd_mode.html#details) |
|  | |
| struct | [ApiBufferCondition::ApiBufferConditionArguments::InPos](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_in_pos.html) |
|  | This structure contains arguments for the [InPos](classwmx3_api_1_1_api_buffer_condition_type.html#adf1f3edb9115acb0a1e04209b7a9937ba2401e17ee947b291eca39634077a3cbd) API buffer condition type. [More...](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_in_pos.html#details) |
|  | |
| struct | [ApiBufferCondition::ApiBufferConditionArguments::PosSET](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_pos_s_e_t.html) |
|  | This structure contains arguments for the [PosSET](classwmx3_api_1_1_api_buffer_condition_type.html#adf1f3edb9115acb0a1e04209b7a9937baef9b32afb2093d9e96b67fd6d7761a4b) API buffer condition type. [More...](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_pos_s_e_t.html#details) |
|  | |
| struct | [ApiBufferCondition::ApiBufferConditionArguments::DelayedPosSET](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_delayed_pos_s_e_t.html) |
|  | This structure contains arguments for the [DelayedPosSET](classwmx3_api_1_1_api_buffer_condition_type.html#adf1f3edb9115acb0a1e04209b7a9937ba411c94871e83f4cb75b027da2018dbc1) API buffer condition type. [More...](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_delayed_pos_s_e_t.html#details) |
|  | |
| struct | [ApiBufferCondition::ApiBufferConditionArguments::CommandDistributedEnd](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_command_distributed_end.html) |
|  | This structure contains arguments for the [CommandDistributedEnd](classwmx3_api_1_1_api_buffer_condition_type.html#adf1f3edb9115acb0a1e04209b7a9937ba1179923d7367553b23d1be266bf1d034) API buffer condition type. [More...](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_command_distributed_end.html#details) |
|  | |
| struct | [ApiBufferCondition::ApiBufferConditionArguments::RemainingTime](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_remaining_time.html) |
|  | This structure contains arguments for the [RemainingTime](classwmx3_api_1_1_api_buffer_condition_type.html#adf1f3edb9115acb0a1e04209b7a9937ba6d98b4ec267acd26c88913ff1c4ed933) API buffer condition type. [More...](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_remaining_time.html#details) |
|  | |
| struct | [ApiBufferCondition::ApiBufferConditionArguments::RemainingDistance](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_remaining_distance.html) |
|  | This structure contains arguments for the [RemainingDistance](classwmx3_api_1_1_api_buffer_condition_type.html#adf1f3edb9115acb0a1e04209b7a9937ba1e15f75157d369a00339df83d8755b18) API buffer condition type. [More...](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_remaining_distance.html#details) |
|  | |
| struct | [ApiBufferCondition::ApiBufferConditionArguments::CompletedTime](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_completed_time.html) |
|  | This structure contains arguments for the [CompletedTime](classwmx3_api_1_1_api_buffer_condition_type.html#adf1f3edb9115acb0a1e04209b7a9937ba2bbe1542a19bb1f21701568ac8c8ee6c) API buffer condition type. [More...](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_completed_time.html#details) |
|  | |
| struct | [ApiBufferCondition::ApiBufferConditionArguments::CompletedDistance](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_completed_distance.html) |
|  | This structure contains arguments for the [CompletedDistance](classwmx3_api_1_1_api_buffer_condition_type.html#adf1f3edb9115acb0a1e04209b7a9937ba08dadca5a9f905205baf89e6d9e0cc46) API buffer condition type. [More...](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_completed_distance.html#details) |
|  | |
| struct | [ApiBufferCondition::ApiBufferConditionArguments::DistanceToTarget](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_distance_to_target.html) |
|  | This structure contains arguments for the [DistanceToTarget](classwmx3_api_1_1_api_buffer_condition_type.html#adf1f3edb9115acb0a1e04209b7a9937ba918dda064a0ddaa8373a0ac648d8a7ee) API buffer condition type. [More...](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_distance_to_target.html#details) |
|  | |
| struct | [ApiBufferCondition::ApiBufferConditionArguments::DecelerationStarted](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_deceleration_started.html) |
|  | This structure contains arguments for the [DecelerationStarted](classwmx3_api_1_1_api_buffer_condition_type.html#adf1f3edb9115acb0a1e04209b7a9937ba3a2d921ff657ca04b902414e01654776) API buffer condition type. [More...](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_deceleration_started.html#details) |
|  | |
| struct | [ApiBufferCondition::ApiBufferConditionArguments::AxisIdle](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_axis_idle.html) |
|  | This structure contains arguments for the [AxisIdle](classwmx3_api_1_1_api_buffer_condition_type.html#adf1f3edb9115acb0a1e04209b7a9937ba20ddc962ef9ee85c9c6f1a33fab8bee3) API buffer condition type. [More...](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_axis_idle.html#details) |
|  | |
| struct | [ApiBufferCondition::ApiBufferConditionArguments::MotionStarted](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_motion_started.html) |
|  | This structure contains arguments for the [MotionStarted](classwmx3_api_1_1_api_buffer_condition_type.html#adf1f3edb9115acb0a1e04209b7a9937bae94d25c1c88ea7ec549a0fa441184b6f) API buffer condition type. [More...](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_motion_started.html#details) |
|  | |
| struct | [ApiBufferCondition::ApiBufferConditionArguments::MotionStartedOverrideReady](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_motion_started_override_ready.html) |
|  | This structure contains arguments for the [MotionStartedOverrideReady](classwmx3_api_1_1_api_buffer_condition_type.html#adf1f3edb9115acb0a1e04209b7a9937babd8193f0503e31289a6adc6243a084fc) API buffer condition type. [More...](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_motion_started_override_ready.html#details) |
|  | |
| struct | [ApiBufferCondition::ApiBufferConditionArguments::Event](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_event.html) |
|  | This structure contains arguments for the [Event](classwmx3_api_1_1_api_buffer_condition_type.html#adf1f3edb9115acb0a1e04209b7a9937ba179ea6039d06368199692ba093b79047) API buffer condition type. [More...](structwmx3_api_1_1_api_buffer_condition_1_1_api_buffer_condition_arguments_1_1_event.html#details) |
|  | |
| class | [ApiBufferErrorLog](classwmx3_api_1_1_api_buffer_error_log.html) |
|  | This class contains the log of an error encountered during the execution of an API buffer channel. [More...](classwmx3_api_1_1_api_buffer_error_log.html#details) |
|  | |
| class | [ApiBufferStatus](classwmx3_api_1_1_api_buffer_status.html) |
|  | This class contains the current status of an API buffer channnel. Also see [API Buffer Statuses](_w_m_x_d_o_c__f_u_n_c__a_p_b__a_d_v_a_n_c_e_d__s_t_a_t_u_s.html). [More...](classwmx3_api_1_1_api_buffer_status.html#details) |
|  | |
| class | [ApiBufferOptions](classwmx3_api_1_1_api_buffer_options.html) |
|  | This class contains options for an API buffer channel. Also see [API Buffer Options](_w_m_x_d_o_c__f_u_n_c__a_p_b__a_d_v_a_n_c_e_d__o_p_t_i_o_n.html). [More...](classwmx3_api_1_1_api_buffer_options.html#details) |
|  | |
| class | [ApiBufferWatch](classwmx3_api_1_1_api_buffer_watch.html) |
|  | This class contains watch options for an API buffer channel. [More...](classwmx3_api_1_1_api_buffer_watch.html#details) |
|  | |
| class | [ApiBufferChannelSelection](classwmx3_api_1_1_api_buffer_channel_selection.html) |
|  | This class contains a selection of API buffer channels. [More...](classwmx3_api_1_1_api_buffer_channel_selection.html#details) |
|  | |
| class | [ApiBufferEventOutput](classwmx3_api_1_1_api_buffer_event_output.html) |
|  | This class defines event output functions that can be processed by the ApiBuffer module. Also see [API Buffer Outputs](_w_m_x_d_o_c__f_u_n_c__e_v_t__o_u_t_p_u_t__a_p_i_b_u_f_f_e_r.html). [More...](classwmx3_api_1_1_api_buffer_event_output.html#details) |
|  | |
| union | [ApiBufferEventOutput::OutputFunctionArguments](unionwmx3_api_1_1_api_buffer_event_output_1_1_output_function_arguments.html) |
|  | This union defines the structs containing arguments for each output function. [More...](unionwmx3_api_1_1_api_buffer_event_output_1_1_output_function_arguments.html#details) |
|  | |
| struct | [ApiBufferEventOutput::OutputFunctionArguments::StartAPIBuffer](structwmx3_api_1_1_api_buffer_event_output_1_1_output_function_arguments_1_1_start_a_p_i_buffer.html) |
|  | This structure contains arguments for the [StartAPIBuffer](structwmx3_api_1_1_api_buffer_event_output_1_1_output_function_arguments_1_1_start_a_p_i_buffer.html) output function. [More...](structwmx3_api_1_1_api_buffer_event_output_1_1_output_function_arguments_1_1_start_a_p_i_buffer.html#details) |
|  | |
| struct | [ApiBufferEventOutput::OutputFunctionArguments::HaltAPIBuffer](structwmx3_api_1_1_api_buffer_event_output_1_1_output_function_arguments_1_1_halt_a_p_i_buffer.html) |
|  | This structure contains arguments for the [HaltAPIBuffer](structwmx3_api_1_1_api_buffer_event_output_1_1_output_function_arguments_1_1_halt_a_p_i_buffer.html) output function. [More...](structwmx3_api_1_1_api_buffer_event_output_1_1_output_function_arguments_1_1_halt_a_p_i_buffer.html#details) |
|  | |
| class | [ApiBuffer](classwmx3_api_1_1_api_buffer.html) |
|  | **This class contains API buffer functions.**  [More...](classwmx3_api_1_1_api_buffer.html#details) |
|  | |

| Variables | |
| --- | --- |
| static const int | [maxApiBufferChannel](namespacewmx3_api_1_1constants.html#a52d66ee07d993905cb563a54a99161c5) = 255 |
|  | The maximum number of API buffer channels (also see [API Buffer Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__a_p_i_b_u_f_f_e_r.html)). |
|  | |
| static const int | [maxApiBufferErrorLog](namespacewmx3_api_1_1constants.html#a5e026ed67a6e3c7636d735afd609264b) = 10 |
|  | The maximum number of errors logged in the API buffer log (also see [API Buffer Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__a_p_i_b_u_f_f_e_r.html)). |
|  | |
| static const int | [maxDefaultApiBufferSize](namespacewmx3_api_1_1constants.html#a98d2b941b907bfe90ec2f2f4f3e00f47) = 524288 |
|  | The maximum default size of an API buffer channel (also see [API Buffer Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__a_p_i_b_u_f_f_e_r.html)). |
|  | |




* [common](dir_bdd9a5d540de89e9fe90efdfc6973a4f.html)
* [include](dir_11fbc4217d50ab21044e5ad6614aede5.html)
* [ApiBufferApi.h](_api_buffer_api_8h.html)



