import os
import open3d as o3d


def read_obj():
    mesh_list = []
    for root, dirs, files in os.walk('F:\BaiduNetdiskDownload\OBJ\Data'):
        for file in files:
            if file.endswith('.obj'):
                obj_file_path = os.path.join(root, file)
                mesh = o3d.io.read_triangle_mesh(obj_file_path)
                mesh_list.append(mesh)
    o3d.visualization.draw_geometries(mesh_list)
    # print(mesh_list)


def read_ply():
    ply_list = []
    for root, dirs, files in os.walk('F:\BaiduNetdiskDownload\PLY'):
        for file in files:
            if file.endswith('.ply'):
                ply_file_path = os.path.join(root, file)
                pcd = o3d.io.read_point_cloud(ply_file_path)
                ply_list.append(pcd)
    o3d.visualization.draw_geometries(ply_list, window_name="大红鹰", width=1024, height=768)

    # # 获取点云数据
    # points = pcd.points
    #
    # # 打印前三个点的坐标
    # for i in range(min(3, len(points))):
    #     print("Point", i + 1, ":", points[i])


if __name__ == '__main__':
    # read_obj()
    read_ply()
