
st a star
# 1 part


WMX3 User Manual: Copy Operators




## 1.1





| Logo | WMX3 User Manual  3.6u1 |
| --- | --- |







Copy Operators  

Module classes have overloaded copy assignment operators and copy constructors (see [Self Devices](_w_m_x_d_o_c__a_r_c_h_i_t_e_c_t_u_r_e__d_e_v_i_c_e__s_e_l_f__d_e_v_i_c_e.html) for a list of standard module classes).

For devices that are not [Self Devices](_w_m_x_d_o_c__a_r_c_h_i_t_e_c_t_u_r_e__d_e_v_i_c_e__s_e_l_f__d_e_v_i_c_e.html), the copy assignment operator and copy constructor will initialize the object and copy the pointer to the [WMX3Api](classwmx3_api_1_1_w_m_x3_api.html) object from the source. Therefore, the object will share the same device as the source.

The following is an example of using the copy constructor for a non-self device.

```
WMX3Api wmxlib;
CoreMotion wmxlib_cm(&wmxlib);    //Uses the device created by wmxlib
CoreMotion wmxlib_cm2(wmxlib_cm); //Uses the same device as wmxlib_cm
```

For devices that are [Self Devices](_w_m_x_d_o_c__a_r_c_h_i_t_e_c_t_u_r_e__d_e_v_i_c_e__s_e_l_f__d_e_v_i_c_e.html), the copy assignment operator and copy constructor will initialize the object and create a new self device for the object. Therefore, the object will not share the same device as the source.

The following is an example of using the copy assignment operator for a self device.

```
WMX3Api wmxlib;
CoreMotion wmxlib_cm(&wmxlib); //Uses the device created by wmxlib
CoreMotion wmxlib_cm2;         //Uses a self device

wmxlib_cm = wmxlib_cm2; //wmxlib_cm will create a new self device
```






# 2 part

a



## 2.1 



## 2.2
dde
## 2.3
顶顶顶顶
### 2.2.3
顶顶顶顶

# 3 part

# 4 part 

