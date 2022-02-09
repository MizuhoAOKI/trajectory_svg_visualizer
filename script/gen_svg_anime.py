import os, sys
PROJECT_ROOT = os.path.join(os.path.dirname(__file__), '..')
sys.path.append(PROJECT_ROOT)
from include.csvhandler import *
from include.svg_visualizer import *

# settings
REFERENCE_PATH  = os.path.join(PROJECT_ROOT, "csv/ovalpath_r15m.csv")
VEHICLE_LOG     = os.path.join(PROJECT_ROOT, "csv/vehicle_state_log.csv")
OUTPUT_SVG_PATH = os.path.join(PROJECT_ROOT, "result/svg_animation.svg")

# Load csv and visualize svg animation
def gen_svg_anime():

    print("Loading reference path")
    ref = CSVHandler(REFERENCE_PATH)
    ref.read_csv(ignore_row_num=1)

    # Note that timestamp should start from 0.0
    print("Loading vehicle state log")
    log = CSVHandler(VEHICLE_LOG)
    log.read_csv(ignore_row_num=1)

    print("Generate svg animation")
    try:
        svg_visualizer(
            timestamp=np.ravel(log.points[:,0]), # set timestamp data
            car_x_ary=np.ravel(log.points[:,1]), car_y_ary=np.ravel(log.points[:,2]), # set vehicle location in x-y plane
            ref_x_ary=np.ravel(ref.points[:,0]), ref_y_ary=np.ravel(ref.points[:,1]), # set reference path points
            outputpath=OUTPUT_SVG_PATH # set output path of svg animation
        )
    except:
        print("Error occured and program interruped.")
        print(f"Check your csv files at {REFERENCE_PATH} and {VEHICLE_LOG}")
        return False

    print(f"Successfully output svg animation at {OUTPUT_SVG_PATH}")
    return True

if __name__ == "__main__":
    gen_svg_anime()