




WMX3 User Manual: Start Communication and Servo On










| Logo | WMX3 User Manual  3.6u1 |
| --- | --- |







Start Communication and Servo On  

Cyclic communication with the servo network is started with the [StartCommunication](classwmx3_api_1_1_w_m_x3_api.html#a5c6aac8b393e06eee2c3627bd171f43e) function. Calling this function will attempt to start communication with the network using the parameters set in [Module.ini](_w_m_x_d_o_c__s_e_t_u_p__w_m_x3__m_o_d_u_l_e_i_n_i.html), the **Network Definition** files, and the **RtxTcpIp.ini** files.

Once communication has been established, the [Engine State](_w_m_x_d_o_c__s_t_a_t_u_s__s_y_s_t_e_m.html#WMXDOC_STATUS_MAIN_ENGINE_STATE) status returned by the [GetStatus](classwmx3_api_1_1_core_motion.html#afd1be408f4bcfb5c8e44a5dbbecf8b9d) function will be set to [Communicating](classwmx3_api_1_1_engine_state.html#adf1f3edb9115acb0a1e04209b7a9937ba0a7d961415a32950c3bb8d8959d2ab2e).

When communication is started for the first time after starting the engine, the [home position](_w_m_x_d_o_c__f_u_n_c__h_o_m__d_e_f_i_n_i_t_i_o_n.html) will be 0 and the position feedback ([Actual Pos](_w_m_x_d_o_c__s_t_a_t_u_s__a_x_i_s.html#WMXDOC_STATUS_MAIN_ACTUAL_POS)) will be equal to the [Encoder Feedback](_w_m_x_d_o_c__s_t_a_t_u_s__a_x_i_s.html#WMXDOC_STATUS_MAIN_ENCODER_FEEDBACK) position (divided by the [Gear Ratio](_w_m_x_d_o_c__p_a_r_a_m__a_x_i_s.html#WMXDOC_PARAM_AXIS_GEAR_RATIO_NUMERATOR)).

Communication can be stopped with the [StopCommunication](classwmx3_api_1_1_w_m_x3_api.html#a87dfd61c70f9161923b1ad48475ee2d7) function.

When communication is started, all servos will be in servo off state. Whether the servo is on or off can be checked with the [Servo On](_w_m_x_d_o_c__s_t_a_t_u_s__a_x_i_s.html#WMXDOC_STATUS_MAIN_SERVO_ON) status returned by the [GetStatus](classwmx3_api_1_1_core_motion.html#afd1be408f4bcfb5c8e44a5dbbecf8b9d) function. The servo can be turned on or off with the [SetServoOn](classwmx3_api_1_1_axis_control.html#ae1be0f391446117d353eea5cc3d92af0) function.

The servo only follows position commands ([Pos Cmd](_w_m_x_d_o_c__s_t_a_t_u_s__a_x_i_s.html#WMXDOC_STATUS_MAIN_POS_CMD)) while it is on. While the servo is off, the position command is set equal to the position feedback every cycle. Therefore, when the axis is moved by hand while the servo is off and then turned on, the position command will be equal to the position feedback just before the servo is turned on.








