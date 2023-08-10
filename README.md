# UR2Unity
# get file_server
git clone https://github.com/gramaziokohler/ros_file_server
# run file_server
rosrun file_server file_server

# run rosapi (if needed)
rosrun rosapi rosapi_node 

# run rosbridge(connect with ros#)
roslaunch rosbridge_server rosbridge_websocket.launch

# Adding RosConnector into Hierarchy
1. Add Joint State Patcher (Enable the publisher and subscriber)
2. Add Pose Stamped Publisher
