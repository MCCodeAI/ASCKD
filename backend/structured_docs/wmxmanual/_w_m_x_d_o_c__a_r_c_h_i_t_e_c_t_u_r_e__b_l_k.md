




WMX3 User Manual: Function Calls That Are Blocking










| Logo | WMX3 User Manual  3.6u1 |
| --- | --- |







Function Calls That Are Blocking  

Most functions in the WMX3 library are non-blocking, meaning that they will finish execution and return processing to the calling thread within a few microseconds or less.

However, some functions or conditions will cause functions to block for a length of time up to one communication cycle or more. The causes of these delays and potential workarounds are discussed in this page.

---

Function Calls During Interrupt Processing
------------------------------------------

The WMX3 engine processes the interrupt (see [Function Calls Affected by Interrupts](_w_m_x_d_o_c__a_r_c_h_i_t_e_c_t_u_r_e__i_p_t.html)) every cyclic period ([Cycle Time Milliseconds](_w_m_x_d_o_c__s_t_a_t_u_s__s_y_s_t_e_m.html#WMXDOC_STATUS_MAIN_CYCLE_TIME_MILLISECONDS)) to communicate with the servo network. If a WMX3 library function is called while the engine is processing the interrupt, or if the interrupt occurs before the function completes, the execution of the function will be delayed until the interrupt finishes.

The time taken to process the interrupt is affected by the speed of the CPU, the number of axes in the network, and the function that is currently executed by the axes.

Certain functions do not need to communicate with the engine, and will execute with no delay even if the function is called while the WMX3 engine is processing the interrupt. These functions include:

* [ErrorToString](classwmx3_api_1_1_w_m_x3_api.html#a8e6c982ca071233d1bf89493bed7058d) (of every module)
* [GetLibVersion](classwmx3_api_1_1_w_m_x3_api.html#a5a4bf0cefa3c789f566711f64bd4bdfe) (of every module)
* [WMX3Api::GetIMDllVersion](classwmx3_api_1_1_w_m_x3_api.html#aee9938bfa32acd1509d138ac20e5de92)
* [CoreMotion::GetStatus](classwmx3_api_1_1_core_motion.html#afd1be408f4bcfb5c8e44a5dbbecf8b9d)
* [Io::SetOutBitEx](classwmx3_api_1_1_io.html#a53dd3c3e281bf0eb2aeec00274c8f2bd)
* [Io::SetOutByteEx](classwmx3_api_1_1_io.html#a6a8a7efa44bbdc7e141c14c0f84736aa)
* [Io::SetOutBytesEx](classwmx3_api_1_1_io.html#ab32458850504551e7f00d16c056cde63)
* [Io::SetOutBitsEx](classwmx3_api_1_1_io.html#aad6229fed81ccc17a0e6b998aafb7f1d)
* [Io::SetOutAnalogDataCharEx](classwmx3_api_1_1_io.html#ab9795e95b41668b38baf7a037d8742d5)
* [Io::SetOutAnalogDataUCharEx](classwmx3_api_1_1_io.html#ab9817f9d6c0215fb342acae35e25f86f)
* [Io::SetOutAnalogDataShortEx](classwmx3_api_1_1_io.html#a4abe87b55bf04285d494433233a2471f)
* [Io::SetOutAnalogDataUShortEx](classwmx3_api_1_1_io.html#a8d0bd19b6efc81751c01251b295064bf)
* [Io::SetOutAnalogDataIntEx](classwmx3_api_1_1_io.html#a5dd9058857782d811c714011add0cf71)
* [Io::SetOutAnalogDataUIntEx](classwmx3_api_1_1_io.html#a0a521043d0564701ec8587a5b7b7de36)
* [Io::GetInBitEx](classwmx3_api_1_1_io.html#a5daee926eabb0810205edf3700f79df6)
* [Io::GetInByteEx](classwmx3_api_1_1_io.html#a45bd2bec6ee1e2d38b80ddfa657b2e35)
* [Io::GetInBytesEx](classwmx3_api_1_1_io.html#a708a4f2c9aa940d2840f554a86124b1f)
* [Io::GetInAnalogDataCharEx](classwmx3_api_1_1_io.html#a664923130faf26fd7276c45d852963ee)
* [Io::GetInAnalogDataUCharEx](classwmx3_api_1_1_io.html#af3ce1b383a2d8be3c435ee067ddc3ea3)
* [Io::GetInAnalogDataShortEx](classwmx3_api_1_1_io.html#a4d6937333c4fdf088909f0e755ae140d)
* [Io::GetInAnalogDataUShortEx](classwmx3_api_1_1_io.html#a24876841513b03ff28e6e9a0404155fb)
* [Io::GetInAnalogDataIntEx](classwmx3_api_1_1_io.html#a99c30ddb2123ebb108996f4109f5a205)
* [Io::GetInAnalogDataUIntEx](classwmx3_api_1_1_io.html#a60d8adedfff5412085f189785af99412)
* [Io::GetOutBitEx](classwmx3_api_1_1_io.html#a918c44d1c5342f1cbdf37933d1985429)
* [Io::GetOutByteEx](classwmx3_api_1_1_io.html#a26be59ac05fb34acdfe08d6ea139a294)
* [Io::GetOutBytesEx](classwmx3_api_1_1_io.html#a570db24f10af0c14d88be4c662a13644)
* [Io::GetOutAnalogDataCharEx](classwmx3_api_1_1_io.html#a2a13fee83bfb0a2c22392cea779f662d)
* [Io::GetOutAnalogDataUCharEx](classwmx3_api_1_1_io.html#a37ae30d97ce50818570354a39f10c968)
* [Io::GetOutAnalogDataShortEx](classwmx3_api_1_1_io.html#a0b227995074d385046e71da18cb9d41c)
* [Io::GetOutAnalogDataUShortEx](classwmx3_api_1_1_io.html#ae46b5bafab2cb795b90dcb851eea78a6)
* [Io::GetOutAnalogDataIntEx](classwmx3_api_1_1_io.html#ac0480f20550158c3383a10743054fd96)
* [Io::GetOutAnalogDataUIntEx](classwmx3_api_1_1_io.html#a9b6d8967748befc6cb35eccd34d5e9d7)

Another method of avoiding this delay is to assign more than one CPU core to the RTX operating system using the affinityMask argument of the function that starts the WMX3 engine ([CreateDevice](classwmx3_api_1_1_w_m_x3_api.html#acdf68c4d0df80ffe358ab80410053301), [StartEngine](classwmx3_api_1_1_w_m_x3_api.html#a1c5d4ea51b8b20fcaea20d467e48c216), or [RestartEngine](classwmx3_api_1_1_w_m_x3_api.html#a4fd859e4bc08434652b1abb318468182)). This allows the second core to execute a function call even while the first core processes the interrupt. ***This requires an RTX license that supports two or more cores.***

---

"Wait Until Motion Start" Parameter
-----------------------------------

If the [Wait Until Motion Start](_w_m_x_d_o_c__p_a_r_a_m__m_o_t_i_o_n.html#WMXDOC_PARAM_MOTION_API_WAIT_UNTIL_MOTION_START) parameter is set to TRUE, most motion functions will block and not return until the end of the next interrupt. This allows the user to not check if the motion has started before executing an override motion function from the same thread.

If this parameter is set to FALSE, or if the override motion command will be called from a different thread, the [Command Ready](_w_m_x_d_o_c__s_t_a_t_u_s__a_x_i_s.html#WMXDOC_STATUS_MAIN_COMMAND_READY) status must be checked before calling the override motion function. If the override motion function is called before the first interrupt after the motion starts, the [StartingPreviousCommand](classwmx3_api_1_1_error_code.html#ac36f475ca5b446f4fde4c9b90bec77c8ac62c6463ebff8c75e776fe50d8e0f0f9) error will be returned. For example, if [Cycle Time Milliseconds](_w_m_x_d_o_c__s_t_a_t_u_s__s_y_s_t_e_m.html#WMXDOC_STATUS_MAIN_CYCLE_TIME_MILLISECONDS) is 1ms, then calling [StartPos](classwmx3_api_1_1_motion.html#a77568fe64b1c464554481daad716c2d9) and then calling [StartPos](classwmx3_api_1_1_motion.html#a77568fe64b1c464554481daad716c2d9) again before 1ms elapses can cause this error to be returned.

The [Wait Until Motion Start](_w_m_x_d_o_c__p_a_r_a_m__m_o_t_i_o_n.html#WMXDOC_PARAM_MOTION_API_WAIT_UNTIL_MOTION_START) parameter is set to TRUE by default, but can be changed using [SetParam](classwmx3_api_1_1_config.html#a61ce281e23455c83db99821e67307d4a) or any other function that sets this parameter.

The following functions are affected by this parameter.

* [Motion::StartPos](classwmx3_api_1_1_motion.html#a77568fe64b1c464554481daad716c2d9)
* [Motion::StartMov](classwmx3_api_1_1_motion.html#a5811733ce4f6706bf9302e1b21876e81)
* [Motion::StartLinearIntplPos](classwmx3_api_1_1_motion.html#a054d1e42b521d1eb61fc6866b0153763)
* [Motion::StartLinearIntplMov](classwmx3_api_1_1_motion.html#aedb8dd0e998609a3ae346e4ab191d128)
* [Motion::StartCircularIntplPos](classwmx3_api_1_1_motion.html#a9af0cada31f217dc1fd7bd57f0274d7a)
* [Motion::StartCircularIntplMov](classwmx3_api_1_1_motion.html#a28b74a0090f5be6caaa823df852ffeb8)
* [Motion::StartHelicalIntplPos](classwmx3_api_1_1_motion.html#abe501d6c20f4881d5ed6f950cadc1198)
* [Motion::StartHelicalIntplMov](classwmx3_api_1_1_motion.html#ae477791ce796689d78e3cc7664cb3beb)
* [Motion::StartJog](classwmx3_api_1_1_motion.html#a2fa6e0215067395c3f75560c74319131)
* [Motion::StartPosToJog](classwmx3_api_1_1_motion.html#a84cda0ce9c4d23425949166130fb17e9)
* [Motion::StartMovToJog](classwmx3_api_1_1_motion.html#acd367df9df86b8521e069e1d3cffe95b)
* [Motion::Stop](classwmx3_api_1_1_motion.html#a5f1104dad986ac278deaf35d50be6a68)
* [Motion::ExecQuickStop](classwmx3_api_1_1_motion.html#abcdcdb7834dadebd7d9b0ef517072f7c)
* [Motion::ExecTimedStop](classwmx3_api_1_1_motion.html#a1153e73f0dc38da8dea5a0373cf2e9e0)
* [Motion::Pause](classwmx3_api_1_1_motion.html#aff6a9531e9f219416b6f6ce4601deffd)
* [Motion::Resume](classwmx3_api_1_1_motion.html#a08b7284d2100e95c7fcf84ec81146f23)
* [Motion::OverridePos](classwmx3_api_1_1_motion.html#a70354675e0ae10272418fd96bccead14)
* [Motion::OverrideMov](classwmx3_api_1_1_motion.html#acd4b1de6f84d926d9b21f7aa375560ce)
* [Motion::OverrideVel](classwmx3_api_1_1_motion.html#ab61b212082766ad60a17815e5f9dbbc5)
* [Motion::OverrideAcc](classwmx3_api_1_1_motion.html#a3806ed700a1146548f6125a7eb06ac38)
* [Motion::OverrideDec](classwmx3_api_1_1_motion.html#a151b2c4bcc924846b60e6d1000fa8ab0)
* [Motion::OverrideJerkAcc](classwmx3_api_1_1_motion.html#a9750659e7b6b93142cf8b3f78a5c3114)
* [Motion::OverrideJerkDec](classwmx3_api_1_1_motion.html#a34760b64482dd52d80e45bc14abf4a68)
* [Motion::OverrideProfile](classwmx3_api_1_1_motion.html#a7ac0753148aa4425359d7ddc88559811)
* [Motion::StopJogAtPos](classwmx3_api_1_1_motion.html#a694842e701c8f060d2ae45df53ef283c)
* [Velocity::StartVel](classwmx3_api_1_1_velocity.html#ad6d050212f26fea9e3cfccce1eca3311)
* [Velocity::Stop](classwmx3_api_1_1_velocity.html#a5f1104dad986ac278deaf35d50be6a68)
* [Velocity::ExecQuickStop](classwmx3_api_1_1_velocity.html#abcdcdb7834dadebd7d9b0ef517072f7c)
* [Velocity::StartPosToVel](classwmx3_api_1_1_velocity.html#a0a6d2fb43d379acc71d960efc32e63e3)
* [Torque::StartTrq](classwmx3_api_1_1_torque.html#a3048421dae2b1a70fae40bd16e926cda)
* [Torque::StartRampTimeTrq](classwmx3_api_1_1_torque.html#a0ee8f96dadc37051a9b10f8fc23dc65c)
* [Torque::StartRampRateTrq](classwmx3_api_1_1_torque.html#a77870f0d06119577187a905e109c8f04)
* [Torque::StartPosToTrq](classwmx3_api_1_1_torque.html#a5f8f3192a7285a90573a50880eca57fb)
* [Torque::StartVelToTrq](classwmx3_api_1_1_torque.html#ad6c06ade6c14615d960a5f3b92bf71e8)
* [Home::SetCommandPos](classwmx3_api_1_1_home.html#a8b101dfc9690613ae0186125a42281d1)
* [Home::SetFeedbackPos](classwmx3_api_1_1_home.html#a74b732cd6bbfb89ec483b24392fb1664)
* [Home::SetCommandPosToFeedbackPos](classwmx3_api_1_1_home.html#a136b0b82ad2611a82469c49c20abcb3c)
* [Sync::SetSyncMasterSlave](classwmx3_api_1_1_sync.html#a59dd338c78663f1714effe54c3313906)
* [Sync::SetSyncCombine](classwmx3_api_1_1_sync.html#aea852ab03c47a1744727eda2c417b85b)
* [Sync::SetSyncGearRatio](classwmx3_api_1_1_sync.html#a66b4bcff8769008d9cf3dfa2a26f18d7) (when starting a new sync control)
* [AdvMotion::StartCSplinePos](classwmx3_api_1_1_adv_motion.html#ad5629bd13d86e1401c6a469c2916fed7)
* [AdvMotion::StartCSplineMov](classwmx3_api_1_1_adv_motion.html#ac9c57c1b837a983da575262773f37213)
* [AdvMotion::StartCBSplinePos](classwmx3_api_1_1_adv_motion.html#a8ea96a80f09001ff28993914f842322f)
* [AdvMotion::StartCBSplineMov](classwmx3_api_1_1_adv_motion.html#addf68595c647a1ecec245ab591ac1ade)
* [Motion::StartPVT](classwmx3_api_1_1_motion.html#a6148c6ca4f03bc091a7cca99d5eadd29)
* [Motion::StartPT](classwmx3_api_1_1_motion.html#aebe56252d025ae2973e305c27e109a72)
* [Motion::StartVT](classwmx3_api_1_1_motion.html#aa38794ea3114ddfe8d14cad01fe082e8)
* [Motion::StartAT](classwmx3_api_1_1_motion.html#a5ceebc42e3c009b4ebac50c256ae76db)
* [AdvMotion::StartPathIntplPos](classwmx3_api_1_1_adv_motion.html#a7c879bbd7d26d10528de4d2facf5c984)
* [AdvMotion::StartPathIntplMov](classwmx3_api_1_1_adv_motion.html#a1d2e7c24345760727dd4317d8361f5a3)
* [AdvMotion::StartPathIntpl3DPos](classwmx3_api_1_1_adv_motion.html#a15ee05ff5041683286fdf2ea46c22282)
* [AdvMotion::StartPathIntpl3DMov](classwmx3_api_1_1_adv_motion.html#a470b5a405968943345e2668c6023bed6)
* [AdvMotion::StartPathIntplWithRotation](classwmx3_api_1_1_adv_motion.html#a6a6e2baef07552c1a7dd251aae1458c7)
* [AdvMotion::StartPathIntplLookahead](classwmx3_api_1_1_adv_motion.html#af960e594c5b70eca6e428191c1a2f546)
* [AdvMotion::StartCoordinatedPos](classwmx3_api_1_1_adv_motion.html#aa4399c73e2d93fc86cf5b0fa8375fb04)
* [AdvMotion::StartTwoLinkLinearPos](classwmx3_api_1_1_adv_motion.html#aaf2ff0657bf28b364437f23455ccab53)
* [AdvMotion::StartTwoLinkLinearMov](classwmx3_api_1_1_adv_motion.html#afe719ccddf21bd641563dff2c07cce32)
* [AdvMotion::StartTwoLinkRotaryPos](classwmx3_api_1_1_adv_motion.html#a4f17bb8f0bba36dfdcb7893879797d27)
* [AdvMotion::StartTwoLinkRotaryMov](classwmx3_api_1_1_adv_motion.html#ad435c70d422f1f26a3fff4dcefcb8098)
* [AdvMotion::StartTwoLinkUntetheredLinearPos](classwmx3_api_1_1_adv_motion.html#a6c67db20de434ad3f8849188e86a52e8)
* [AdvMotion::StartTwoLinkUntetheredLinearMov](classwmx3_api_1_1_adv_motion.html#abbcff3bc88a195f7f0e0b9283f81ff21)
* [AdvMotion::StartTwoLinkUntetheredRotaryPos](classwmx3_api_1_1_adv_motion.html#a57df06a75f3598e403c1668210a870a3)
* [AdvMotion::StartTwoLinkUntetheredRotaryMov](classwmx3_api_1_1_adv_motion.html#a404d5fbe8876afe6dc23446876df5fde)

---

Functions That Block Until the End of the Next Interrupt
--------------------------------------------------------

The following functions will block and not return until the end of the next interrupt.

* [Compensation::SetPitchErrorCompensation](classwmx3_api_1_1_compensation.html#aa3225f99bd6ca271156b0f4568603494)
* [Compensation::EnablePitchErrorCompensation](classwmx3_api_1_1_compensation.html#a6bfff19303b60e06c21b639840ae01b2)
* [Compensation::Set2DPitchErrorCompensation](classwmx3_api_1_1_compensation.html#ac350d737fe21dc99debf197c2005d742)
* [Compensation::Enable2DPitchErrorCompensation](classwmx3_api_1_1_compensation.html#a6457d00a30910cea313fcac7e3530422)

---

Wait Functions
--------------

The [Wait](classwmx3_api_1_1_motion.html#a7f6670155c871d765af1a345c4ae201c) functions in the CoreMotion module will intentionally block and not return until the specified condition is satisfied. The thread executing the function will be suspended until the condition is satisfied.

---

Path Interpolation with Look Ahead
----------------------------------

Path interpolation with look ahead will require heavy processing time, especially if the number of points is very large. The [AddPathIntplWithRotationCommand](classwmx3_api_1_1_adv_motion.html#abbc8e17db71c2a9030c729e7e68d0d50) function may block for a long time (potentially hundreds of milliseconds or multiple seconds depending on the number of points) before returning.

---

RemoveEvent and ClearAllEvent
-----------------------------

The [RemoveEvent](classwmx3_api_1_1_event_control.html#aa330b3226b7ab5a51c6c2a47df59a43b) and [ClearAllEvent](classwmx3_api_1_1_event_control.html#a64ff8e43ea5d8551b35f945c69ba8be7) functions will block execution until the next interrupt finishes. The specified events are removed during the interrupt. If communication is stopped and events are not being processed, these functions are non-blocking and will remove the specified events immediately.

---

ApiBuffer Mode Change Functions
-------------------------------

The following mode change functions from the ApiBuffer module will block until the mode change completes (typically 1ms) or the mode change request times out (50ms).

* [Execute](classwmx3_api_1_1_api_buffer.html#a2dbf7eee9c7659926a3d5ea13ca5fd9b)
* [Halt](classwmx3_api_1_1_api_buffer.html#aa72903ceeafab70c16756fea25ddb52f)
* [Clear](classwmx3_api_1_1_api_buffer.html#adee1e5e02afda6acb4a79c53d6fef81b)
* [Rewind](classwmx3_api_1_1_api_buffer.html#ac235fca18a1d04775b8f7a757ea45c2e)
* [ExecuteMultipleChannel](classwmx3_api_1_1_api_buffer.html#a567a340657b6d0899503aac808c0fb22)
* [HaltMultipleChannel](classwmx3_api_1_1_api_buffer.html#a387c00921e20522176d0e9345086e456)
* [ClearMultipleChannel](classwmx3_api_1_1_api_buffer.html#a8646d7ff09b9e045d8d129e8d722e7a8)
* [RewindMultipleChannel](classwmx3_api_1_1_api_buffer.html#af8ae0d13d802d9b610493441cd0cd80f)







