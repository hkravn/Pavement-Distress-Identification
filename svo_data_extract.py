import pyzed.sl as sl
from pathlib import Path

def pointcloud(filename,frameref=0):
    svo_input_path = Path(filename)

    # Create ZED objects
    zed = sl.Camera()

    # Specify SVO Parameter
    init_params = sl.InitParameters()
    init_params.set_from_svo_file(str(svo_input_path))
    init_params.svo_real_time_mode = False # Don't convert in realtime
    init_params.coordinate_units = sl.UNIT.MILLIMETER # Use milliliter units (for depth measurements)
    init_params.coordinate_system = sl.COORDINATE_SYSTEM.IMAGE

    rt_params = sl.RuntimeParameters(
        sensing_mode = sl.SENSING_MODE.FILL,
        enable_depth = True,
        measure3D_reference_frame = sl.REFERENCE_FRAME.WORLD,
        confidence_threshold = 99,
        texture_confidence_threshold = 99
    )

    # Open the SVO file with specified parameters
    err = zed.open(init_params)
    if err != sl.ERROR_CODE.SUCCESS:
        print(repr(err))
        zed.close()
        exit()
    
    no_of_frames = zed.get_svo_number_of_frames()
    resolution = zed.get_camera_information().camera_resolution
    svo_position = 0

    if frameref<0 or frameref>no_of_frames:
        print("Reference Frame out of Bounds")

    point_cloud = sl.Mat(resolution.width, resolution.height, sl.MAT_TYPE.F32_C4, sl.MEM.CPU)

    if zed.grab() == sl.ERROR_CODE.SUCCESS:
        zed.retrieve_measure(point_cloud, sl.MEASURE.XYZRGBA,sl.MEM.CPU, resolution)


pointcloud("sample.svo")