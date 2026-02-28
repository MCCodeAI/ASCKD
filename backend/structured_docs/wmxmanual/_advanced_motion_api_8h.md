




WMX3 User Manual: AdvancedMotionApi.h File Reference










| Logo | WMX3 User Manual  3.6u1 |
| --- | --- |







[Classes](#nested-classes) |
[Variables](#var-members) 
AdvancedMotionApi.h File Reference 

| Classes | |
| --- | --- |
| class | [AdvancedMotionErrorCode](classwmx3_api_1_1_advanced_motion_error_code.html) |
|  | This enumerator class enumerates the WMX3 advanced motion library error codes. [More...](classwmx3_api_1_1_advanced_motion_error_code.html#details) |
|  | |
| class | [AdvSync](classwmx3_api_1_1_adv_sync.html) |
|  | **This class contains advanced sync functions.**  [More...](classwmx3_api_1_1_adv_sync.html#details) |
|  | |
| class | [AdvSync::ECAMType](classwmx3_api_1_1_adv_sync_1_1_e_c_a_m_type.html) |
|  | This enumerator class enumerates the types of E-CAM, which determine certain characteristics of E-CAM. Also see [E-CAM](_w_m_x_d_o_c__f_u_n_c__e_c_m.html). [More...](classwmx3_api_1_1_adv_sync_1_1_e_c_a_m_type.html#details) |
|  | |
| class | [AdvSync::ECAMSourceType](classwmx3_api_1_1_adv_sync_1_1_e_c_a_m_source_type.html) |
|  | This enumerator class enumerates the sources of the E-CAM master input. [More...](classwmx3_api_1_1_adv_sync_1_1_e_c_a_m_source_type.html#details) |
|  | |
| class | [AdvSync::ECAMSourceOptions](classwmx3_api_1_1_adv_sync_1_1_e_c_a_m_source_options.html) |
|  | This class contains E-CAM source options. This determines the source of the master input that is used to calculate the slave command position from the E-CAM table. [More...](classwmx3_api_1_1_adv_sync_1_1_e_c_a_m_source_options.html#details) |
|  | |
| class | [AdvSync::ECAMClutchType](classwmx3_api_1_1_adv_sync_1_1_e_c_a_m_clutch_type.html) |
|  | This enumerator class enumerates the E-CAM clutch types. [More...](classwmx3_api_1_1_adv_sync_1_1_e_c_a_m_clutch_type.html#details) |
|  | |
| class | [AdvSync::ECAMClutchOptions](classwmx3_api_1_1_adv_sync_1_1_e_c_a_m_clutch_options.html) |
|  | This class contains E-CAM clutch options. The E-CAM clutch determines how the slave axis synchronizes with the master axis when E-CAM is started. [More...](classwmx3_api_1_1_adv_sync_1_1_e_c_a_m_clutch_options.html#details) |
|  | |
| class | [AdvSync::ECAMOptions](classwmx3_api_1_1_adv_sync_1_1_e_c_a_m_options.html) |
|  | This class contains E-CAM options, including the E-CAM clutch options. [More...](classwmx3_api_1_1_adv_sync_1_1_e_c_a_m_options.html#details) |
|  | |
| class | [AdvSync::ECAMData](classwmx3_api_1_1_adv_sync_1_1_e_c_a_m_data.html) |
|  | This class contains all settings for E-CAM control, including E-CAM table data. [More...](classwmx3_api_1_1_adv_sync_1_1_e_c_a_m_data.html#details) |
|  | |
| class | [AdvSync::DancerControlOptions](classwmx3_api_1_1_adv_sync_1_1_dancer_control_options.html) |
|  | This class contains options for dancer control. [More...](classwmx3_api_1_1_adv_sync_1_1_dancer_control_options.html#details) |
|  | |
| class | [AdvSync::DancerControlStatus](classwmx3_api_1_1_adv_sync_1_1_dancer_control_status.html) |
|  | This class contains the status for dancer control. [More...](classwmx3_api_1_1_adv_sync_1_1_dancer_control_status.html#details) |
|  | |
| class | [AdvVelocity](classwmx3_api_1_1_adv_velocity.html) |
|  | **This class contains advanced velocity command functions.**  [More...](classwmx3_api_1_1_adv_velocity.html#details) |
|  | |
| class | [AdvMotion](classwmx3_api_1_1_adv_motion.html) |
|  | **This class contains advanced position command functions.**  [More...](classwmx3_api_1_1_adv_motion.html#details) |
|  | |
| class | [AdvMotion::SplinePoint](classwmx3_api_1_1_adv_motion_1_1_spline_point.html) |
|  | This class contains data for a spline point. [More...](classwmx3_api_1_1_adv_motion_1_1_spline_point.html#details) |
|  | |
| class | [AdvMotion::PointTimeSplineCommand](classwmx3_api_1_1_adv_motion_1_1_point_time_spline_command.html) |
|  | This class contains data for a spline command in which the time at each point is specified. [More...](classwmx3_api_1_1_adv_motion_1_1_point_time_spline_command.html#details) |
|  | |
| class | [AdvMotion::TotalTimeSplineCommand](classwmx3_api_1_1_adv_motion_1_1_total_time_spline_command.html) |
|  | This class contains data for a spline command in which the total time is specified. [More...](classwmx3_api_1_1_adv_motion_1_1_total_time_spline_command.html#details) |
|  | |
| class | [AdvMotion::ProfileSplineCommand](classwmx3_api_1_1_adv_motion_1_1_profile_spline_command.html) |
|  | This class contains data for a spline command in which the spline is traversed using a motion profile. [More...](classwmx3_api_1_1_adv_motion_1_1_profile_spline_command.html#details) |
|  | |
| class | [AdvMotion::VelAccLimitedSplineCommand](classwmx3_api_1_1_adv_motion_1_1_vel_acc_limited_spline_command.html) |
|  | This class contains data for a spline command in which the spline is traversed while staying within the specified velocity and acceleration limits for each axis. [More...](classwmx3_api_1_1_adv_motion_1_1_vel_acc_limited_spline_command.html#details) |
|  | |
| class | [AdvMotion::PathIntplSegmentType](classwmx3_api_1_1_adv_motion_1_1_path_intpl_segment_type.html) |
|  | This enumerator class enumerates the segment types of motion segments in a path interpolation. [More...](classwmx3_api_1_1_adv_motion_1_1_path_intpl_segment_type.html#details) |
|  | |
| class | [AdvMotion::PathIntplOutputType](classwmx3_api_1_1_adv_motion_1_1_path_intpl_output_type.html) |
|  | This enumerator class enumerates the output types of outputs in a path interpolation. [More...](classwmx3_api_1_1_adv_motion_1_1_path_intpl_output_type.html#details) |
|  | |
| class | [AdvMotion::PathIntplOutputSource](classwmx3_api_1_1_adv_motion_1_1_path_intpl_output_source.html) |
|  | This enumerator class enumerates the output sources of outputs in a path interpolation. [More...](classwmx3_api_1_1_adv_motion_1_1_path_intpl_output_source.html#details) |
|  | |
| class | [AdvMotion::PathIntplCoordinateType](classwmx3_api_1_1_adv_motion_1_1_path_intpl_coordinate_type.html) |
|  | This enumerator class enumerates the coordinate types of path interpolations. The coordinate type determines how the coordinates are specified when defining positions in a path interpolation. [More...](classwmx3_api_1_1_adv_motion_1_1_path_intpl_coordinate_type.html#details) |
|  | |
| class | [AdvMotion::PathIntplCommand](classwmx3_api_1_1_adv_motion_1_1_path_intpl_command.html) |
|  | This class contains data for a path interpolation motion command. [More...](classwmx3_api_1_1_adv_motion_1_1_path_intpl_command.html#details) |
|  | |
| class | [AdvMotion::PathIntplAdditionalCommand](classwmx3_api_1_1_adv_motion_1_1_path_intpl_additional_command.html) |
|  | This class contains data for additional interpolation segment data for path interpolation. [More...](classwmx3_api_1_1_adv_motion_1_1_path_intpl_additional_command.html#details) |
|  | |
| class | [AdvMotion::PathIntpl3DCommand](classwmx3_api_1_1_adv_motion_1_1_path_intpl3_d_command.html) |
|  | This class contains data for a 3D path interpolation motion command. [More...](classwmx3_api_1_1_adv_motion_1_1_path_intpl3_d_command.html#details) |
|  | |
| class | [AdvMotion::PathIntpl3DAdditionalCommand](classwmx3_api_1_1_adv_motion_1_1_path_intpl3_d_additional_command.html) |
|  | This class contains data for additional interpolation segment data for 3D path interpolation. [More...](classwmx3_api_1_1_adv_motion_1_1_path_intpl3_d_additional_command.html#details) |
|  | |
| class | [AdvMotion::PathIntplWithRotationConfiguration](classwmx3_api_1_1_adv_motion_1_1_path_intpl_with_rotation_configuration.html) |
|  | This class contains the configuration data for a path interpolation with rotation channel. [More...](classwmx3_api_1_1_adv_motion_1_1_path_intpl_with_rotation_configuration.html#details) |
|  | |
| class | [AdvMotion::PathIntplWithRotationCommandPoint](classwmx3_api_1_1_adv_motion_1_1_path_intpl_with_rotation_command_point.html) |
|  | This class contains data for one point in the path interpolation with rotation motion command. [More...](classwmx3_api_1_1_adv_motion_1_1_path_intpl_with_rotation_command_point.html#details) |
|  | |
| class | [AdvMotion::PathIntplWithRotationCommand](classwmx3_api_1_1_adv_motion_1_1_path_intpl_with_rotation_command.html) |
|  | This class contains data for a path interpolation with rotation command. [More...](classwmx3_api_1_1_adv_motion_1_1_path_intpl_with_rotation_command.html#details) |
|  | |
| class | [AdvMotion::PathIntplWithRotationState](classwmx3_api_1_1_adv_motion_1_1_path_intpl_with_rotation_state.html) |
|  | This enumerator class enumerates the path interpolation with rotation states. [More...](classwmx3_api_1_1_adv_motion_1_1_path_intpl_with_rotation_state.html#details) |
|  | |
| class | [AdvMotion::PathIntplWithRotationStatus](classwmx3_api_1_1_adv_motion_1_1_path_intpl_with_rotation_status.html) |
|  | This class contains status data for a path interpolation with rotation channel. [More...](classwmx3_api_1_1_adv_motion_1_1_path_intpl_with_rotation_status.html#details) |
|  | |
| class | [AdvMotion::PathIntplLookaheadSegmentType](classwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_segment_type.html) |
|  | This enumerator class enumerates the segment types of motion segments in a path interpolation with look ahead. [More...](classwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_segment_type.html#details) |
|  | |
| class | [AdvMotion::PathIntplLookaheadCoordinateType](classwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_coordinate_type.html) |
|  | This enumerator class enumerates the coordinate types of path interpolations with look ahead. The coordinate type determines how the coordinates are specified when defining positions in a path interpolation with look ahead. [More...](classwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_coordinate_type.html#details) |
|  | |
| class | [AdvMotion::PathIntplLookaheadConfiguration](classwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_configuration.html) |
|  | This class contains the configuration data for a path interpolation with look ahead channel. [More...](classwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_configuration.html#details) |
|  | |
| class | [AdvMotion::PathIntplLookaheadCommandPoint](classwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_command_point.html) |
|  | This class contains data for one point in the path interpolation with look ahead motion command. [More...](classwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_command_point.html#details) |
|  | |
| union | [AdvMotion::PathIntplLookaheadCommandPoint::Data](unionwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_command_point_1_1_data.html) |
|  | This union defines the structs containing parameters for each segment type. The parameters should be specified in the struct corresponding to the [PathIntplLookaheadSegmentType](classwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_segment_type.html) of this point. [More...](unionwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_command_point_1_1_data.html#details) |
|  | |
| struct | [AdvMotion::PathIntplLookaheadCommandPoint::Data::Linear](structwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_command_point_1_1_data_1_1_linear.html) |
|  | This structure contains the arguments for the [Linear](classwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_segment_type.html#adf1f3edb9115acb0a1e04209b7a9937ba1a1f3bc55fefa098d9034cc46e2e7a2b) segment type. [More...](structwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_command_point_1_1_data_1_1_linear.html#details) |
|  | |
| struct | [AdvMotion::PathIntplLookaheadCommandPoint::Data::CenterAndLengthCircular](structwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_command_point_1_1_data_1_1_center_and_length_circular.html) |
|  | This structure contains the arguments for the [CenterAndLengthCircular](classwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_segment_type.html#adf1f3edb9115acb0a1e04209b7a9937ba16180b9d3a2a400d3df7e581c20359da) segment type. [More...](structwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_command_point_1_1_data_1_1_center_and_length_circular.html#details) |
|  | |
| struct | [AdvMotion::PathIntplLookaheadCommandPoint::Data::CenterAndEndCircular](structwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_command_point_1_1_data_1_1_center_and_end_circular.html) |
|  | This structure contains the arguments for the [CenterAndEndCircular](classwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_segment_type.html#adf1f3edb9115acb0a1e04209b7a9937ba9aaf6420f6cb02ebbe90eb1fe83e89d3) segment type. [More...](structwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_command_point_1_1_data_1_1_center_and_end_circular.html#details) |
|  | |
| struct | [AdvMotion::PathIntplLookaheadCommandPoint::Data::ThroughAndEndCircular](structwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_command_point_1_1_data_1_1_through_and_end_circular.html) |
|  | This structure contains the arguments for the [ThroughAndEndCircular](classwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_segment_type.html#adf1f3edb9115acb0a1e04209b7a9937ba02eb6d17c799c9e77ea03efc72b9368a) segment type. [More...](structwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_command_point_1_1_data_1_1_through_and_end_circular.html#details) |
|  | |
| struct | [AdvMotion::PathIntplLookaheadCommandPoint::Data::LengthAndEndCircular](structwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_command_point_1_1_data_1_1_length_and_end_circular.html) |
|  | This structure contains the arguments for the [LengthAndEndCircular](classwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_segment_type.html#adf1f3edb9115acb0a1e04209b7a9937ba7de6ef40349723f9bb3cdefd6780994d) segment type. [More...](structwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_command_point_1_1_data_1_1_length_and_end_circular.html#details) |
|  | |
| struct | [AdvMotion::PathIntplLookaheadCommandPoint::Data::RadiusAndEndCircular](structwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_command_point_1_1_data_1_1_radius_and_end_circular.html) |
|  | This structure contains the arguments for the [RadiusAndEndCircular](classwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_segment_type.html#adf1f3edb9115acb0a1e04209b7a9937ba72e8c35f9872c4db6534b1477f3e6889) segment type. [More...](structwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_command_point_1_1_data_1_1_radius_and_end_circular.html#details) |
|  | |
| struct | [AdvMotion::PathIntplLookaheadCommandPoint::Data::ThroughAndEnd3DCircular](structwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_command_point_1_1_data_1_1_through_and_end3_d_circular.html) |
|  | This structure contains the arguments for the [ThroughAndEnd3DCircular](classwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_segment_type.html#adf1f3edb9115acb0a1e04209b7a9937ba02249175e1f8e5153675bab1bedc1fd3) segment type. [More...](structwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_command_point_1_1_data_1_1_through_and_end3_d_circular.html#details) |
|  | |
| struct | [AdvMotion::PathIntplLookaheadCommandPoint::Data::Sleep](structwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_command_point_1_1_data_1_1_sleep.html) |
|  | This structure contains arguments for the [Sleep](classwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_segment_type.html#adf1f3edb9115acb0a1e04209b7a9937ba5b382c5c9788ae9f606d475a6709e721) segment type. [More...](structwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_command_point_1_1_data_1_1_sleep.html#details) |
|  | |
| struct | [AdvMotion::PathIntplLookaheadCommandPoint::Data::SetOutputBit](structwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_command_point_1_1_data_1_1_set_output_bit.html) |
|  | This structure contains arguments for the [SetOutputBit](classwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_segment_type.html#adf1f3edb9115acb0a1e04209b7a9937bad2bfad21dc65d248f3ef6741a44c249e) segment type. [More...](structwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_command_point_1_1_data_1_1_set_output_bit.html#details) |
|  | |
| class | [AdvMotion::PathIntplLookaheadCommand](classwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_command.html) |
|  | This class contains data for path interpolation with look ahead. [More...](classwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_command.html#details) |
|  | |
| class | [AdvMotion::PathIntplLookaheadState](classwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_state.html) |
|  | This enumerator class enumerates the states of a path interpolation with look ahead channel. [More...](classwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_state.html#details) |
|  | |
| class | [AdvMotion::PathIntplLookaheadStatus](classwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_status.html) |
|  | This class contains status data for a path interpolation with look ahead channel. [More...](classwmx3_api_1_1_adv_motion_1_1_path_intpl_lookahead_status.html#details) |
|  | |
| class | [AdvMotion::PosCommand](classwmx3_api_1_1_adv_motion_1_1_pos_command.html) |
|  | This class contains data for a position command. [More...](classwmx3_api_1_1_adv_motion_1_1_pos_command.html#details) |
|  | |
| class | [AdvMotion::CoordinatedPosCommand](classwmx3_api_1_1_adv_motion_1_1_coordinated_pos_command.html) |
|  | This class contains data for a coordinated position command. [More...](classwmx3_api_1_1_adv_motion_1_1_coordinated_pos_command.html#details) |
|  | |
| class | [AdvMotion::CoordinatedJerkRatioPosCommand](classwmx3_api_1_1_adv_motion_1_1_coordinated_jerk_ratio_pos_command.html) |
|  | This class contains data for a coordinated position command with two or more axes. [More...](classwmx3_api_1_1_adv_motion_1_1_coordinated_jerk_ratio_pos_command.html#details) |
|  | |
| class | [AdvMotion::TwoLinkLinearCommand](classwmx3_api_1_1_adv_motion_1_1_two_link_linear_command.html) |
|  | This class contains data for a two link motion command for a linear axis. [More...](classwmx3_api_1_1_adv_motion_1_1_two_link_linear_command.html#details) |
|  | |
| class | [AdvMotion::TwoLinkRotaryCommand](classwmx3_api_1_1_adv_motion_1_1_two_link_rotary_command.html) |
|  | This class contains data for a two link motion command for a rotary axis. [More...](classwmx3_api_1_1_adv_motion_1_1_two_link_rotary_command.html#details) |
|  | |
| class | [AdvMotion::SimulatePathIntplCommand](classwmx3_api_1_1_adv_motion_1_1_simulate_path_intpl_command.html) |
|  | This class contains data for simulating a path interpolation motion command. [More...](classwmx3_api_1_1_adv_motion_1_1_simulate_path_intpl_command.html#details) |
|  | |
| class | [AdvMotion::SimulatePathIntpl3DCommand](classwmx3_api_1_1_adv_motion_1_1_simulate_path_intpl3_d_command.html) |
|  | This class contains data for simulating a 3D path interpolation motion. [More...](classwmx3_api_1_1_adv_motion_1_1_simulate_path_intpl3_d_command.html#details) |
|  | |
| class | [AdvancedMotion](classwmx3_api_1_1_advanced_motion.html) |
|  | **This class contains advanced motion functions.**  [More...](classwmx3_api_1_1_advanced_motion.html#details) |
|  | |

| Variables | |
| --- | --- |
| static const int | [maxSplineDimensions](namespacewmx3_api_1_1constants.html#ae3e30abaa22640e7612960efe5cde375) = 8 |
|  | The maximum number of axes in a spline interpolation (also see [Advanced Motion Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__a_d_v_a_n_c_e_d_m_o_t_i_o_n.html)). |
|  | |
| static const int | [maxSplineChannel](namespacewmx3_api_1_1constants.html#a1f910c3f78533d599440ca7845c73e90) = 128 |
|  | The maximum number of spline execution channels (also see [Advanced Motion Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__a_d_v_a_n_c_e_d_m_o_t_i_o_n.html)). |
|  | |
| static const int | [maxPathInterpolateAppendPoints](namespacewmx3_api_1_1constants.html#a389a4b58f947ab03d2f1db4049f4d936) = 512 |
|  | The maximum number of path interpolation points that may be appended to a path interpolation sequence with a single command (also see [Advanced Motion Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__a_d_v_a_n_c_e_d_m_o_t_i_o_n.html)). |
|  | |
| static const int | [maxPathInterpolateOutputs](namespacewmx3_api_1_1constants.html#a59dd7d5514e5674a27d2bc1f76fbe8ab) = 512 |
|  | The maximum number of outputs that may be defined in a path interpolation sequence (also see [Advanced Motion Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__a_d_v_a_n_c_e_d_m_o_t_i_o_n.html)). |
|  | |
| static const int | [maxPathInterpolateDimensions](namespacewmx3_api_1_1constants.html#ad74a5ea4e28a4f599400730ac1abeb1b) = 2 |
|  | The maximum number of axes that may be controlled by a path interpolation sequence (also see [Advanced Motion Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__a_d_v_a_n_c_e_d_m_o_t_i_o_n.html)). |
|  | |
| static const int | [max3DPathInterpolateDimensions](namespacewmx3_api_1_1constants.html#a169a4164d55d1fc9c20f9ffeccc68b4f) = 3 |
|  | The maximum number of axes that may be controlled by a 3D path interpolation sequence (also see [Advanced Motion Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__a_d_v_a_n_c_e_d_m_o_t_i_o_n.html)). |
|  | |
| static const int | [maxPathIntplWithRotationAppendPoints](namespacewmx3_api_1_1constants.html#aa727130913c6f319d0304097cbe00901) = 1024 |
|  | The maximum number of path interpolation points that may be appended to a path interpolation with rotation sequence by a single function call (also see [Advanced Motion Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__a_d_v_a_n_c_e_d_m_o_t_i_o_n.html)). |
|  | |
| static const int | [maxPathIntplWithRotationChannel](namespacewmx3_api_1_1constants.html#adf3ebb02eb796da51f9122306631c256) = 128 |
|  | The maximum number of path interpolation with rotation channels (also see [Advanced Motion Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__a_d_v_a_n_c_e_d_m_o_t_i_o_n.html)). |
|  | |
| static const int | [maxPathIntplLookaheadDimensions](namespacewmx3_api_1_1constants.html#a93cc6cf1d9086de6e42fef34d5b6ffa9) = 6 |
|  | The maximum number of axes that may be controlled by a path interpolation with look ahead sequence (also see [Advanced Motion Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__a_d_v_a_n_c_e_d_m_o_t_i_o_n.html)). |
|  | |
| static const int | [maxPathIntplLookaheadAppendPoints](namespacewmx3_api_1_1constants.html#aa0543587dee8546fd156367211c3e348) = 1500 |
|  | The maximum number of path interpolation points that may be appended to a path interpolation with look ahead sequence by a single function call (also see [Advanced Motion Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__a_d_v_a_n_c_e_d_m_o_t_i_o_n.html)). |
|  | |
| static const int | [maxPathIntplLookaheadChannel](namespacewmx3_api_1_1constants.html#a85a5145a1f8152fc0f6e7d13b0a424d7) = 128 |
|  | The maximum number of path interpolation with look ahead channels (also see [Advanced Motion Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__a_d_v_a_n_c_e_d_m_o_t_i_o_n.html)). |
|  | |
| static const int | [maxPathIntplLookaheadOutputPerSegment](namespacewmx3_api_1_1constants.html#ab16ef367e6f3c1fe0ee66bfe3fb71c04) = 128 |
|  | The maximum number of outputs that may be defined per segment in a path interpolation with look ahead sequence (also see [Advanced Motion Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__a_d_v_a_n_c_e_d_m_o_t_i_o_n.html)). |
|  | |
| static const int | [maxPathIntplLookaheadSmoothingCycles](namespacewmx3_api_1_1constants.html#ad3c41ba0bc6c234dea1deec9995869a1) = 2000 |
|  | The maximum number of cycles of smoothing that can be applied to path interpolation with look ahead. |
|  | |
| static const int | [maxPathIntplLookaheadAuxiliaryAxes](namespacewmx3_api_1_1constants.html#a96c7e2e4f9e2ac443c3f649931999f6a) = 3 |
|  | The maximum number of auxiliary axes per segment in a path interpolation with look ahead sequence. |
|  | |
| static const int | [maxEcamPoints](namespacewmx3_api_1_1constants.html#af647e98b7f0e5c817ca41c5024004855) = 4096 |
|  | The maximum number of E-CAM points that may be defined per E-CAM channel (also see [Advanced Motion Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__a_d_v_a_n_c_e_d_m_o_t_i_o_n.html)). |
|  | |
| static const int | [maxEcamChannel](namespacewmx3_api_1_1constants.html#aba10cd7caabccdaa2fd51a37686c8a29) = 8 |
|  | The maximum number of E-CAM channels (also see [Advanced Motion Constants](_w_m_x_d_o_c__c_o_n_s_t_a_n_t_s__a_d_v_a_n_c_e_d_m_o_t_i_o_n.html)). |
|  | |




* [common](dir_bdd9a5d540de89e9fe90efdfc6973a4f.html)
* [include](dir_11fbc4217d50ab21044e5ad6614aede5.html)
* [AdvancedMotionApi.h](_advanced_motion_api_8h.html)



   