# Index constants for accessing data in the Data Handler


def const(val):
    # Mock for uPy mock
    return val


class CDH_IDX:
    TIME = const(0)
    SC_STATE = const(1)
    SD_USAGE = const(2)
    CURRENT_RAM_USAGE = const(3)
    REBOOT_COUNT = const(4)
    WATCHDOG_TIMER = const(5)
    HAL_BITFLAGS = const(6)
    DETUMBLING_ERROR_FLAG = const(7)


class EPS_IDX:
    TIME_EPS = const(0)
    MAINBOARD_VOLTAGE = const(1)
    MAINBOARD_CURRENT = const(2)
    BATTERY_PACK_REPORTED_SOC = const(3)
    BATTERY_PACK_REPORTED_CAPACITY = const(4)
    BATTERY_PACK_CURRENT = const(5)
    BATTERY_PACK_VOLTAGE = const(6)
    BATTERY_PACK_MIDPOINT_VOLTAGE = const(7)
    BATTERY_PACK_TTE = const(8)
    BATTERY_PACK_TTF = const(9)
    XP_COIL_VOLTAGE = const(10)
    XP_COIL_CURRENT = const(11)
    XM_COIL_VOLTAGE = const(12)
    XM_COIL_CURRENT = const(13)
    YP_COIL_VOLTAGE = const(14)
    YP_COIL_CURRENT = const(15)
    YM_COIL_VOLTAGE = const(16)
    YM_COIL_CURRENT = const(17)
    ZP_COIL_VOLTAGE = const(18)
    ZP_COIL_CURRENT = const(19)
    ZM_COIL_VOLTAGE = const(20)
    ZM_COIL_CURRENT = const(21)
    JETSON_INPUT_VOLTAGE = const(22)
    JETSON_INPUT_CURRENT = const(23)
    RF_LDO_OUTPUT_VOLTAGE = const(24)
    RF_LDO_OUTPUT_CURRENT = const(25)
    GPS_VOLTAGE = const(26)
    GPS_CURRENT = const(27)
    XP_SOLAR_CHARGE_VOLTAGE = const(28)
    XP_SOLAR_CHARGE_CURRENT = const(29)
    XM_SOLAR_CHARGE_VOLTAGE = const(30)
    XM_SOLAR_CHARGE_CURRENT = const(31)
    YP_SOLAR_CHARGE_VOLTAGE = const(32)
    YP_SOLAR_CHARGE_CURRENT = const(33)
    YM_SOLAR_CHARGE_VOLTAGE = const(34)
    YM_SOLAR_CHARGE_CURRENT = const(35)
    ZP_SOLAR_CHARGE_VOLTAGE = const(36)
    ZP_SOLAR_CHARGE_CURRENT = const(37)
    ZM_SOLAR_CHARGE_VOLTAGE = const(38)
    ZM_SOLAR_CHARGE_CURRENT = const(39)


class ADCS_IDX:
    TIME_ADCS = const(0)
    MODE = const(1)
    GYRO_X = const(2)
    GYRO_Y = const(3)
    GYRO_Z = const(4)
    MAG_X = const(5)
    MAG_Y = const(6)
    MAG_Z = const(7)
    SUN_STATUS = const(8)
    SUN_VEC_X = const(9)
    SUN_VEC_Y = const(10)
    SUN_VEC_Z = const(11)
    ECLIPSE = const(12)
    LIGHT_SENSOR_XP = const(13)
    LIGHT_SENSOR_XM = const(14)
    LIGHT_SENSOR_YP = const(15)
    LIGHT_SENSOR_YM = const(16)
    LIGHT_SENSOR_ZP1 = const(17)
    LIGHT_SENSOR_ZP2 = const(18)
    LIGHT_SENSOR_ZP3 = const(19)
    LIGHT_SENSOR_ZP4 = const(20)
    LIGHT_SENSOR_ZM = const(21)
    XP_COIL_STATUS = const(22)
    XM_COIL_STATUS = const(23)
    YP_COIL_STATUS = const(24)
    YM_COIL_STATUS = const(25)
    ZP_COIL_STATUS = const(26)
    ZM_COIL_STATUS = const(27)
    COARSE_ATTITUDE_QW = const(28)
    COARSE_ATTITUDE_QX = const(29)
    COARSE_ATTITUDE_QY = const(30)
    COARSE_ATTITUDE_QZ = const(31)


class IMU_IDX:
    TIME_IMU = const(0)
    ACCEL_X = const(1)
    ACCEL_Y = const(2)
    ACCEL_Z = const(3)
    MAGNETOMETER_X = const(4)
    MAGNETOMETER_Y = const(5)
    MAGNETOMETER_Z = const(6)
    GYROSCOPE_X = const(7)
    GYROSCOPE_Y = const(8)
    GYROSCOPE_Z = const(9)


class GPS_IDX:
    TIME_GPS = const(0)
    GPS_MESSAGE_ID = const(1)
    GPS_FIX_MODE = const(2)
    GPS_NUMBER_OF_SV = const(3)
    GPS_GNSS_WEEK = const(4)
    GPS_GNSS_TOW = const(5)
    GPS_LATITUDE = const(6)
    GPS_LONGITUDE = const(7)
    GPS_ELLIPSOID_ALT = const(8)
    GPS_MEAN_SEA_LVL_ALT = const(9)
    GPS_GDOP = const(10)
    GPS_PDOP = const(11)
    GPS_HDOP = const(12)
    GPS_VDOP = const(13)
    GPS_TDOP = const(14)
    GPS_ECEF_X = const(15)
    GPS_ECEF_Y = const(16)
    GPS_ECEF_Z = const(17)
    GPS_ECEF_VX = const(18)
    GPS_ECEF_VY = const(19)
    GPS_ECEF_VZ = const(20)


class THERMAL_IDX:
    TIME_THERMAL = const(0)
    IMU_TEMPERATURE = const(1)
    CPU_TEMPERATURE = const(2)
    BATTERY_PACK_TEMPERATURE = const(3)


class PAYLOAD_IDX:
    pass
